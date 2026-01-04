# -*- coding: utf-8 -*-
"""
Telegram Bot for Python Learning
15 lessons from basics to building a Telegram bot
All lessons are FREE - no payment required
"""

import os
import io
import json
import logging
import asyncio
from datetime import datetime, timezone
from functools import wraps
from typing import List, Optional

import jdatetime
from dotenv import load_dotenv
from supabase import create_client, Client
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Bot
from telegram.error import Conflict, TimedOut, NetworkError
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

# Import new lessons content
try:
    from lessons_content_new import get_all_lessons, get_lesson_by_number
except ImportError:
    # Fallback to old content if new doesn't exist
    from lessons_content import get_all_lessons, get_lesson_by_number

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()

# Validate environment variables
missing_vars = []
if not BOT_TOKEN:
    missing_vars.append("BOT_TOKEN")
if not SUPABASE_URL:
    missing_vars.append("SUPABASE_URL")
if not SUPABASE_KEY:
    missing_vars.append("SUPABASE_KEY")

if missing_vars:
    logger.error(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
    logger.error("Please set these variables in Railway dashboard:")
    for var in missing_vars:
        logger.error(f"  - {var}")
    if not BOT_TOKEN:
        logger.error("⚠️  Bot cannot start without BOT_TOKEN!")
        exit(1)

# Initialize Supabase client
supabase: Optional[Client] = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        logger.info("✅ Supabase client initialized successfully")
    except Exception as e:
        logger.error(f"❌ Error initializing Supabase client: {e}")
        logger.error("Bot will continue but database features will be disabled")
        supabase = None
else:
    logger.warning("⚠️  Supabase credentials not found, client not initialized")
    logger.warning("Bot will continue but database features will be disabled")

# Admin IDs
ADMIN_IDS_STR = os.environ.get("ADMIN_IDS", "")
ADMIN_IDS = [int(admin_id.strip()) for admin_id in ADMIN_IDS_STR.split(",") if admin_id.strip()]

# Total lessons: 15 (all free)
TOTAL_LESSONS = 15

# Conversation states
WAITING_NAME, WAITING_PHONE, WAITING_PYTHON_STATUS = range(3)
WAITING_EXAM_ANSWER = 10  # For answering exam questions

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
    if not supabase:
        logger.error("Supabase client not initialized")
        return None
    try:
        result = supabase.table("users").select("id,status").eq("telegram_id", telegram_id).execute()
        if result.data:
            return result.data[0]
        return None
    except Exception as e:
        logger.error(f"Error checking existing registration: {e}")
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle /start command"""
    try:
        user_id = update.effective_user.id
        username = update.effective_user.username or "Unknown"
        logger.info(f"Received /start from user {user_id} (@{username})")
        
        message = update.effective_message
        if not message:
            logger.error("No effective message found in update")
            return ConversationHandler.END
        
        # Check for existing registration
        existing = check_existing_registration(user_id)
        if existing:
            status = existing.get("status", "")
            if status == "confirmed":
                # User already registered, show lessons menu
                await show_lessons_menu(update, context)
                return ConversationHandler.END
        
        # Welcome message
        welcome_text = (
            "🎓 **به دوره آموزش پایتون خوش آمدید!**\n\n"
            "در این دوره شما یاد می‌گیرید:\n"
            "✅ مبانی پایتون\n"
            "✅ ساختارهای داده\n"
            "✅ برنامه‌نویسی پیشرفته\n"
            "✅ ساخت ربات تلگرام\n\n"
            "**همه درس‌ها رایگان هستند!** 🎉\n\n"
            "لطفاً نام خود را وارد کنید:"
        )
        
        await message.reply_text(welcome_text, parse_mode='Markdown')
        return WAITING_NAME
        
    except Exception as e:
        logger.error(f"Error in start: {e}", exc_info=True)
        if update.effective_message:
            await update.effective_message.reply_text("❌ خطایی رخ داد. لطفاً دوباره تلاش کنید.")
        return ConversationHandler.END

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle user name input"""
    try:
        name = update.message.text.strip()
        if len(name) < 2:
            await update.message.reply_text("❌ نام باید حداقل 2 کاراکتر باشد. لطفاً دوباره وارد کنید:")
            return WAITING_NAME
        
        context.user_data["name"] = name
        
        # Request phone number
        keyboard = [[KeyboardButton("📱 اشتراک‌گذاری شماره", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        
        await update.message.reply_text(
            f"خوب {name}! حالا لطفاً شماره موبایل خود را وارد کنید یا دکمه زیر را بزنید:",
            reply_markup=reply_markup
        )
        return WAITING_PHONE
        
    except Exception as e:
        logger.error(f"Error in handle_name: {e}")
        await update.message.reply_text("❌ خطایی رخ داد. لطفاً دوباره تلاش کنید.")
        return WAITING_NAME

async def handle_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle phone number input"""
    try:
        user_id = update.effective_user.id
        phone = None
        
        # Check if contact was shared
        if update.message.contact:
            phone = update.message.contact.phone_number
        else:
            phone = update.message.text.strip()
        
        if not phone or len(phone) < 10:
            await update.message.reply_text("❌ شماره موبایل معتبر نیست. لطفاً دوباره وارد کنید:")
            return WAITING_PHONE
        
        context.user_data["phone"] = phone
        
        # Complete registration
        await finish_registration(update, context)
        
        # Ask about Python installation
        keyboard = [
            [InlineKeyboardButton("✅ بله", callback_data="python_yes")],
            [InlineKeyboardButton("❌ خیر", callback_data="python_no")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🎯 **سوال مهم:**\n\n"
            "آیا پایتون روی کامپیوتر شما نصب است؟",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return WAITING_PYTHON_STATUS
        
    except Exception as e:
        logger.error(f"Error in handle_phone: {e}")
        await update.message.reply_text("❌ خطایی رخ داد. لطفاً دوباره تلاش کنید.")
        return WAITING_PHONE

async def finish_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Complete registration and save to database"""
    try:
        user_id = update.effective_user.id
        user_name = context.user_data.get("name")
        user_phone = context.user_data.get("phone")
        
        if not user_name or not user_phone:
            await update.message.reply_text("❌ اطلاعات ناقص است.")
            return
        
        if not supabase:
            await update.message.reply_text("⚠️ دیتابیس در دسترس نیست. لطفاً بعداً تلاش کنید.")
            return
        
        # Check if user exists
        existing = check_existing_registration(user_id)
        if existing:
            # Update existing user
            supabase.table("users").update({
                "name": user_name,
                "phone": user_phone,
                "plan": "رایگان",
                "payment_method": "none",
                "status": "confirmed"
            }).eq("telegram_id", user_id).execute()
        else:
            # Insert new user
            user_data = {
                "telegram_id": user_id,
                "name": user_name,
                "phone": user_phone,
                "plan": "رایگان",
                "payment_method": "none",
                "status": "confirmed"
            }
            supabase.table("users").insert(user_data).execute()
        
        logger.info(f"User {user_id} registered successfully")
        
    except Exception as e:
        logger.error(f"Error in finish_registration: {e}")
        raise

async def handle_python_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle Python installation status"""
    try:
        query = update.callback_query
        await query.answer()
        
        user_id = update.effective_user.id
        choice = query.data
        
        if choice == "python_yes":
            await query.edit_message_text(
                "✅ عالی! شما آماده شروع یادگیری هستید.\n\n"
                "از دستور /lessons برای مشاهده فهرست درس‌ها استفاده کنید."
            )
            # Start learning path
            await show_lessons_menu(update, context)
        else:
            await query.edit_message_text(
                "📦 **راهنمای نصب پایتون:**\n\n"
                "1. به سایت python.org بروید\n"
                "2. آخرین نسخه Python 3.11+ را دانلود کنید\n"
                "3. هنگام نصب، گزینه 'Add Python to PATH' را تیک بزنید\n"
                "4. بعد از نصب، از دستور /lessons استفاده کنید"
            )
        
        return ConversationHandler.END
        
    except Exception as e:
        logger.error(f"Error in handle_python_status: {e}")
        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel current operation"""
    await update.message.reply_text("❌ عملیات لغو شد.")
    context.user_data.clear()
    return ConversationHandler.END

def check_lesson_exam_passed(telegram_id: int, lesson_number: int) -> bool:
    """Check if user passed exam for a lesson"""
    # If no database, allow access to all lessons
    if not supabase:
        logger.info(f"⚠️  No database connection - allowing access to lesson {lesson_number}")
        return True
    
    try:
        # Get lesson ID
        lesson_result = supabase.table("lessons").select("id").eq("lesson_number", lesson_number).execute()
        if not lesson_result.data:
            logger.debug(f"Lesson {lesson_number} not found")
            return False
        
        lesson_id = lesson_result.data[0]["id"]
        
        # Check progress
        progress_result = supabase.table("user_progress").select("is_completed").eq("telegram_id", telegram_id).eq("lesson_id", lesson_id).execute()
        
        if not progress_result.data:
            logger.debug(f"No progress record for user {telegram_id}, lesson {lesson_number}")
            return False
        
        is_completed = progress_result.data[0].get("is_completed", False)
        logger.debug(f"User {telegram_id}, lesson {lesson_number}: is_completed = {is_completed}")
        return is_completed
        
    except Exception as e:
        logger.error(f"Error checking exam status: {e}")
        return False

async def show_lessons_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show lessons menu"""
    try:
        user_id = update.effective_user.id
        
        if not supabase:
            await update.effective_message.reply_text("⚠️ دیتابیس در دسترس نیست.")
            return
        
        # Get all lessons from database
        result = supabase.table("lessons").select("id,lesson_number,title,is_free").order("lesson_number").execute()
        
        if not result.data:
            await update.effective_message.reply_text(
                "⚠️ در حال حاضر درسی موجود نیست.\n"
                "لطفاً با ادمین تماس بگیرید."
            )
            return
        
        # Build keyboard
        keyboard = []
        buttons_per_row = 2
        
        for lesson in result.data:
            try:
                lesson_num = lesson["lesson_number"]
                title = lesson.get("title", "")
                
                # Determine status icon
                if lesson_num == 1:
                    status_icon = "🆓"  # First lesson is always free
                else:
                    # Check if previous lesson exam passed
                    prev_passed = check_lesson_exam_passed(user_id, lesson_num - 1)
                    if not prev_passed:
                        status_icon = "🔒"  # Locked
                    else:
                        status_icon = "🆓"  # All lessons are free now
                
                button_text = f"{status_icon} درس {lesson_num}"
                if title and len(title) > 15:
                    button_text += f": {title[:15]}..."
                elif title:
                    button_text += f": {title}"
                
                # Add button
                if len(keyboard) == 0 or len(keyboard[-1]) >= buttons_per_row:
                    keyboard.append([InlineKeyboardButton(button_text, callback_data=f"lesson_{lesson_num}")])
                else:
                    keyboard[-1].append(InlineKeyboardButton(button_text, callback_data=f"lesson_{lesson_num}"))
            except Exception as e:
                logger.error(f"Error processing lesson {lesson.get('lesson_number', 'unknown')}: {e}")
                continue
        
        # Add navigation buttons
        keyboard.append([InlineKeyboardButton("📊 پیشرفت من", callback_data="my_progress")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        menu_text = (
            f"📚 **فهرست درس‌ها** ({TOTAL_LESSONS} درس)\n\n"
            "🆓 همه درس‌ها رایگان هستند!\n"
            "🔒 درس‌های قفل شده نیاز به قبولی آزمون قبلی دارند.\n\n"
            "یک درس را انتخاب کنید:"
        )
        
        if hasattr(update, 'callback_query') and update.callback_query:
            await update.callback_query.edit_message_text(menu_text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            await update.effective_message.reply_text(menu_text, reply_markup=reply_markup, parse_mode='Markdown')
            
    except Exception as e:
        logger.error(f"Error in show_lessons_menu: {e}", exc_info=True)
        if update.effective_message:
            await update.effective_message.reply_text("❌ خطا در نمایش منوی درس‌ها.")

def get_lesson_data(lesson_number: int):
    """Get lesson data from database or fallback to local content"""
    # Try database first
    if supabase:
        try:
            result = supabase.table("lessons").select("*").eq("lesson_number", lesson_number).execute()
            if result.data and len(result.data) > 0:
                logger.info(f"✅ Lesson {lesson_number} loaded from database")
                return result.data[0]
        except Exception as e:
            logger.warning(f"⚠️  Error getting lesson {lesson_number} from database: {e}")
            logger.info(f"💡 Falling back to local lesson content...")
    
    # Fallback to local content
    try:
        lesson_data = get_lesson_by_number(lesson_number)
        if lesson_data:
            logger.info(f"✅ Lesson {lesson_number} loaded from local content")
            # Convert local format to database format
            # Note: content in lessons_content_new.py is already JSON string, so use it directly
            content_raw = lesson_data.get("content", "[]")
            if isinstance(content_raw, str):
                # Already JSON string, use as is
                content = content_raw
            else:
                # List, convert to JSON string
                content = json.dumps(content_raw, ensure_ascii=False)
            
            code_examples_raw = lesson_data.get("code_examples", "[]")
            if isinstance(code_examples_raw, str):
                code_examples = code_examples_raw
            else:
                code_examples = json.dumps(code_examples_raw, ensure_ascii=False)
            
            expected_outputs_raw = lesson_data.get("expected_outputs", "[]")
            if isinstance(expected_outputs_raw, str):
                expected_outputs = expected_outputs_raw
            else:
                expected_outputs = json.dumps(expected_outputs_raw, ensure_ascii=False)
            
            return {
                "id": lesson_number,
                "lesson_number": lesson_number,
                "title": lesson_data.get("title", f"درس {lesson_number}"),
                "content": content,
                "code_examples": code_examples,
                "expected_outputs": expected_outputs,
                "is_free": True
            }
    except Exception as e:
        logger.error(f"❌ Error getting lesson {lesson_number} from local content: {e}", exc_info=True)
    
    return None

async def send_lesson(update_or_bot, chat_id: int, lesson_number: int, context=None):
    """Send a complete lesson to user"""
    try:
        logger.info(f"Sending lesson {lesson_number} to user {chat_id}")
        
        lesson_data = get_lesson_data(lesson_number)
        if not lesson_data:
            error_msg = "❌ درس یافت نشد."
            bot = context.bot if hasattr(context, 'bot') and context else None
            if isinstance(update_or_bot, Update):
                await update_or_bot.message.reply_text(error_msg)
            elif bot:
                await bot.send_message(chat_id=chat_id, text=error_msg)
            elif hasattr(update_or_bot, 'send_message'):
                await update_or_bot.send_message(chat_id=chat_id, text=error_msg)
            else:
                logger.error("Cannot send error message - no bot instance available")
            return
        
        # Check if previous lesson exam is passed (except for first lesson)
        if lesson_number > 1:
            prev_passed = check_lesson_exam_passed(chat_id, lesson_number - 1)
            if not prev_passed:
                error_msg = (
                    f"🔒 **این درس قفل است!**\n\n"
                    f"برای دسترسی به درس {lesson_number}، باید آزمون درس {lesson_number - 1} را قبول کنید.\n\n"
                    f"از منوی درس‌ها، درس {lesson_number - 1} را انتخاب کنید و آزمون آن را بدهید."
                )
                bot = context.bot if hasattr(context, 'bot') and context else None
                if isinstance(update_or_bot, Update):
                    await update_or_bot.message.reply_text(error_msg, parse_mode='Markdown')
                elif bot:
                    await bot.send_message(chat_id=chat_id, text=error_msg, parse_mode='Markdown')
                elif hasattr(update_or_bot, 'send_message'):
                    await update_or_bot.send_message(chat_id=chat_id, text=error_msg, parse_mode='Markdown')
                else:
                    logger.error("Cannot send locked lesson message - no bot instance available")
                return
        
        # Parse content - handle both string and list formats
        content_raw = lesson_data.get("content", "[]")
        if isinstance(content_raw, str):
            try:
                content = json.loads(content_raw)
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing content JSON for lesson {lesson_number}: {e}")
                logger.error(f"Content: {content_raw[:200]}...")
                content = [content_raw] if content_raw else []
        else:
            content = content_raw if isinstance(content_raw, list) else []
        
        if not content:
            logger.warning(f"⚠️  No content found for lesson {lesson_number}")
            content = [f"درس {lesson_number} در حال آماده‌سازی است..."]
        
        title = lesson_data.get("title", f"درس {lesson_number}")
        
        # Send lesson content
        lesson_text = f"📚 **{title}**\n\n"
        
        for i, section in enumerate(content, 1):
            if i > 1:
                lesson_text += "\n" + "─" * 30 + "\n\n"
            lesson_text += section
        
        # Parse code examples - handle both string and list formats
        code_examples_raw = lesson_data.get("code_examples", "[]")
        if isinstance(code_examples_raw, str):
            try:
                code_examples = json.loads(code_examples_raw)
            except json.JSONDecodeError:
                logger.error(f"Error parsing code_examples JSON for lesson {lesson_number}")
                code_examples = []
        else:
            code_examples = code_examples_raw if isinstance(code_examples_raw, list) else []
        
        expected_outputs_raw = lesson_data.get("expected_outputs", "[]")
        if isinstance(expected_outputs_raw, str):
            try:
                expected_outputs = json.loads(expected_outputs_raw)
            except json.JSONDecodeError:
                logger.error(f"Error parsing expected_outputs JSON for lesson {lesson_number}")
                expected_outputs = []
        else:
            expected_outputs = expected_outputs_raw if isinstance(expected_outputs_raw, list) else []
        
        if code_examples:
            lesson_text += "\n\n" + "─" * 30 + "\n\n"
            lesson_text += "💻 **مثال‌های کد:**\n\n"
            for i, code in enumerate(code_examples, 1):
                lesson_text += f"```python\n{code}\n```\n\n"
                if i < len(expected_outputs):
                    lesson_text += f"**خروجی:**\n```\n{expected_outputs[i-1]}\n```\n\n"
        
        # Navigation buttons
        keyboard = []
        if lesson_number > 1:
            keyboard.append([InlineKeyboardButton("⬅️ درس قبلی", callback_data=f"lesson_{lesson_number - 1}")])
        
        if lesson_number < TOTAL_LESSONS:
            keyboard.append([InlineKeyboardButton("➡️ درس بعدی", callback_data=f"lesson_{lesson_number + 1}")])
        
        keyboard.append([
            InlineKeyboardButton("📚 منوی درس‌ها", callback_data="lessons_menu"),
            InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")
        ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send lesson - always send as new message, never edit
        sent_message = None
        bot = context.bot if hasattr(context, 'bot') and context else None
        
        if isinstance(update_or_bot, Update):
            sent_message = await update_or_bot.message.reply_text(lesson_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif bot:
            # Use bot from context to send new message
            sent_message = await bot.send_message(chat_id=chat_id, text=lesson_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif hasattr(update_or_bot, 'send_message'):
            # update_or_bot is a Bot instance
            sent_message = await update_or_bot.send_message(chat_id=chat_id, text=lesson_text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            logger.error(f"Cannot send lesson - no valid bot instance available")
            return
        
        # Store lesson message ID for later reference
        if sent_message and hasattr(sent_message, 'message_id'):
            if isinstance(update_or_bot, Update) and update_or_bot.message:
                context = update_or_bot.message._bot._application._context if hasattr(update_or_bot.message, '_bot') else None
            elif hasattr(update_or_bot, 'context'):
                context = update_or_bot.context
            else:
                context = None
            
            if context:
                context.user_data["lesson_message_id"] = sent_message.message_id
        
        # Don't auto-start exam - let user click a button to start exam
        exam_keyboard = [[InlineKeyboardButton("📝 شروع آزمون", callback_data=f"start_exam_{lesson_number}")]]
        exam_reply_markup = InlineKeyboardMarkup(exam_keyboard)
        
        exam_prompt = f"✅ درس {lesson_number} ارسال شد!\n\n📝 برای شروع آزمون، دکمه زیر را بزنید:"
        
        # Always send as new message, never edit
        bot = context.bot if hasattr(context, 'bot') else None
        if isinstance(update_or_bot, Update):
            await update_or_bot.message.reply_text(exam_prompt, reply_markup=exam_reply_markup)
        elif bot:
            await bot.send_message(chat_id=chat_id, text=exam_prompt, reply_markup=exam_reply_markup)
        elif hasattr(update_or_bot, 'send_message'):
            await update_or_bot.send_message(chat_id=chat_id, text=exam_prompt, reply_markup=exam_reply_markup)
        else:
            # Fallback: try to send new message instead of edit
            if bot:
                await bot.send_message(chat_id=chat_id, text=exam_prompt, reply_markup=exam_reply_markup)
            else:
                logger.error("Cannot send exam prompt - no bot instance available")
        
    except Exception as e:
        logger.error(f"Error sending lesson {lesson_number}: {e}", exc_info=True)
        error_msg = f"❌ خطا در ارسال درس.\n\nخطا: {str(e)[:100]}"
        bot = context.bot if hasattr(context, 'bot') and context else None
        if isinstance(update_or_bot, Update):
            await update_or_bot.message.reply_text(error_msg)
        elif bot:
            await bot.send_message(chat_id=chat_id, text=error_msg)
        elif hasattr(update_or_bot, 'send_message'):
            await update_or_bot.send_message(chat_id=chat_id, text=error_msg)
        else:
            logger.error("Cannot send error message - no bot instance available")

async def start_lesson_exam(update_or_bot, chat_id: int, lesson_id: int, lesson_number: int, context=None):
    """Start exam for a lesson"""
    try:
        # Get questions from database
        result = supabase.table("questions").select("*").eq("lesson_id", lesson_id).order("question_number").execute()
        
        if not result.data:
            logger.warning(f"No questions found for lesson {lesson_number}")
            error_msg = "❌ سوالی برای این درس یافت نشد."
            bot = context.bot if hasattr(context, 'bot') and context else None
            if bot:
                await bot.send_message(chat_id=chat_id, text=error_msg)
            elif hasattr(update_or_bot, 'send_message'):
                await update_or_bot.send_message(chat_id=chat_id, text=error_msg)
            else:
                logger.error("Cannot send error message - no bot instance available")
            return
        
        questions = result.data
        
        # Get context
        if context is None:
            if hasattr(update_or_bot, 'context') and update_or_bot.context:
                context = update_or_bot.context
            elif isinstance(update_or_bot, Update):
                # Try to get context from update
                if hasattr(update_or_bot, '_bot') and hasattr(update_or_bot._bot, '_application'):
                    context = update_or_bot._bot._application._context
                else:
                    logger.error("Cannot get context for exam")
                    return
            else:
                logger.error("Cannot get context for exam")
                return
        
        # Store exam data in context
        context.user_data["exam_questions"] = questions
        context.user_data["exam_current_question"] = 0
        context.user_data["exam_lesson_id"] = lesson_id
        context.user_data["exam_lesson_number"] = lesson_number
        context.user_data["exam_answers"] = []
        context.user_data["exam_shown_answers"] = set()
        context.user_data["waiting_exam_answer"] = True
        
        # Send first question
        await send_exam_question(update_or_bot, chat_id, context, 0)
        
    except Exception as e:
        logger.error(f"Error starting exam: {e}", exc_info=True)
        error_msg = f"❌ خطا در شروع آزمون: {str(e)[:100]}"
        bot = context.bot if hasattr(context, 'bot') and context else None
        if bot:
            await bot.send_message(chat_id=chat_id, text=error_msg)
        elif hasattr(update_or_bot, 'send_message'):
            await update_or_bot.send_message(chat_id=chat_id, text=error_msg)
        else:
            logger.error("Cannot send error message - no bot instance available")

async def send_exam_question(update_or_bot, chat_id: int, context, question_index: int):
    """Send an exam question"""
    try:
        questions = context.user_data.get("exam_questions", [])
        if question_index >= len(questions):
            return
        
        question = questions[question_index]
        lesson_number = context.user_data.get("exam_lesson_number", "?")
        question_text = f"📝 *آزمون درس {lesson_number}*\n\n❓ *سوال {question_index + 1} از {len(questions)}:*\n\n{question['question_text']}"
        
        keyboard = []
        
        # Parse options if multiple choice
        if question.get("question_type") == "multiple_choice" and question.get("options"):
            options = json.loads(question["options"])
            for i, option in enumerate(options):
                keyboard.append([InlineKeyboardButton(option, callback_data=f"exam_answer_{question_index}_{i}")])
        
        # Add show answer button
        keyboard.append([InlineKeyboardButton("💡 نمایش جواب", callback_data=f"exam_show_answer_{question_index}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Always send as new message, don't edit previous message
        # Get bot instance from context
        bot = context.bot if hasattr(context, 'bot') else None
        
        if isinstance(update_or_bot, Update):
            await update_or_bot.message.reply_text(question_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif bot:
            # Use bot.send_message to send new message
            await bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif hasattr(update_or_bot, 'send_message'):
            await update_or_bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif hasattr(update_or_bot, 'message') and hasattr(update_or_bot.message, 'reply_text'):
            await update_or_bot.message.reply_text(question_text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            logger.error("Cannot send exam question - no bot instance available")
            
    except Exception as e:
        logger.error(f"Error sending exam question: {e}", exc_info=True)

async def handle_exam_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle exam answer"""
    try:
        user_id = update.effective_user.id
        
        # Check if in exam mode
        if not context.user_data.get("waiting_exam_answer", False):
            return
        
        user_answer = update.message.text.strip() if update.message and update.message.text else None
        if not user_answer:
            return
        
        current_question = context.user_data.get("exam_current_question", 0)
        questions = context.user_data.get("exam_questions", [])
        
        if current_question >= len(questions):
            return
        
        question = questions[current_question]
        correct_answer = question.get("correct_answer", "").strip().lower()
        user_answer_lower = user_answer.strip().lower()
        
        is_correct = user_answer_lower == correct_answer
        
        # Store answer
        context.user_data["exam_answers"].append({
            "question_id": question["id"],
            "user_answer": user_answer,
            "is_correct": is_correct
        })
        
        if is_correct:
            await update.message.reply_text("✅ صحیح! سوال بعدی...")
            context.user_data["exam_current_question"] += 1
            
            if context.user_data["exam_current_question"] < len(questions):
                await send_exam_question(update, user_id, context, context.user_data["exam_current_question"])
            else:
                await finish_exam(update, context)
        else:
            await update.message.reply_text("❌ اشتباه است. لطفاً دوباره تلاش کنید.")
            
    except Exception as e:
        logger.error(f"Error handling exam answer: {e}", exc_info=True)

async def handle_exam_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle exam answer from callback (multiple choice)"""
    try:
        query = update.callback_query
        await query.answer()
        
        # Handle start exam button
        if query.data.startswith("start_exam_"):
            lesson_number = int(query.data.split("_")[-1])
            lesson_data = get_lesson_data(lesson_number)
            if not lesson_data:
                await query.edit_message_text("❌ درس یافت نشد.")
                return
            
            # Start exam - pass context explicitly
            # Answer callback first
            await query.answer("⏳ در حال شروع آزمون...")
            # Send new message instead of editing
            bot = context.bot
            await bot.send_message(chat_id=query.from_user.id, text="⏳ در حال شروع آزمون...")
            await start_lesson_exam(bot, query.from_user.id, lesson_data["id"], lesson_number, context)
            return
        
        # Check if showing answer
        if query.data.startswith("exam_show_answer_"):
            question_index = int(query.data.split("_")[-1])
            questions = context.user_data.get("exam_questions", [])
            if question_index < len(questions):
                question = questions[question_index]
                correct_answer = question.get("correct_answer", "")
                explanation = question.get("explanation", "")
                
                answer_text = f"💡 **جواب صحیح:** {correct_answer}"
                if explanation:
                    answer_text += f"\n\n📝 **توضیح:** {explanation}"
                
                # Mark as shown (doesn't count in score)
                context.user_data["exam_shown_answers"].add(question_index)
                
                # Add next button
                keyboard = [[InlineKeyboardButton("➡️ سوال بعدی", callback_data=f"exam_next_{question_index}")]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await query.edit_message_text(answer_text, reply_markup=reply_markup, parse_mode='Markdown')
            return
        
        # Handle next after showing answer
        if query.data.startswith("exam_next_"):
            question_index = int(query.data.split("_")[-1])
            context.user_data["exam_current_question"] = question_index + 1
            
            await query.answer()
            questions = context.user_data.get("exam_questions", [])
            bot = context.bot if hasattr(context, 'bot') else None
            if context.user_data["exam_current_question"] < len(questions):
                if bot:
                    await send_exam_question(bot, query.from_user.id, context, context.user_data["exam_current_question"])
                else:
                    await send_exam_question(query, query.from_user.id, context, context.user_data["exam_current_question"])
            else:
                await finish_exam(query, context)
            return
        
        # Handle answer selection
        if query.data.startswith("exam_answer_"):
            parts = query.data.split("_")
            question_index = int(parts[2])
            option_index = int(parts[3])
            
            questions = context.user_data.get("exam_questions", [])
            if question_index >= len(questions):
                return
            
            question = questions[question_index]
            options = json.loads(question.get("options", "[]"))
            user_answer = options[option_index]
            correct_answer = question.get("correct_answer", "").strip()
            
            is_correct = user_answer.strip() == correct_answer.strip()
            
            # Store answer
            context.user_data["exam_answers"].append({
                "question_id": question["id"],
                "user_answer": user_answer,
                "is_correct": is_correct
            })
            
            # Update current question index
            context.user_data["exam_current_question"] = question_index + 1
            
            # Send feedback as new message
            bot = context.bot if hasattr(context, 'bot') else None
            if bot:
                if is_correct:
                    await bot.send_message(chat_id=query.from_user.id, text="✅ صحیح!")
                else:
                    await bot.send_message(chat_id=query.from_user.id, text=f"❌ اشتباه! جواب صحیح: {correct_answer}")
            
            # Edit the question message to remove buttons
            try:
                await query.edit_message_text(query.message.text + "\n\n✅ پاسخ ثبت شد")
            except Exception as e:
                logger.warning(f"Could not edit message: {e}")
            
            # Send next question or finish exam
            if context.user_data["exam_current_question"] < len(questions):
                await asyncio.sleep(1)
                # Send next question as new message
                if bot:
                    await send_exam_question(bot, query.from_user.id, context, context.user_data["exam_current_question"])
                else:
                    await send_exam_question(query, query.from_user.id, context, context.user_data["exam_current_question"])
            else:
                await finish_exam(query, context)
                
    except Exception as e:
        logger.error(f"Error handling exam callback: {e}", exc_info=True)

async def finish_exam(update_or_bot, context):
    """Finish exam and show results"""
    try:
        user_id = update_or_bot.from_user.id if hasattr(update_or_bot, 'from_user') else update_or_bot.effective_user.id
        questions = context.user_data.get("exam_questions", [])
        answers = context.user_data.get("exam_answers", [])
        shown_answers = context.user_data.get("exam_shown_answers", set())
        lesson_id = context.user_data.get("exam_lesson_id")
        lesson_number = context.user_data.get("exam_lesson_number")
        
        # Calculate score (excluding shown answers)
        total_questions = len(questions)
        answered_questions = len([a for i, a in enumerate(answers) if i not in shown_answers])
        correct_answers = len([a for i, a in enumerate(answers) if a.get("is_correct") and i not in shown_answers])
        
        if answered_questions == 0:
            score_percent = 0
        else:
            score_percent = int((correct_answers / answered_questions) * 100)
        
        # Save answers to database
        if supabase:
            try:
                for answer in answers:
                    supabase.table("question_answers").upsert({
                        "telegram_id": user_id,
                        "question_id": answer["question_id"],
                        "user_answer": answer["user_answer"],
                        "is_correct": answer["is_correct"]
                    }, on_conflict="telegram_id,question_id").execute()
            except Exception as e:
                logger.error(f"Error saving answers: {e}")
        
        # Check if passed (70%)
        passed = score_percent >= 70
        
        # Update progress
        if supabase and passed:
            try:
                supabase.table("user_progress").upsert({
                    "telegram_id": user_id,
                    "lesson_id": lesson_id,
                    "is_completed": True,
                    "completed_at": datetime.now(timezone.utc).isoformat()
                }, on_conflict="telegram_id,lesson_id").execute()
            except Exception as e:
                logger.error(f"Error updating progress: {e}")
        
        # Prepare result message
        result_text = (
            f"📊 **نتایج آزمون درس {lesson_number}**\n\n"
            f"✅ پاسخ‌های صحیح: {correct_answers} از {answered_questions}\n"
            f"📈 نمره: {score_percent}%\n\n"
        )
        
        if passed:
            result_text += "🎉 **تبریک! شما قبول شدید!**\n\n"
            if lesson_number < TOTAL_LESSONS:
                result_text += f"درس بعدی ({lesson_number + 1}) خودکار ارسال می‌شود..."
        else:
            result_text += "❌ متأسفانه قبول نشدید.\n\nنمره قبولی: 70%\n\nلطفاً درس را دوباره مطالعه کنید."
        
        # Navigation buttons
        keyboard = []
        if passed and lesson_number < TOTAL_LESSONS:
            keyboard.append([InlineKeyboardButton("➡️ درس بعدی", callback_data=f"lesson_{lesson_number + 1}")])
        else:
            keyboard.append([InlineKeyboardButton("🔄 آزمون مجدد", callback_data=f"lesson_{lesson_number}")])
        
        keyboard.append([
            InlineKeyboardButton("📚 منوی درس‌ها", callback_data="lessons_menu"),
            InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")
        ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send result - always send as new message
        bot = context.bot if hasattr(context, 'bot') and context else None
        if isinstance(update_or_bot, Update):
            await update_or_bot.message.reply_text(result_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif bot:
            await bot.send_message(chat_id=user_id, text=result_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif hasattr(update_or_bot, 'send_message'):
            await update_or_bot.send_message(chat_id=user_id, text=result_text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            logger.error("Cannot send exam result - no bot instance available")
        
        # Auto-send next lesson if passed
        if passed and lesson_number < TOTAL_LESSONS:
            await asyncio.sleep(2)
            await send_lesson(update_or_bot, user_id, lesson_number + 1, context)
        
        # Clear exam data
        context.user_data.pop("exam_questions", None)
        context.user_data.pop("exam_current_question", None)
        context.user_data.pop("exam_answers", None)
        context.user_data.pop("waiting_exam_answer", None)
        context.user_data.pop("exam_shown_answers", None)
        
    except Exception as e:
        logger.error(f"Error finishing exam: {e}", exc_info=True)

async def handle_lesson_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle lesson selection from menu"""
    try:
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        
        # Handle menu callbacks
        if query.data == "lessons_menu":
            await show_lessons_menu(update, context)
            return
        elif query.data == "main_menu":
            await start(update, context)
            return
        
        # Extract lesson number
        if not query.data.startswith("lesson_"):
            return
        
        lesson_number = int(query.data.split("_")[1])
        
        # Check if lesson exists
        lesson_data = get_lesson_data(lesson_number)
        if not lesson_data:
            await query.answer("❌ درس یافت نشد.", show_alert=True)
            await context.bot.send_message(chat_id=user_id, text="❌ درس یافت نشد.")
            return
        
        # Send lesson - pass context to send_lesson
        # Don't edit the menu message, send lesson as new message
        await query.answer("⏳ در حال بارگذاری درس...")
        bot = context.bot
        await bot.send_message(chat_id=user_id, text="⏳ در حال بارگذاری درس...")
        await send_lesson(bot, user_id, lesson_number, context)
        
    except Exception as e:
        logger.error(f"Error handling lesson selection: {e}", exc_info=True)
        bot = context.bot if hasattr(context, 'bot') and context else None
        error_msg = "❌ خطا در بارگذاری درس."
        if bot:
            await bot.send_message(chat_id=user_id, text=error_msg)
        elif update.callback_query:
            await update.callback_query.answer("❌ خطا در بارگذاری درس.", show_alert=True)

async def lessons_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /lessons command"""
    # Check registration
    user_id = update.effective_user.id
    existing = check_existing_registration(user_id)
    if not existing or existing.get("status") != "confirmed":
        await update.message.reply_text(
            "⚠️ برای استفاده از درس‌ها باید ابتدا ثبت‌نام کنید.\n"
            "از دستور /start استفاده کنید."
        )
        return
    
    await show_lessons_menu(update, context)

async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /progress command"""
    try:
        user_id = update.effective_user.id
        
        if not supabase:
            await update.message.reply_text("⚠️ دیتابیس در دسترس نیست.")
            return
        
        # Get user progress
        progress_result = supabase.table("user_progress").select("lesson_id,is_completed").eq("telegram_id", user_id).eq("is_completed", True).execute()
        
        completed_count = len(progress_result.data) if progress_result.data else 0
        
        progress_text = (
            f"📊 **پیشرفت شما:**\n\n"
            f"✅ درس‌های تکمیل شده: {completed_count} از {TOTAL_LESSONS}\n"
            f"📈 درصد پیشرفت: {int((completed_count / TOTAL_LESSONS) * 100)}%\n\n"
            f"از دستور /lessons برای مشاهده فهرست درس‌ها استفاده کنید."
        )
        
        await update.message.reply_text(progress_text, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error in progress_command: {e}")
        await update.message.reply_text("❌ خطا در نمایش پیشرفت.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    error = context.error
    logger.error(f"Exception while handling an update: {error}")
    
    # Handle Conflict errors gracefully (multiple instances)
    if isinstance(error, Conflict):
        logger.warning("⚠️  Conflict detected - another bot instance may be running")
        logger.warning("💡 This is usually temporary and will resolve automatically")
        return  # Don't send error message to user for conflicts
    
    # Handle network errors gracefully
    if isinstance(error, (NetworkError, TimedOut)):
        logger.warning(f"⚠️  Network error: {error}")
        logger.warning("💡 Retrying automatically...")
        return
    
    # Log full traceback for other errors
    if error:
        import traceback
        logger.error(traceback.format_exc())
    
    # Send error message to user for other errors
    if update and update.effective_message:
        try:
            await update.effective_message.reply_text("❌ متأسفانه خطایی رخ داد. لطفاً دوباره تلاش کنید.")
        except:
            pass

async def test_bot_connection(token: str, max_retries: int = 3) -> bool:
    """Test bot connection to Telegram API"""
    for attempt in range(max_retries):
        try:
            logger.info(f"Testing connection to Telegram API (attempt {attempt + 1}/{max_retries})...")
            bot = Bot(token=token)
            await bot.initialize()
            me = await bot.get_me()
            await bot.shutdown()
            logger.info(f"✅ Connection successful! Bot: @{me.username}")
            return True
        except Exception as e:
            error_msg = str(e)
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                logger.warning(f"⚠️  Connection failed (attempt {attempt + 1}/{max_retries}): {error_msg[:100]}")
                logger.info(f"⏳ Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                logger.error(f"❌ Failed to connect after {max_retries} attempts")
                logger.error(f"Error: {error_msg}")
                return False
    return False

def main() -> None:
    """Start the bot"""
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN not found in environment variables!")
        logger.error("Please check your .env file and ensure BOT_TOKEN is set.")
        return
    
    logger.info("=" * 60)
    logger.info("🤖 Starting Telegram Bot...")
    logger.info("=" * 60)
    
    # Test connection first
    try:
        connection_ok = asyncio.run(test_bot_connection(BOT_TOKEN))
        if not connection_ok:
            logger.error("\n" + "=" * 60)
            logger.error("❌ Cannot connect to Telegram API!")
            logger.error("=" * 60)
            logger.error("\n💡 Troubleshooting:")
            logger.error("   1. Check your internet connection")
            logger.error("   2. Verify BOT_TOKEN is correct in .env file")
            logger.error("   3. If in Iran, use VPN/proxy to access Telegram")
            logger.error("   4. Check firewall/proxy settings")
            logger.error("   5. Try accessing https://api.telegram.org in browser")
            logger.error("\n⚠️  Bot will not start without connection.")
            return
    except Exception as e:
        logger.error(f"❌ Error testing connection: {e}")
        return
    
    try:
        logger.info("📱 Creating bot application...")
        application = Application.builder().token(BOT_TOKEN).build()
        logger.info("✅ Application created successfully")
    except Exception as e:
        logger.error(f"❌ Error creating application: {e}")
        return
    
    # Conversation handler for registration
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            WAITING_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name),
                CommandHandler("cancel", cancel)
            ],
            WAITING_PHONE: [
                MessageHandler(filters.CONTACT, handle_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_phone),
                CommandHandler("cancel", cancel)
            ],
            WAITING_PYTHON_STATUS: [
                CallbackQueryHandler(handle_python_status, pattern="^python_"),
                CommandHandler("cancel", cancel)
            ],
        },
        fallbacks=[CommandHandler("start", start), CommandHandler("cancel", cancel)],
        per_chat=True,
        per_user=True
    )
    
    # Add handlers
    logger.info("📝 Registering handlers...")
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("lessons", lessons_command))
    application.add_handler(CommandHandler("progress", progress_command))
    application.add_handler(CallbackQueryHandler(handle_lesson_selection, pattern="^lesson_"))
    application.add_handler(CallbackQueryHandler(handle_lesson_selection, pattern="^lessons_menu"))
    application.add_handler(CallbackQueryHandler(handle_lesson_selection, pattern="^main_menu"))
    application.add_handler(CallbackQueryHandler(handle_exam_answer_callback, pattern="^(exam_|start_exam_)"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_exam_answer))
    application.add_error_handler(error_handler)
    
    logger.info("✅ All handlers registered")
    logger.info("=" * 60)
    logger.info("🚀 Bot is ready! Starting polling...")
    logger.info("=" * 60)
    
    # run_polling automatically deletes webhook when drop_pending_updates=True
    try:
        application.run_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True,
            close_loop=False
        )
    except KeyboardInterrupt:
        logger.info("\n⚠️  Bot stopped by user")
    except Conflict as e:
        logger.error(f"❌ Conflict error: {e}")
        logger.error("💡 Make sure only one bot instance is running!")
        logger.error("   - Check Railway for duplicate deployments")
        logger.error("   - Stop any local instances")
        logger.error("   - Wait a few seconds and restart")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == '__main__':
    main()

