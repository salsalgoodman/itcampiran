# -*- coding: utf-8 -*-
"""
Telegram Bot for Workshop Registration
Handles user registration with online and offline payment methods
"""

import os
import io
import json
import logging
from datetime import datetime
from functools import wraps
from typing import List, Optional

import jdatetime
from dotenv import load_dotenv
from supabase import create_client, Client
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Admin IDs (comma-separated string to list)
ADMIN_IDS_STR = os.environ.get("ADMIN_IDS", "")
ADMIN_IDS = [int(admin_id.strip()) for admin_id in ADMIN_IDS_STR.split(",") if admin_id.strip()]

# Zarinpal Payment Gateway
ZARINPAL_BASE_URL = os.environ.get("ZARINPAL_URL", "https://zarinp.al/itcampiran.ir")

# Zarinpal URLs for each plan (can use same URL or different)
ZARINPAL_URLS = {
    "plan_economy": os.environ.get("ZARINPAL_URL_ECONOMY", ZARINPAL_BASE_URL),
    "plan_standard": os.environ.get("ZARINPAL_URL_STANDARD", ZARINPAL_BASE_URL),
    "plan_professional": os.environ.get("ZARINPAL_URL_PROFESSIONAL", ZARINPAL_BASE_URL),
}

# Bank account info
BANK_NAME = os.environ.get("BANK_NAME", "بانک ملت")
BANK_ACCOUNT = os.environ.get("BANK_ACCOUNT", "")
ACCOUNT_HOLDER = os.environ.get("ACCOUNT_HOLDER", "")

# Plan information
PLANS = {
    "plan_economy": {
        "name": "اقتصادی",
        "price": "۱٬۸۰۰٬۰۰۰",
        "price_num": 1800000
    },
    "plan_standard": {
        "name": "استاندارد",
        "price": "۲٬۵۰۰٬۰۰۰",
        "price_num": 2500000
    },
    "plan_professional": {
        "name": "حرفه‌ای",
        "price": "۵٬۸۰۰٬۰۰۰",
        "price_num": 5800000
    }
}

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Conversation states
SELECTING_PLAN, SELECTING_PAYMENT, WAITING_RECEIPT, WAITING_NAME, WAITING_PHONE = range(5)
WAITING_ANSWER = 10  # For answering questions


# Admin restriction decorator
def restricted(func):
    """Decorator to restrict command access to admins only"""
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        if update.effective_user.id not in ADMIN_IDS:
            logger.warning(f"Unauthorized access blocked for user {update.effective_user.id}")
            await update.message.reply_text("❌ شما دسترسی به این دستور را ندارید.")
            return
        return await func(update, context, *args, **kwargs)
    return wrapper


def check_existing_registration(telegram_id: int) -> dict:
    """Check if user already has a registration"""
    try:
        result = supabase.table("users").select("id,status").eq("telegram_id", telegram_id).execute()
        if result.data:
            return result.data[0]
        return None
    except Exception as e:
        logger.error(f"Error checking existing registration: {e}")
        return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle /start command - show welcome and plan selection"""
    user_id = update.effective_user.id
    
    # Check for existing registration
    existing = check_existing_registration(user_id)
    if existing:
        status = existing.get("status", "")
        if status == "confirmed":
            await update.message.reply_text(
                "✅ شما قبلاً ثبت‌نام کرده‌اید و ثبت‌نام شما تأیید شده است.\n"
                "منتظر پیام‌های بعدی ما باشید."
            )
            return ConversationHandler.END
        elif status == "pending":
            await update.message.reply_text(
                "⏳ شما قبلاً ثبت‌نام کرده‌اید و در انتظار تأیید هستید.\n"
                "به محض تأیید، به شما اطلاع داده خواهد شد."
            )
            return ConversationHandler.END
    
    # Welcome message with plan selection
    welcome_text = (
        "سلام! 👋\n"
        "به ورکشاپ آموزشی ما خوش آمدید.\n\n"
        "لطفاً یکی از پلن‌های زیر را انتخاب کنید:"
    )
    
    keyboard = [
        [
            InlineKeyboardButton(
                f"اقتصادی – {PLANS['plan_economy']['price']} تومان",
                callback_data="plan_economy"
            ),
            InlineKeyboardButton(
                f"استاندارد – {PLANS['plan_standard']['price']} تومان",
                callback_data="plan_standard"
            )
        ],
        [
            InlineKeyboardButton(
                f"حرفه‌ای – {PLANS['plan_professional']['price']} تومان",
                callback_data="plan_professional"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    return SELECTING_PLAN


async def on_plan_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle plan selection callback"""
    query = update.callback_query
    await query.answer()
    
    plan_choice = query.data
    plan_info = PLANS.get(plan_choice)
    
    if not plan_info:
        await query.edit_message_text("❌ خطا در انتخاب پلن. لطفاً دوباره تلاش کنید.")
        return ConversationHandler.END
    
    # Store selected plan
    context.user_data["plan"] = plan_choice
    
    # Confirmation message with payment method selection
    confirm_text = (
        f"✅ شما پلن *{plan_info['name']}* با قیمت *{plan_info['price']} تومان* را انتخاب کردید.\n\n"
        "لطفاً شیوه پرداخت را انتخاب کنید:"
    )
    
    buttons = [
        [InlineKeyboardButton("💳 پرداخت آنلاین", callback_data="pay_online")],
        [InlineKeyboardButton("🏧 کارت‌به‌کارت", callback_data="pay_offline")]
    ]
    
    await query.edit_message_text(
        confirm_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode='Markdown'
    )
    return SELECTING_PAYMENT


