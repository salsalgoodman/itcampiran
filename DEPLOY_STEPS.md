# 🚀 مراحل استقرار در Render.com (رایگان)

## ✅ وضعیت فعلی
- Git initialized ✅
- همه فایل‌ها آماده ✅
- Procfile موجود ✅
- requirements.txt موجود ✅

---

## 📝 مراحل استقرار

### مرحله 1: Commit کردن کد

```bash
git commit -m "Workshop registration bot ready for deployment"
```

### مرحله 2: ایجاد Repository در GitHub

1. به https://github.com/new بروید
2. نام Repository را وارد کنید (مثلاً: `workshop-telegram-bot`)
3. **Public** یا **Private** انتخاب کنید
4. روی **"Create repository"** کلیک کنید
5. **DO NOT** initialize with README (کد شما آماده است)

### مرحله 3: اتصال به GitHub

```bash
# جای YOUR_USERNAME و YOUR_REPO را با اطلاعات خود جایگزین کنید
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### مرحله 4: استقرار در Render.com

#### 4.1. ثبت‌نام
- برو به https://render.com
- با GitHub ثبت‌نام کن

#### 4.2. ایجاد Background Worker
1. **New +** → **Background Worker**
2. **Connect GitHub** → Repository خود را انتخاب کن
3. تنظیمات:
   ```
   Name: workshop-bot
   Region: (نزدیک‌ترین به شما)
   Branch: main
   Build Command: pip install -r requirements.txt
   Start Command: python workshop_signup_bot.py
   ```

#### 4.3. Environment Variables

در بخش **Environment Variables** این متغیرها را اضافه کن:

```
BOT_TOKEN=7967637047:AAFA0MXwYkHRzVqivdn7PiKAZLM771wL7sQ
SUPABASE_URL=https://npzffoovhbmikjwrzdhw.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5wemZmb292aGJtaWtqd3J6ZGh3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ1Mzc3MDYsImV4cCI6MjA4MDExMzcwNn0.RV8pVrHspveFIjlk-gFZei0vC3qA445xBCvwi_Qwf84
ADMIN_IDS=581327769
ZARINPAL_URL=https://zarinp.al/itcampiran.ir
ZARINPAL_URL_ECONOMY=https://zarinp.al/itcampiran.ir
ZARINPAL_URL_STANDARD=https://zarinp.al/itcampiran.ir
ZARINPAL_URL_PROFESSIONAL=https://zarinp.al/itcampiran.ir
BANK_NAME=بانک ملت
BANK_ACCOUNT=XXXX-XXXX-XXXX-XXXX
ACCOUNT_HOLDER=نام صاحب حساب
```

**⚠️ مهم:** مقادیر واقعی خود را وارد کن!

#### 4.4. Deploy
- روی **"Create Background Worker"** کلیک کن
- منتظر بمان (2-5 دقیقه)
- لاگ‌ها را بررسی کن

---

## ✅ بررسی

1. در Render Dashboard → باید **"Live"** نشان دهد
2. در Telegram → `/start` را بفرست → باید پاسخ دهد

---

## 💡 نکات

- نسخه رایگان بعد از 15 دقیقه خاموش می‌شود
- با دریافت پیام خودکار بیدار می‌شود
- برای همیشه روشن: پلن Starter ($7/ماه)

---

## 🆘 مشکل داری؟

- لاگ‌های Render را بررسی کن
- Environment Variables را دوباره چک کن
- مطمئن شو همه فایل‌ها در GitHub هستند

---

**موفق باشی! 🎉**

