# 🚀 راهنمای استقرار ربات در Render.com

## ✅ وضعیت فعلی
- ✅ Git initialized
- ✅ کد commit شده
- ✅ همه فایل‌های لازم آماده است

---

## 📋 مراحل بعدی (5 دقیقه)

### مرحله 1: ایجاد Repository در GitHub

1. به https://github.com/new بروید
2. نام Repository را وارد کنید (مثلاً: `workshop-telegram-bot`)
3. **Public** یا **Private** انتخاب کنید
4. **⚠️ مهم:** تیک "Add a README file" را نزنید (کد شما آماده است)
5. روی **"Create repository"** کلیک کنید

### مرحله 2: اتصال و Push به GitHub

بعد از ایجاد Repository، GitHub دستورات زیر را نشان می‌دهد. این دستورات را در ترمینال اجرا کنید:

```bash
# جای YOUR_USERNAME و YOUR_REPO را با اطلاعات خود جایگزین کنید
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

**مثال:**
```bash
git remote add origin https://github.com/samern/workshop-telegram-bot.git
git branch -M main
git push -u origin main
```

### مرحله 3: استقرار در Render.com

#### 3.1. ثبت‌نام
1. به https://render.com بروید
2. روی **"Get Started for Free"** کلیک کنید
3. با **GitHub** ثبت‌نام کنید (ساده‌ترین روش)

#### 3.2. ایجاد Background Worker
1. در داشبورد Render، روی **"New +"** کلیک کنید
2. **"Background Worker"** را انتخاب کنید

#### 3.3. اتصال Repository
1. **"Connect GitHub"** را انتخاب کنید
2. Repository خود را انتخاب کنید
3. روی **"Connect"** کلیک کنید

#### 3.4. تنظیمات

این تنظیمات را وارد کنید:

- **Name:** `workshop-bot` (یا هر نام دیگری)
- **Region:** نزدیک‌ترین منطقه به شما (مثلاً: Singapore, Frankfurt)
- **Branch:** `main`
- **Root Directory:** خالی بگذارید
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python workshop_signup_bot.py`

#### 3.5. Environment Variables (خیلی مهم!)

روی **"Advanced"** کلیک کنید و سپس **"Add Environment Variable"** و این متغیرها را یکی یکی اضافه کنید:

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

**⚠️ مهم:** 
- مقادیر بالا را با اطلاعات واقعی خود از فایل `.env` جایگزین کنید!
- هر متغیر را جداگانه اضافه کنید (Copy/Paste هر خط)

#### 3.6. Deploy
1. روی **"Create Background Worker"** کلیک کنید
2. منتظر بمانید (2-5 دقیقه)
3. لاگ‌ها را بررسی کنید

---

## ✅ بررسی موفقیت

### در Render Dashboard:
- باید **"Live"** نشان دهد (سبز)
- در بخش **Logs** باید این پیام را ببینید:
  ```
  Bot started!
  ```

### در Telegram:
1. ربات خود را باز کنید
2. دستور `/start` را بفرستید
3. باید پاسخ ربات را دریافت کنید!

---

## ⚠️ نکات مهم

### نسخه رایگان Render:
- ✅ **کاملاً رایگان برای همیشه**
- ⏰ بعد از 15 دقیقه عدم فعالیت خاموش می‌شود
- 🔄 با دریافت پیام خودکار بیدار می‌شود
- ⏱️ ممکن است 10-30 ثانیه طول بکشد تا بیدار شود (cold start)

### اگر نیاز به پاسخ فوری دارید:
- ارتقا به پلن **"Starter"** ($7/ماه)
- بدون cold start
- همیشه در حال اجرا

---

## 🔧 عیب‌یابی

### ربات پاسخ نمی‌دهد؟
1. ✅ لاگ‌های Render را بررسی کنید (Dashboard → Logs)
2. ✅ Environment Variables را دوباره بررسی کنید
3. ✅ مطمئن شوید Worker **"Live"** است (نه "Stopped")

### Build ناموفق؟
1. ✅ بررسی کنید `requirements.txt` درست است
2. ✅ لاگ‌های Build را برای خطاها بررسی کنید

### Cold Start (تأخیر در پاسخ)؟
- این طبیعی است در نسخه رایگان
- برای پاسخ فوری، به نسخه پولی ارتقا دهید

---

## 📊 مانیتورینگ

- **مشاهده لاگ‌ها:** Render Dashboard → سرویس شما → Logs
- **مشاهده متریک‌ها:** Render Dashboard → Metrics
- **راه‌اندازی مجدد:** Render Dashboard → Manual Deploy

---

## 🎉 موفقیت!

ربات شما اکنون 24/7 در ابر به صورت رایگان اجرا می‌شود!

می‌توانید:
- ✅ کامپیوتر خود را خاموش کنید
- ✅ کامپیوتر را به حالت Sleep ببرید
- ✅ ربات همچنان اجرا می‌شود
- ✅ همه اینها رایگان است!

---

## 📝 چک‌لیست نهایی

- [ ] Repository در GitHub ایجاد شد
- [ ] کد به GitHub push شد
- [ ] حساب Render ایجاد شد
- [ ] Background Worker ایجاد شد
- [ ] Environment Variables اضافه شد
- [ ] Deployment موفق بود
- [ ] ربات در Telegram پاسخ می‌دهد

---

## 🆘 کمک بیشتر

اگر مشکلی داشتید:
1. لاگ‌های Render را بررسی کنید
2. Environment Variables را دوباره بررسی کنید
3. مطمئن شوید همه فایل‌ها در GitHub هستند

---

**موفق باشید! 🚀**

