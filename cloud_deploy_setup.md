# Cloud Deployment - Keep Bot Running 24/7

## ⚠️ Important: Local PC vs Cloud

**If you turn off your PC:**
- ❌ Bot stops running
- ❌ Users can't register
- ❌ Bot is offline

**Solution: Deploy to Cloud**
- ✅ Bot runs 24/7
- ✅ Works even when PC is off
- ✅ Always available

## 🚀 Quick Cloud Deployment Options

### Option 1: Railway (Easiest - Recommended)

**Steps:**
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Connect your repository (or create one)
6. Railway auto-detects Python
7. Add environment variables:
   - `BOT_TOKEN`
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `ADMIN_IDS`
   - (all other .env variables)
8. Deploy!

**Cost:** Free tier available, then ~$5/month

### Option 2: Render (Free Tier Available)

**Steps:**
1. Go to https://render.com
2. Sign up
3. Create new "Background Worker"
4. Connect GitHub repo
5. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python workshop_signup_bot.py`
6. Add environment variables from .env
7. Deploy!

**Cost:** Free tier available (spins down after inactivity, but wakes on request)

### Option 3: Fly.io (Good Free Tier)

**Steps:**
1. Install Fly CLI: `iwr https://fly.io/install.ps1 -useb | iex`
2. Login: `fly auth login`
3. Create app: `fly launch`
4. Add secrets: `fly secrets set BOT_TOKEN=... SUPABASE_URL=...`
5. Deploy: `fly deploy`

**Cost:** Free tier available

### Option 4: DigitalOcean App Platform

**Steps:**
1. Go to https://cloud.digitalocean.com
2. Create App
3. Connect GitHub
4. Configure as Worker
5. Add environment variables
6. Deploy

**Cost:** ~$5/month

## 📋 Prepare for Deployment

### 1. Create Procfile (for Heroku/Railway)

Create `Procfile`:
```
worker: python workshop_signup_bot.py
```

### 2. Create runtime.txt (optional)

Create `runtime.txt`:
```
python-3.11
```

### 3. Create .gitignore (already done)

Make sure `.env` is in `.gitignore` (already done)

### 4. Environment Variables Needed

You'll need to add these in cloud platform:
- `BOT_TOKEN`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `ADMIN_IDS`
- `ZARINPAL_URL_ECONOMY`
- `ZARINPAL_URL_STANDARD`
- `ZARINPAL_URL_PROFESSIONAL`
- `BANK_NAME`
- `BANK_ACCOUNT`
- `ACCOUNT_HOLDER`

## 🎯 Recommended: Railway (Easiest)

Railway is the easiest option:

1. **Create GitHub Repo** (if you haven't):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   # Push to GitHub
   ```

2. **Deploy on Railway**:
   - Go to railway.app
   - New Project → Deploy from GitHub
   - Select your repo
   - Add environment variables
   - Deploy!

3. **Done!** Bot runs 24/7

## 💡 Alternative: Keep PC On

If you don't want cloud deployment:
- Keep your PC on 24/7
- Use PM2 to auto-restart on crashes
- Set Windows to never sleep
- Use a dedicated old PC/laptop

## 🔧 Quick Setup Script for Railway

I'll create a script to help you prepare for Railway deployment.

