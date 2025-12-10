# Telegram Bot for Workshop Registration

یک ربات تلگرام برای ثبت‌نام در ورکشاپ با قابلیت پرداخت آنلاین و کارت به کارت

## ویژگی‌ها

- ✅ انتخاب از بین 3 پلن قیمت‌گذاری (اقتصادی، استاندارد، حرفه‌ای)
- 💳 پرداخت آنلاین از طریق زرین‌پال
- 🏧 پرداخت کارت به کارت با آپلود رسید
- 👥 سیستم تأیید ادمین برای پرداخت‌های کارت به کارت
- 📋 دستور `/submissions` برای مشاهده ثبت‌نام‌ها (فقط ادمین)
- 🔒 جلوگیری از ثبت‌نام تکراری
- 📸 ذخیره‌سازی تصاویر رسید در Supabase Storage
- 🇮🇷 رابط کاربری کاملاً فارسی

## نیازمندی‌ها

- Python 3.9 یا بالاتر
- حساب Supabase
- ربات تلگرام (از @BotFather)

## نصب و راه‌اندازی

### 1. نصب پکیج‌ها

```bash
pip install -r requirements.txt
```

### 2. تنظیم متغیرهای محیطی

یک فایل `.env` در ریشه پروژه ایجاد کنید و مقادیر زیر را تنظیم کنید:

```env
# Telegram Bot Configuration
BOT_TOKEN=your_telegram_bot_token_here

# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key

# Admin Telegram User IDs (comma-separated)
ADMIN_IDS=11111111,22222222,33333333,44444444,55555555

# Zarinpal Payment URLs (for each plan)
ZARINPAL_URL_ECONOMY=https://www.zarinpal.com/pg/StartPay/ECONOMY_DEMO_LINK
ZARINPAL_URL_STANDARD=https://www.zarinpal.com/pg/StartPay/STANDARD_DEMO_LINK
ZARINPAL_URL_PROFESSIONAL=https://www.zarinpal.com/pg/StartPay/PRO_DEMO_LINK

# Bank Account Information (for manual transfers)
BANK_NAME=بانک ملت
BANK_ACCOUNT=XXXX-XXXX-XXXX-XXXX
ACCOUNT_HOLDER=نام صاحب حساب
```

### 3. راه‌اندازی Supabase

#### ایجاد جداول

در Supabase SQL Editor، دستورات زیر را اجرا کنید:

```sql
-- جدول users
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    plan TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    status TEXT NOT NULL DEFAULT 'pending'
);

-- جدول receipts
CREATE TABLE receipts (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    admin_id BIGINT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ایندکس برای جستجوی سریع‌تر
CREATE INDEX idx_users_telegram_id ON users(telegram_id);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_receipts_user_id ON receipts(user_id);
CREATE INDEX idx_receipts_status ON receipts(status);
```

#### ایجاد Storage Bucket

1. به بخش Storage در داشبورد Supabase بروید
2. یک bucket جدید با نام `itcamptel` ایجاد کنید
3. تنظیمات bucket را به صورت Public تنظیم کنید (برای دسترسی به تصاویر)

#### تنظیم Row Level Security (اختیاری)

اگر می‌خواهید امنیت بیشتری داشته باشید، می‌توانید RLS را فعال کنید و policy مناسب اضافه کنید. برای این ربات، استفاده از service role key یا تنظیم policy برای insert/select توصیه می‌شود.

### 4. اجرای ربات

```bash
python workshop_signup_bot.py
```

## ساختار پایگاه داده

### جدول users

| فیلد | نوع | توضیحات |
|------|-----|---------|
| id | BIGSERIAL | شناسه یکتا |
| telegram_id | BIGINT | شناسه تلگرام کاربر |
| name | TEXT | نام و نام خانوادگی |
| phone | TEXT | شماره تماس |
| plan | TEXT | پلن انتخاب شده (اقتصادی/استاندارد/حرفه‌ای) |
| payment_method | TEXT | روش پرداخت (online/offline) |
| timestamp | TIMESTAMPTZ | زمان ثبت‌نام |
| status | TEXT | وضعیت (pending/confirmed/rejected) |

### جدول receipts

| فیلد | نوع | توضیحات |
|------|-----|---------|
| id | BIGSERIAL | شناسه یکتا |
| user_id | BIGINT | شناسه کاربر (FK) |
| image_url | TEXT | آدرس تصویر رسید |
| status | TEXT | وضعیت (pending/approved/rejected) |
| admin_id | BIGINT | شناسه ادمین تأییدکننده |
| created_at | TIMESTAMPTZ | زمان ایجاد |

## استفاده

### برای کاربران

1. ربات را با `/start` شروع کنید
2. یکی از پلن‌ها را انتخاب کنید
3. روش پرداخت را انتخاب کنید:
   - **پرداخت آنلاین**: لینک زرین‌پال را باز کنید و پرداخت کنید، سپس نام و شماره تماس را وارد کنید
   - **کارت به کارت**: اطلاعات حساب را دریافت کنید، واریز کنید، عکس رسید را ارسال کنید، سپس نام و شماره تماس را وارد کنید

### برای ادمین‌ها

- **مشاهده ثبت‌نام‌ها**: `/submissions` - نمایش ثبت‌نام‌های در انتظار
- **فیلتر بر اساس وضعیت**: `/submissions confirmed` یا `/submissions rejected`
- **جستجو**: `/submissions نام کاربر`
- **تأیید/رد پرداخت**: با کلیک روی دکمه‌های تأیید/رد در پیام‌های اعلان

## امنیت

- دسترسی به دستورات ادمین فقط برای کاربران تعریف شده در `ADMIN_IDS`
- بررسی مجوز ادمین در تمام عملیات حساس
- جلوگیری از ثبت‌نام تکراری بر اساس `telegram_id`
- ذخیره‌سازی ایمن اطلاعات حساس در `.env`

## عیب‌یابی

### خطای اتصال به Supabase
- بررسی صحت `SUPABASE_URL` و `SUPABASE_KEY`
- اطمینان از دسترسی به اینترنت

### خطای آپلود تصویر
- بررسی وجود bucket با نام `itcamptel` در Supabase
- اطمینان از public بودن bucket

### ربات پاسخ نمی‌دهد
- بررسی صحت `BOT_TOKEN`
- بررسی لاگ‌ها برای خطاهای احتمالی

## مجوز

این پروژه برای استفاده شخصی و تجاری آزاد است.

## پشتیبانی

در صورت بروز مشکل، لطفاً issue ایجاد کنید یا با تیم پشتیبانی تماس بگیرید.

