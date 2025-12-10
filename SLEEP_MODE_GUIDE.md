# Sleep Mode vs Bot Running

## ⚠️ What Happens in Sleep Mode?

**If your PC goes to sleep:**
- ❌ Bot stops running
- ❌ Bot can't receive messages
- ❌ Users can't register
- ❌ Bot appears offline

**Sleep mode = Bot stops** (same as turning off PC)

## 🔧 Solutions

### Option 1: Prevent Sleep (Temporary Solution)

**Windows Settings:**
1. Open Settings → System → Power & Sleep
2. Set "When plugged in, PC goes to sleep after: **Never**"
3. Set "Screen turns off after: **Your preference**"

**Or use Command Prompt (Admin):**
```bash
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0
```

**⚠️ Note:** This keeps PC running 24/7, uses electricity, and PC must stay on.

### Option 2: Cloud Deployment (Best Solution) ✅

Deploy bot to cloud - then you can:
- ✅ Put PC to sleep anytime
- ✅ Turn off PC anytime
- ✅ Bot runs 24/7 in cloud
- ✅ No electricity cost on your PC

**Recommended:** Railway.app or Render.com

### Option 3: Keep PC Awake (Not Recommended)

- Keep PC on 24/7
- Prevent sleep mode
- Uses electricity
- PC must stay on

## 💡 Best Practice

**For Development/Testing:**
- Keep PC awake while testing
- Use sleep mode when not testing

**For Production:**
- Deploy to cloud (Railway/Render)
- Then you can sleep/turn off PC anytime
- Bot runs independently in cloud

## 🚀 Quick Cloud Deploy

See `cloud_deploy_setup.md` for deployment steps.

**Railway.app** - Easiest option:
1. Sign up with GitHub
2. Deploy from GitHub repo
3. Add environment variables
4. Done! Bot runs 24/7

## Summary

| Situation | Bot Status |
|-----------|------------|
| PC Sleep | ❌ Bot Stops |
| PC Off | ❌ Bot Stops |
| PC On (no sleep) | ✅ Bot Runs |
| Cloud Deployed | ✅ Bot Runs 24/7 |

**Recommendation:** Deploy to cloud for 24/7 operation!

