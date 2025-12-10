# 🚀 استقرار سریع در Render.com

## مراحل سریع (5 دقیقه)

### 1️⃣ آماده‌سازی Git

```bash
git init
git add .
git commit -m "Workshop bot ready"
```

### 2️⃣ ایجاد Repository در GitHub

1. برو به https://github.com/new
2. نام Repository را وارد کن
3. Create repository را بزن
4. دستورات زیر را اجرا کن:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 3️⃣ استقرار در Render

1. برو به https://render.com
2. Sign up با GitHub
3. New + → Background Worker
4. Connect GitHub → Repository خود را انتخاب کن
5. تنظیمات:
   - **Name:** `workshop-bot`
   - **Build:** `pip install -r requirements.txt`
   - **Start:** `python workshop_signup_bot.py`
6. Environment Variables را اضافه کن (از فایل `.env` خودت)
7. Create Background Worker

### 4️⃣ Environment Variables در Render

این متغیرها را اضافه کن:

```
BOT_TOKEN=توکن_ربات_تلگرام
SUPABASE_URL=آدرس_سوپابیس
SUPABASE_KEY=کلید_سوپابیس
ADMIN_IDS=آیدی_ادمین
ZARINPAL_URL=https://zarinp.al/itcampiran.ir
ZARINPAL_URL_ECONOMY=https://zarinp.al/itcampiran.ir
ZARINPAL_URL_STANDARD=https://zarinp.al/itcampiran.ir
ZARINPAL_URL_PROFESSIONAL=https://zarinp.al/itcampiran.ir
BANK_NAME=بانک ملت
BANK_ACCOUNT=شماره_حساب
ACCOUNT_HOLDER=نام_صاحب_حساب
```

### ✅ تمام!

ربات شما اکنون در Render اجرا می‌شود و کاملاً رایگان است!

---

## ⚠️ نکته مهم

نسخه رایگان Render بعد از 15 دقیقه عدم فعالیت خاموش می‌شود، اما به طور خودکار با دریافت پیام بیدار می‌شود.

برای همیشه روشن بودن، می‌توانی به پلن Starter ($7/ماه) ارتقا دهی.

