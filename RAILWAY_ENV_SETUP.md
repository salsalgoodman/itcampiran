# 🔧 راهنمای تنظیم متغیرهای محیطی در Railway

## ❌ مشکل فعلی:

```
supabase._sync.client.SupabaseException: supabase_url is required
```

این خطا به این معنی است که متغیرهای محیطی در Railway تنظیم نشده‌اند.

---

## ✅ راه‌حل: تنظیم Environment Variables در Railway

### مرحله 1: ورود به Railway Dashboard

1. به [Railway Dashboard](https://railway.app) بروید
2. پروژه خود را انتخاب کنید
3. روی سرویس (Service) خود کلیک کنید

### مرحله 2: تنظیم Variables

1. در صفحه سرویس، به تب **Variables** بروید
2. روی **New Variable** کلیک کنید
3. متغیرهای زیر را اضافه کنید:

#### متغیرهای ضروری:

```
BOT_TOKEN=7967637047:AAFA0MXwYkHRzVqivdn7PiKAZLM771wL7sQ
```

```
SUPABASE_URL=https://npzffoovhbmikjwrzdhw.supabase.co
```

```
SUPABASE_KEY=your_supabase_anon_key_here
```

#### متغیرهای اختیاری:

```
ADMIN_IDS=5813277691
```

---

### مرحله 3: دریافت Supabase Key

1. به [Supabase Dashboard](https://app.supabase.com) بروید
2. پروژه خود را انتخاب کنید
3. به **Settings** → **API** بروید
4. **anon/public** key را کپی کنید
5. در Railway، آن را به عنوان `SUPABASE_KEY` اضافه کنید

---

### مرحله 4: Redeploy

بعد از اضافه کردن متغیرها:

1. Railway به صورت خودکار redeploy می‌کند
2. یا می‌توانید دستی **Redeploy** را بزنید

---

## 📋 چک‌لیست متغیرها:

- [ ] `BOT_TOKEN` - توکن بات تلگرام
- [ ] `SUPABASE_URL` - آدرس Supabase
- [ ] `SUPABASE_KEY` - کلید Supabase (anon key)
- [ ] `ADMIN_IDS` - شناسه‌های ادمین (اختیاری)

---

## 🔍 بررسی متغیرها:

بعد از تنظیم، در Railway Logs باید ببینید:

```
✅ Supabase client initialized successfully
```

اگر خطا دیدید:

```
❌ Missing required environment variables: SUPABASE_URL, SUPABASE_KEY
```

یعنی متغیرها درست تنظیم نشده‌اند.

---

## 💡 نکات مهم:

1. **هیچ فاصله اضافی** در مقادیر متغیرها نباشد
2. **مقادیر را درون کوتیشن** قرار ندهید (Railway خودش مدیریت می‌کند)
3. بعد از تغییر متغیرها، **Redeploy** کنید

---

## 🆘 اگر مشکل حل نشد:

1. Logs را در Railway بررسی کنید
2. مطمئن شوید که همه متغیرها اضافه شده‌اند
3. Redeploy کنید
4. اگر هنوز مشکل دارید، متغیرها را دوباره چک کنید

---

**بعد از تنظیم متغیرها، بات باید بدون مشکل کار کند! 🚀**