async def on_payment_method(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle payment method selection"""
    query = update.callback_query
    await query.answer()
    
    payment_method = query.data
    plan_choice = context.user_data.get("plan")
    plan_info = PLANS.get(plan_choice)
    
    if payment_method == "pay_online":
        # Online payment flow
        zarinpal_url = ZARINPAL_URLS.get(plan_choice, "")
        
        if not zarinpal_url:
            await query.edit_message_text(
                "❌ خطا: لینک پرداخت تنظیم نشده است. لطفاً با پشتیبانی تماس بگیرید."
            )
            return ConversationHandler.END
        
        pay_btn = InlineKeyboardButton("⭐ پرداخت از طریق زرین‌پال", url=zarinpal_url)
        
        await query.edit_message_text(
            f"💳 پرداخت آنلاین\n\n"
            f"مبلغ: *{plan_info['price']} تومان*\n\n"
            "لطفاً از طریق دکمه زیر پرداخت را انجام دهید و سپس نام و شماره تماس خود را وارد کنید:",
            reply_markup=InlineKeyboardMarkup([[pay_btn]]),
            parse_mode='Markdown'
        )
        
        await query.message.reply_text("لطفاً نام و نام خانوادگی خود را وارد کنید:")
        return WAITING_NAME
    
    elif payment_method == "pay_offline":
        # Manual bank transfer flow
        bank_info_text = (
            f"🏧 اطلاعات پرداخت کارت به کارت:\n\n"
            f"*{BANK_NAME}*\n"
            f"شماره کارت: `{BANK_ACCOUNT}`\n"
            f"نام صاحب حساب: {ACCOUNT_HOLDER}\n\n"
            f"مبلغ: *{plan_info['price']} تومان*\n\n"
            "پس از واریز، لطفاً عکس رسید پرداخت را اینجا ارسال کنید. 📸"
        )
        
        await query.edit_message_text(
            bank_info_text,
            parse_mode='Markdown'
        )
        return WAITING_RECEIPT
    
    return ConversationHandler.END


async def handle_receipt_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle receipt photo upload for manual payment"""
    user_id = update.effective_user.id
    plan_choice = context.user_data.get("plan")
    
    if not plan_choice:
        await update.message.reply_text("❌ خطا: پلن انتخاب نشده است. لطفاً از /start شروع کنید.")
        return ConversationHandler.END
    
    try:
        # Get the highest resolution photo
        photo = update.message.photo[-1]
        file = await photo.get_file()
        photo_bytes = await file.download_as_bytearray()
        
        # Upload to Supabase Storage
        timestamp = int(datetime.utcnow().timestamp())
        file_path = f"receipts/{user_id}_{timestamp}.jpg"
        
        # Upload image (using itcamptel bucket)
        supabase.storage.from_("itcamptel").upload(
            file_path,
            io.BytesIO(photo_bytes),
            file_options={"content-type": "image/jpeg", "cache-control": "3600"}
        )
        
        # Get public URL (get_public_url returns a string URL)
        receipt_url = supabase.storage.from_("itcamptel").get_public_url(file_path)
        
        # Store receipt URL temporarily
        context.user_data["receipt_url"] = receipt_url
        context.user_data["receipt_file_path"] = file_path
        
        await update.message.reply_text(
            "✅ رسید دریافت شد!\n\n"
            "لطفاً نام و نام خانوادگی خود را وارد کنید:"
        )
        return WAITING_NAME
        
    except Exception as e:
        logger.error(f"Error handling receipt photo: {e}")
        await update.message.reply_text(
            "❌ خطا در آپلود تصویر. لطفاً دوباره تلاش کنید."
        )
        return WAITING_RECEIPT


async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle user name input"""
    user_name = update.message.text.strip()
    
    if not user_name or len(user_name) < 2:
        await update.message.reply_text("❌ نام وارد شده معتبر نیست. لطفاً نام کامل خود را وارد کنید:")
        return WAITING_NAME
    
    context.user_data["name"] = user_name
    
    # Create contact sharing keyboard
    contact_keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton("📱 اشتراک‌گذاری شماره", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
    await update.message.reply_text(
        "شماره موبایل خود را هم ارسال کنید:",
        reply_markup=contact_keyboard
    )
    return WAITING_PHONE


async def handle_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle user phone input"""
    user_phone = None
    
    # Check if contact was shared
    if update.message.contact:
        user_phone = update.message.contact.phone_number
    else:
        user_phone = update.message.text.strip()
    
    # Basic validation (Iranian phone numbers)
    if not user_phone:
        await update.message.reply_text("❌ شماره تماس وارد نشده است. لطفاً شماره خود را وارد کنید:")
        return WAITING_PHONE
    
    # Remove non-digit characters for validation
    phone_digits = ''.join(filter(str.isdigit, user_phone))
    if len(phone_digits) < 10:
        await update.message.reply_text("❌ شماره تماس معتبر نیست. لطفاً شماره صحیح را وارد کنید:")
        return WAITING_PHONE
    
    context.user_data["phone"] = user_phone
    
    # Determine payment method and finish registration
    payment_method = "online" if "receipt_url" not in context.user_data else "offline"
    
    if payment_method == "online":
        return await finish_registration_online(update, context)
    else:
        return await finish_registration_offline(update, context)


async def finish_registration_online(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Complete online payment registration"""
    user_id = update.effective_user.id
    plan_choice = context.user_data.get("plan")
    user_name = context.user_data.get("name")
    user_phone = context.user_data.get("phone")
    
    try:
        # Insert user record
        plan_name_fa = PLANS[plan_choice]["name"]
        
        user_data = {
            "telegram_id": user_id,
            "name": user_name,
            "phone": user_phone,
            "plan": plan_name_fa,
            "payment_method": "online",
            "timestamp": datetime.utcnow().isoformat(),
            "status": "confirmed"
        }
        
        result = supabase.table("users").insert(user_data).execute()
        registration_id = result.data[0]["id"]
        
        # Generate tracking code
        tracking_code = f"W{registration_id:05d}"
        
        # Convert to Persian date
        persian_date = jdatetime.datetime.fromgregorian(
            datetime=datetime.utcnow(),
            locale=jdatetime.FA_LOCALE
        )
        date_str = persian_date.strftime("%d %B %Y - %H:%M")
        
        confirmation_text = (
            f"🎉 ثبت‌نام شما با موفقیت انجام شد!\n\n"
            f"*کد پیگیری:* `{tracking_code}`\n"
            f"*تاریخ ثبت‌نام:* {date_str}\n\n"
            f"منتظر پیام‌های بعدی ما باشید."
        )
        
        await update.message.reply_text(
            confirmation_text,
            parse_mode='Markdown',
            reply_markup=None  # Remove keyboard
        )
        
        # Start learning path
        await start_learning_path(update, context, user_id)
        
        # Clear user data
        context.user_data.clear()
        return ConversationHandler.END
        
    except Exception as e:
        logger.error(f"Error finishing online registration: {e}")
        await update.message.reply_text(
            "❌ خطا در ثبت اطلاعات. لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید."
        )
        return ConversationHandler.END


async def finish_registration_offline(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Complete offline payment registration and notify admins"""
    user_id = update.effective_user.id
    plan_choice = context.user_data.get("plan")
    user_name = context.user_data.get("name")
    user_phone = context.user_data.get("phone")
    receipt_url = context.user_data.get("receipt_url")
    
    try:
        plan_name_fa = PLANS[plan_choice]["name"]
        
        # Insert user record
        user_data = {
            "telegram_id": user_id,
            "name": user_name,
            "phone": user_phone,
            "plan": plan_name_fa,
            "payment_method": "offline",
            "timestamp": datetime.utcnow().isoformat(),
            "status": "pending"
        }
        
        user_result = supabase.table("users").insert(user_data).execute()
        new_user_id = user_result.data[0]["id"]
        
        # Insert receipt record
        receipt_data = {
            "user_id": new_user_id,
            "image_url": receipt_url,
            "status": "pending",
            "admin_id": None
        }
        
        supabase.table("receipts").insert(receipt_data).execute()
        
        # Notify all admins
        for admin_id in ADMIN_IDS:
            try:
                approve_btn = InlineKeyboardButton(
                    "✅ تأیید",
                    callback_data=f"approve_{new_user_id}"
                )
                reject_btn = InlineKeyboardButton(
                    "❌ رد کردن",
                    callback_data=f"reject_{new_user_id}"
                )
                
                admin_message = (
                    f"📥 *ثبت‌نام جدید*\n\n"
                    f"*نام:* {user_name}\n"
                    f"*تلفن:* {user_phone}\n"
                    f"*پلن:* {plan_name_fa}\n"
                    f"*کد کاربر:* {new_user_id}\n\n"
                    f"رسید واریزی در تصویر بالا منتظر تایید شماست."
                )
                
                await context.bot.send_photo(
                    chat_id=admin_id,
                    photo=receipt_url,
                    caption=admin_message,
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup([[approve_btn, reject_btn]])
                )
            except Exception as e:
                logger.error(f"Error notifying admin {admin_id}: {e}")
        
        # Confirm to user
        await update.message.reply_text(
            "✅ اطلاعات شما ثبت شد و در انتظار تأیید است.\n"
            "به محض تأیید توسط ادمین، پیام تایید برای شما ارسال خواهد شد.",
            reply_markup=None  # Remove keyboard
        )
        
        # Clear user data
        context.user_data.clear()
        return ConversationHandler.END
        
    except Exception as e:
        logger.error(f"Error finishing offline registration: {e}")
        await update.message.reply_text(
            "❌ خطا در ثبت اطلاعات. لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید."
        )
        return ConversationHandler.END


async def on_admin_decision(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle admin approve/reject callbacks"""
    query = update.callback_query
    admin_id = update.effective_user.id
    
    # Check admin authorization
    if admin_id not in ADMIN_IDS:
        await query.answer("❌ شما دسترسی به این عملیات را ندارید.", show_alert=True)
        return
    
    data = query.data
    action, user_id_str = data.split('_', 1)
    user_id = int(user_id_str)
    
    try:
        # Check if already processed
        user_record = supabase.table("users").select("status,telegram_id,name,plan").eq("id", user_id).execute()
        if not user_record.data:
            await query.answer("❌ کاربر یافت نشد.", show_alert=True)
            return
        
        current_status = user_record.data[0].get("status")
        if current_status in ["confirmed", "rejected"]:
            await query.answer(
                f"⚠️ این ثبت‌نام قبلاً {current_status} شده است.",
                show_alert=True
            )
            return
        
        user_telegram_id = user_record.data[0]["telegram_id"]
        user_name = user_record.data[0]["name"]
        user_plan = user_record.data[0]["plan"]
        
        if action == "approve":
            # Update user status
            supabase.table("users").update({
                "status": "confirmed"
            }).eq("id", user_id).execute()
            
            # Update receipt status
            supabase.table("receipts").update({
                "status": "approved",
                "admin_id": admin_id
            }).eq("user_id", user_id).execute()
            
            # Notify user
            tracking_code = f"W{user_id:05d}"
            persian_date = jdatetime.datetime.fromgregorian(
                datetime=datetime.utcnow(),
                locale=jdatetime.FA_LOCALE
            )
            date_str = persian_date.strftime("%d %B %Y - %H:%M")
            
            await context.bot.send_message(
                chat_id=user_telegram_id,
                text=(
                    f"✅ ثبت‌نام شما تأیید شد!\n\n"
                    f"*کد پیگیری:* `{tracking_code}`\n"
                    f"*تاریخ تأیید:* {date_str}\n\n"
                    f"منتظر پیام‌های بعدی ما باشید."
                ),
                parse_mode='Markdown'
            )
            
            # Start learning path
            await start_learning_path_for_user(context.bot, user_telegram_id)
            
            await query.answer("✅ تأیید شد")
            
        elif action == "reject":
            # Update user status
            supabase.table("users").update({
                "status": "rejected"
            }).eq("id", user_id).execute()
            
            # Update receipt status
            supabase.table("receipts").update({
                "status": "rejected",
                "admin_id": admin_id
            }).eq("user_id", user_id).execute()
            
            # Notify user
            await context.bot.send_message(
                chat_id=user_telegram_id,
                text=(
                    "❌ متأسفانه پرداخت شما تأیید نشد.\n\n"
                    "لطفاً با پشتیبانی تماس بگیرید یا دوباره تلاش کنید."
                )
            )
            
            await query.answer("❌ رد شد")
        
        # Update admin message
        admin_name = update.effective_user.first_name or "Admin"
        status_emoji = "✅" if action == "approve" else "❌"
        new_caption = (
            query.message.caption + 
            f"\n\n{status_emoji} {action.upper()} توسط {admin_name}"
        )
        
        await query.edit_message_caption(
            caption=new_caption,
            reply_markup=None  # Remove buttons
        )
        
    except Exception as e:
        logger.error(f"Error processing admin decision: {e}")
        await query.answer("❌ خطا در پردازش درخواست.", show_alert=True)


@restricted
async def submissions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Admin command to view registrations"""
    args = context.args
    
    try:
        query = supabase.table("users")
        
        if not args:
            # Default: show pending
            query = query.select("id,name,phone,plan,status,timestamp").eq("status", "pending").order("timestamp", desc=True)
            title = "📋 لیست ثبت‌نام‌های در انتظار تایید:\n\n"
        else:
            param = args[0].lower()
            if param in ["pending", "confirmed", "rejected"]:
                query = query.select("id,name,phone,plan,status,timestamp").eq("status", param).order("timestamp", desc=True)
                status_fa = {"pending": "در انتظار", "confirmed": "تأیید شده", "rejected": "رد شده"}[param]
                title = f"📋 لیست ثبت‌نام‌های {status_fa}:\n\n"
            else:
                # Search by keyword
                keyword = ' '.join(args)
                query = query.select("id,name,phone,plan,status,timestamp").ilike("name", f"%{keyword}%").order("timestamp", desc=True)
                title = f"🔍 نتایج جستجو برای \"{keyword}\":\n\n"
        
        result = query.execute()
        rows = result.data
        
        if not rows:
            await update.message.reply_text("موردی یافت نشد.")
            return
        
        text = title
        for r in rows:
            status_fa = {"pending": "⏳ در انتظار", "confirmed": "✅ تأیید شده", "rejected": "❌ رد شده"}.get(r.get("status", ""), r.get("status", ""))
            text += f"• {r['name']} ({r['phone']})\n  پلن: {r['plan']} | وضعیت: {status_fa} | کد: {r['id']}\n\n"
        
        # Telegram message limit is 4096 characters
        if len(text) > 4000:
            text = text[:4000] + "\n\n... (نتایج بیشتر حذف شد)"
        
        await update.message.reply_text(text)
        
    except Exception as e:
        logger.error(f"Error in submissions command: {e}")
        await update.message.reply_text("❌ خطا در دریافت اطلاعات.")


# ==================== LEARNING PATH FUNCTIONS ====================

def check_user_access(telegram_id: int) -> dict:
    """Check if user has confirmed registration"""
    try:
        result = supabase.table("users").select("id,status,plan").eq("telegram_id", telegram_id).execute()
        if result.data and result.data[0]["status"] == "confirmed":
            return result.data[0]
        return None
    except Exception as e:
        logger.error(f"Error checking user access: {e}")
        return None

def get_user_current_lesson(telegram_id: int) -> Optional[int]:
    """Get the next lesson number for user"""
    try:
        # Get completed lessons
        completed = supabase.table("user_progress").select("lesson_id").eq("telegram_id", telegram_id).eq("is_completed", True).execute()
        completed_ids = [r["lesson_id"] for r in completed.data] if completed.data else []
        
        # Get all lessons ordered by lesson_number
        all_lessons = supabase.table("lessons").select("id,lesson_number,is_free").order("lesson_number").execute()
        
        if not all_lessons.data:
            return None
        
        # Find first incomplete lesson
        for lesson in all_lessons.data:
            if lesson["id"] not in completed_ids:
                return lesson["lesson_number"]
        
        return None
    except Exception as e:
        logger.error(f"Error getting user current lesson: {e}")
        return None

def get_lesson_data(lesson_number: int):
    """Get lesson data from database"""
    try:
        result = supabase.table("lessons").select("*").eq("lesson_number", lesson_number).execute()
        if result.data:
            lesson = result.data[0]
            lesson["content"] = json.loads(lesson["content"])
            lesson["code_examples"] = json.loads(lesson.get("code_examples", "[]"))
            lesson["expected_outputs"] = json.loads(lesson.get("expected_outputs", "[]"))
            return lesson
        return None
    except Exception as e:
        logger.error(f"Error getting lesson data: {e}")
        return None

def get_lesson_questions(lesson_id: int):
    """Get questions for a lesson"""
    try:
        result = supabase.table("questions").select("*").eq("lesson_id", lesson_id).order("question_number").execute()
        return result.data if result.data else []
    except Exception as e:
        logger.error(f"Error getting lesson questions: {e}")
        return []

def mark_lesson_started(telegram_id: int, lesson_id: int):
    """Mark lesson as started"""
    try:
        supabase.table("user_progress").upsert({
            "telegram_id": telegram_id,
            "lesson_id": lesson_id,
            "started_at": datetime.utcnow().isoformat(),
            "is_completed": False
        }).execute()
    except Exception as e:
        logger.error(f"Error marking lesson started: {e}")

def mark_lesson_completed(telegram_id: int, lesson_id: int):
    """Mark lesson as completed"""
    try:
        supabase.table("user_progress").upsert({
            "telegram_id": telegram_id,
            "lesson_id": lesson_id,
            "completed_at": datetime.utcnow().isoformat(),
            "is_completed": True
        }).execute()
    except Exception as e:
        logger.error(f"Error marking lesson completed: {e}")

async def send_lesson_content(update_or_bot, chat_id: int, lesson_data: dict):
    """Send lesson content (can be multiple messages)"""
    contents = lesson_data.get("content", [])
    
    for i, content in enumerate(contents):
        if i == 0:
            # First message with title
            message = f"📚 *{lesson_data['title']}*\n\n{content}"
            if isinstance(update_or_bot, Update):
                await update_or_bot.message.reply_text(message, parse_mode='Markdown')
            else:
                await update_or_bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
        else:
            # Additional content
            if isinstance(update_or_bot, Update):
                await update_or_bot.message.reply_text(content, parse_mode='Markdown')
            else:
                await update_or_bot.send_message(chat_id=chat_id, text=content, parse_mode='Markdown')
    
    # Send code examples if any
    code_examples = lesson_data.get("code_examples", [])
    expected_outputs = lesson_data.get("expected_outputs", [])
    
    if code_examples:
        for i, code in enumerate(code_examples):
            code_msg = f"```python\n{code}\n```"
            if isinstance(update_or_bot, Update):
                await update_or_bot.message.reply_text(code_msg, parse_mode='Markdown')
            else:
                await update_or_bot.send_message(chat_id=chat_id, text=code_msg, parse_mode='Markdown')
            
            if i < len(expected_outputs):
                output_msg = f"**خروجی:**\n```\n{expected_outputs[i]}\n```"
                if isinstance(update_or_bot, Update):
                    await update_or_bot.message.reply_text(output_msg, parse_mode='Markdown')
                else:
                    await update_or_bot.send_message(chat_id=chat_id, text=output_msg, parse_mode='Markdown')

async def send_lesson(update_or_bot, chat_id: int, lesson_number: int):
    """Send a complete lesson to user"""
    lesson_data = get_lesson_data(lesson_number)
    if not lesson_data:
        error_msg = "❌ درس یافت نشد."
        if isinstance(update_or_bot, Update):
            await update_or_bot.message.reply_text(error_msg)
        else:
            await update_or_bot.send_message(chat_id=chat_id, text=error_msg)
        return
    
    # Check access for paid lessons
    if not lesson_data["is_free"]:
        user_access = check_user_access(chat_id)
        if not user_access:
            error_msg = (
                "🔒 این درس نیاز به ثبت‌نام دارد.\n\n"
                "برای دسترسی به درس‌های پیشرفته، لطفاً ثبت‌نام کنید:\n"
                "/start"
            )
            if isinstance(update_or_bot, Update):
                await update_or_bot.message.reply_text(error_msg)
            else:
                await update_or_bot.send_message(chat_id=chat_id, text=error_msg)
            return
    
    # Mark lesson as started
    mark_lesson_started(chat_id, lesson_data["id"])
    
    # Send lesson content
    await send_lesson_content(update_or_bot, chat_id, lesson_data)
    
    # Send questions
    questions = get_lesson_questions(lesson_data["id"])
    if questions:
        question_msg = "\n\n❓ **سوالات این درس:**\n\n"
        for i, q in enumerate(questions, 1):
            question_msg += f"*سوال {i}:* {q['question_text']}\n\n"
        
        question_msg += "برای پاسخ به سوالات از دستور /answer استفاده کنید."
        
        if isinstance(update_or_bot, Update):
            await update_or_bot.message.reply_text(question_msg, parse_mode='Markdown')
        else:
            await update_or_bot.send_message(chat_id=chat_id, text=question_msg, parse_mode='Markdown')
    
    # Mark lesson as completed
    mark_lesson_completed(chat_id, lesson_data["id"])

async def start_learning_path(update: Update, context: ContextTypes.DEFAULT_TYPE, telegram_id: int):
    """Start learning path for user after registration"""
    await start_learning_path_for_user(context.bot, telegram_id)

async def start_learning_path_for_user(bot, telegram_id: int):
    """Start learning path for a user (can be called from admin approval)"""
    welcome_msg = (
        "🎓 **به مسیر یادگیری پایتون خوش آمدید!**\n\n"
        "شما می‌توانید از درس‌های رایگان استفاده کنید.\n"
        "برای شروع، اولین درس را برای شما ارسال می‌کنم...\n\n"
        "دستورات مفید:\n"
        "/lessons - مشاهده لیست درس‌ها\n"
        "/next - درس بعدی\n"
        "/progress - پیشرفت شما"
    )
    
    await bot.send_message(chat_id=telegram_id, text=welcome_msg, parse_mode='Markdown')
    
    # Send first lesson
    await send_lesson(bot, telegram_id, 0)

async def lessons_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show list of lessons"""
    user_id = update.effective_user.id
    
    try:
        # Get all lessons
        result = supabase.table("lessons").select("lesson_number,title,is_free,section").order("lesson_number").execute()
        lessons = result.data if result.data else []
        
        # Get user progress
        progress_result = supabase.table("user_progress").select("lesson_id,is_completed").eq("telegram_id", user_id).execute()
        completed_lessons = {r["lesson_id"]: r["is_completed"] for r in progress_result.data} if progress_result.data else {}
        
        # Get lesson IDs
        lesson_ids = {l["lesson_number"]: None for l in lessons}
        for l in lessons:
            lesson_id_result = supabase.table("lessons").select("id").eq("lesson_number", l["lesson_number"]).execute()
            if lesson_id_result.data:
                lesson_ids[l["lesson_number"]] = lesson_id_result.data[0]["id"]
        
        message = "📚 *لیست درس‌ها:*\n\n"
        
        current_section = None
        for lesson in lessons:
            # Add section header
            if lesson["section"] != current_section:
                current_section = lesson["section"]
                section_names = {
                    "intro": "🎯 مقدمه",
                    "data_types": "📊 انواع داده‌ها",
                    "operators": "➕ عملگرها",
                    "functions": "🔧 توابع و شرط‌ها",
                    "data_structures": "📦 ساختارهای داده",
                    "methods_libraries": "📚 متدها و کتابخانه‌ها",
                    "ml_theory": "🤖 یادگیری ماشین"
                }
                message += f"\n{section_names.get(current_section, current_section)}\n"
            
            # Check if completed
            lesson_id = lesson_ids[lesson["lesson_number"]]
            status = ""
            if lesson_id and lesson_id in completed_lessons:
                if completed_lessons[lesson_id]:
                    status = " ✅"
            
            free_mark = "🆓" if lesson["is_free"] else "🔒"
            message += f"{free_mark} درس {lesson['lesson_number']}: {lesson['title']}{status}\n"
        
        message += "\n\nبرای شروع یک درس از /next استفاده کنید."
        
        await update.message.reply_text(message, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error in lessons command: {e}")
        await update.message.reply_text("❌ خطا در دریافت لیست درس‌ها.")

async def next_lesson_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send next lesson to user"""
    user_id = update.effective_user.id
    
    # Check access
    user_access = check_user_access(user_id)
    if not user_access:
        await update.message.reply_text(
            "❌ شما ثبت‌نام نکرده‌اید.\nبرای دسترسی به درس‌ها، لطفاً ثبت‌نام کنید:\n/start"
        )
        return
    
    # Get next lesson
    next_lesson_num = get_user_current_lesson(user_id)
    
    if next_lesson_num is None:
        await update.message.reply_text("🎉 تبریک! شما همه درس‌ها را تمام کرده‌اید!")
        return
    
    await send_lesson(update, user_id, next_lesson_num)

async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user progress"""
    user_id = update.effective_user.id
    
    try:
        # Get completed lessons count
        completed = supabase.table("user_progress").select("lesson_id").eq("telegram_id", user_id).eq("is_completed", True).execute()
        completed_count = len(completed.data) if completed.data else 0
        
        # Get total lessons count
        total = supabase.table("lessons").select("id", count="exact").execute()
        total_count = total.count if hasattr(total, 'count') else 0
        
        # Get free lessons count
        free_total = supabase.table("lessons").select("id", count="exact").eq("is_free", True).execute()
        free_count = free_total.count if hasattr(free_total, 'count') else 0
        
        message = (
            f"📊 *پیشرفت شما:*\n\n"
            f"✅ درس‌های تکمیل شده: {completed_count}\n"
            f"📚 کل درس‌ها: {total_count}\n"
            f"🆓 درس‌های رایگان: {free_count}\n\n"
        )
        
        if completed_count > 0:
            percentage = (completed_count / total_count * 100) if total_count > 0 else 0
            message += f"📈 پیشرفت: {percentage:.1f}%"
        
        await update.message.reply_text(message, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error in progress command: {e}")
        await update.message.reply_text("❌ خطا در دریافت پیشرفت.")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the conversation"""
    await update.message.reply_text(
        "❌ عملیات لغو شد. برای شروع مجدد از /start استفاده کنید.",
        reply_markup=None
    )
    context.user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Start the bot"""
    if not BOT_TOKEN or not SUPABASE_URL or not SUPABASE_KEY:
        logger.error("Missing required environment variables!")
        return
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Conversation handler for registration flow
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECTING_PLAN: [
                CallbackQueryHandler(on_plan_selected, pattern="^plan_")
            ],
            SELECTING_PAYMENT: [
                CallbackQueryHandler(on_payment_method, pattern="^pay_")
            ],
            WAITING_RECEIPT: [
                MessageHandler(filters.PHOTO, handle_receipt_photo),
                CommandHandler("cancel", cancel)
            ],
            WAITING_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name),
                CommandHandler("cancel", cancel)
            ],
            WAITING_PHONE: [
                MessageHandler(filters.TEXT | filters.CONTACT, handle_phone),
                CommandHandler("cancel", cancel)
            ],
        },
        fallbacks=[CommandHandler("start", start), CommandHandler("cancel", cancel)]
    )
    
    # Add handlers
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(on_admin_decision, pattern="^(approve|reject)_"))
    application.add_handler(CommandHandler("submissions", submissions, filters=filters.User(user_id=ADMIN_IDS)))
    
    # Learning path handlers
    application.add_handler(CommandHandler("lessons", lessons_command))
    application.add_handler(CommandHandler("next", next_lesson_command))
    application.add_handler(CommandHandler("progress", progress_command))
    
    # Start bot
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

