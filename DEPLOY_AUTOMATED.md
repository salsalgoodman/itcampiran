# 🤖 استقرار خودکار با Render CLI

## دو روش برای استقرار

### روش 1: Render CLI (خودکار) ⭐

#### مرحله 1: نصب Render CLI

**Windows (PowerShell):**
```powershell
# Option 1: با npm (اگر Node.js نصب دارید)
npm install -g @render/cli

# Option 2: با Chocolatey (اگر Chocolatey نصب دارید)
choco install render-cli

# Option 3: اجرای اسکریپت
.\setup_render_cli.ps1
```

**بررسی نصب:**
```bash
render --version
```

#### مرحله 2: لاگین به Render

```bash
render login
```

این دستور یک مرورگر باز می‌کند برای احراز هویت.

#### مرحله 3: استقرار خودکار

```bash
python auto_deploy.py
```

این اسکریپت:
- ✅ کد را به GitHub push می‌کند
- ✅ به Render deploy می‌کند
- ✅ همه چیز را خودکار انجام می‌دهد

---

### روش 2: Render Dashboard (ساده‌تر) ⭐⭐

اگر Render CLI کار نکرد، از Dashboard استفاده کنید:

1. **برو به:** https://dashboard.render.com
2. **New +** → **Background Worker**
3. **Connect GitHub** → Repository خود را انتخاب کن
4. تنظیمات را وارد کن
5. Environment Variables را اضافه کن
6. **Deploy!**

---

## 🚀 استفاده از اسکریپت خودکار

### گام 1: آماده‌سازی

```bash
# بررسی وضعیت
python prepare_deployment.py
```

### گام 2: Push به GitHub

```bash
# اگر Repository در GitHub ایجاد کردی:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### گام 3: استقرار

**Option A: با اسکریپت خودکار**
```bash
python auto_deploy.py
```

**Option B: با Render CLI دستی**
```bash
render login
render deploy
```

**Option C: با Dashboard**
- برو به https://dashboard.render.com
- New + → Background Worker
- Connect GitHub

---

## 📋 چک‌لیست

### قبل از استقرار:
- [ ] Git initialized
- [ ] کد commit شده
- [ ] Repository در GitHub ایجاد شده
- [ ] Remote به GitHub اضافه شده

### برای Render CLI:
- [ ] Render CLI نصب شده (`render --version`)
- [ ] به Render لاگین شده (`render login`)

### برای Dashboard:
- [ ] حساب Render ایجاد شده
- [ ] GitHub به Render متصل شده

---

## 🔧 عیب‌یابی

### Render CLI پیدا نمی‌شود؟
```bash
# نصب مجدد
npm install -g @render/cli

# یا
choco install render-cli
```

### GitHub Authentication مشکل دارد؟
- از GitHub Personal Access Token استفاده کن
- یا از SSH keys استفاده کن

### Render CLI login مشکل دارد؟
- مرورگر را دستی باز کن
- به https://dashboard.render.com برو
- از Dashboard استفاده کن (ساده‌تر است)

---

## 💡 توصیه

**برای شروع:** از **Render Dashboard** استفاده کن (ساده‌تر و بدون نیاز به CLI)

**برای استقرارهای بعدی:** از **Render CLI** استفاده کن (سریع‌تر)

---

## 🎯 مراحل سریع

```bash
# 1. نصب Render CLI
npm install -g @render/cli

# 2. لاگین
render login

# 3. استقرار خودکار
python auto_deploy.py
```

یا ساده‌تر:

1. برو به https://dashboard.render.com
2. New + → Background Worker
3. Connect GitHub
4. Deploy!

---

**موفق باشی! 🚀**

