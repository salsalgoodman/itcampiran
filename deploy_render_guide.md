# Deploy to Render.com (100% FREE) - Step by Step

## 🎯 Render.com - Completely Free Forever!

Render offers **free background workers** - perfect for your Telegram bot!

## 📋 Step-by-Step Guide

### Step 1: Prepare Your Code

Make sure you have these files:
- ✅ `workshop_signup_bot.py` (main bot)
- ✅ `requirements.txt` (dependencies)
- ✅ `Procfile` (tells Render how to run)

**All files are ready!** ✅

### Step 2: Push to GitHub

If you haven't already:

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Workshop registration bot"

# Create repo on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 3: Deploy on Render

1. **Go to Render.com**
   - Visit: https://render.com
   - Click "Get Started for Free"
   - Sign up with GitHub (easiest)

2. **Create Background Worker**
   - Click "New +" button
   - Select "Background Worker"

3. **Connect Repository**
   - Select "Connect GitHub"
   - Choose your repository
   - Click "Connect"

4. **Configure Settings**
   - **Name:** `workshop-bot` (or any name)
   - **Region:** Choose closest to you
   - **Branch:** `main` (or `master`)
   - **Root Directory:** Leave empty (or `./`)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python workshop_signup_bot.py`

5. **Add Environment Variables**
   Click "Advanced" → "Add Environment Variable" and add:
   
   ```
   BOT_TOKEN=7967637047:AAFA0MXwYkHRzVqivdn7PiKAZLM771wL7sQ
   SUPABASE_URL=https://npzffoovhbmikjwrzdhw.supabase.co
   SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5wemZmb292aGJtaWtqd3J6ZGh3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ1Mzc3MDYsImV4cCI6MjA4MDExMzcwNn0.RV8pVrHspveFIjlk-gFZei0vC3qA445xBCvwi_Qwf84
   ADMIN_IDS=581327769
   ZARINPAL_URL_ECONOMY=https://www.zarinpal.com/pg/StartPay/ECONOMY_DEMO_LINK
   ZARINPAL_URL_STANDARD=https://www.zarinpal.com/pg/StartPay/STANDARD_DEMO_LINK
   ZARINPAL_URL_PROFESSIONAL=https://www.zarinpal.com/pg/StartPay/PRO_DEMO_LINK
   BANK_NAME=بانک ملت
   BANK_ACCOUNT=XXXX-XXXX-XXXX-XXXX
   ACCOUNT_HOLDER=نام صاحب حساب
   ```

6. **Deploy!**
   - Click "Create Background Worker"
   - Wait for deployment (2-5 minutes)
   - Check logs to see if bot started

### Step 4: Verify Bot is Running

1. Check Render dashboard - should show "Live"
2. Check logs - should show "Bot started!"
3. Test bot in Telegram - send `/start`

## ✅ Done! Bot Runs 24/7 for FREE!

## ⚠️ Important Notes

### Free Tier Limitations:
- **Spins down after 15 min inactivity**
- **Wakes up automatically** when bot receives message
- **May take 10-30 seconds** to wake up (cold start)
- **Still FREE forever!**

### If You Need Instant Response:
- Upgrade to "Starter" plan ($7/month)
- No cold starts
- Always running

## 🔧 Troubleshooting

### Bot not responding?
- Check Render logs
- Verify environment variables are set
- Check if worker is "Live" (not "Stopped")

### Cold start delay?
- Normal on free tier
- Upgrade to paid for instant response
- Or keep bot active (send periodic messages)

### Build fails?
- Check `requirements.txt` is correct
- Verify Python version compatibility
- Check build logs for errors

## 📊 Monitoring

- **View Logs:** Render dashboard → Your service → Logs
- **View Metrics:** Render dashboard → Metrics
- **Restart:** Render dashboard → Manual Deploy

## 🎉 Success!

Your bot now runs 24/7 in the cloud for FREE!

You can:
- ✅ Turn off your PC
- ✅ Put PC to sleep
- ✅ Bot keeps running
- ✅ All for FREE!

## 💡 Pro Tip

To prevent cold starts, you can:
1. Set up a cron job to ping your bot every 10 minutes
2. Or upgrade to paid plan ($7/month)
3. Or use Railway ($5/month) for always-on

But free tier works great for most use cases!

