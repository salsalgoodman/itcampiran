# Bot Deployment Guide - Keep Bot Running

## ⚠️ Important: Terminal Closing Stops Bot

If you close the terminal, the bot will stop. Here are solutions to keep it running:

## Option 1: Run in Background Window (Windows - Easiest)

```bash
python run_bot_background.py
```

This starts the bot in a separate window. You can close your terminal, but keep the bot window open.

## Option 2: Use PM2 (Recommended for Production)

PM2 is a process manager that keeps your bot running even after closing terminal.

### Install PM2:
```bash
npm install -g pm2
```

### Start bot with PM2:
```bash
pm2 start workshop_signup_bot.py --name workshop-bot --interpreter python
```

### Useful PM2 Commands:
```bash
pm2 list              # View running processes
pm2 logs workshop-bot # View bot logs
pm2 stop workshop-bot # Stop bot
pm2 restart workshop-bot # Restart bot
pm2 delete workshop-bot # Remove from PM2
pm2 save              # Save current process list
pm2 startup           # Auto-start on system boot
```

## Option 3: Windows Task Scheduler

1. Open Task Scheduler (search in Windows)
2. Create Basic Task
3. Name: "Workshop Bot"
4. Trigger: "When I log on" or "At startup"
5. Action: "Start a program"
6. Program: `python`
7. Arguments: `C:\Users\samern\Desktop\itcamptel\workshop_signup_bot.py`
8. Start in: `C:\Users\samern\Desktop\itcamptel`
9. Check "Run whether user is logged on or not"

## Option 4: Use NSSM (Windows Service)

NSSM (Non-Sucking Service Manager) runs your bot as a Windows service.

### Install NSSM:
1. Download from: https://nssm.cc/download
2. Extract to a folder (e.g., `C:\nssm`)

### Install as Service:
```bash
# Open PowerShell as Administrator
cd C:\nssm\win64
.\nssm.exe install WorkshopBot "C:\ProgramData\miniconda3\python.exe" "C:\Users\samern\Desktop\itcamptel\workshop_signup_bot.py"
.\nssm.exe set WorkshopBot AppDirectory "C:\Users\samern\Desktop\itcamptel"
.\nssm.exe start WorkshopBot
```

### Service Commands:
```bash
.\nssm.exe start WorkshopBot    # Start service
.\nssm.exe stop WorkshopBot     # Stop service
.\nssm.exe restart WorkshopBot  # Restart service
.\nssm.exe remove WorkshopBot   # Remove service
```

## Option 5: Cloud Deployment (Best for 24/7)

Deploy to a cloud service that runs 24/7:

### Railway
1. Go to https://railway.app
2. Create new project
3. Connect GitHub repo
4. Add environment variables
5. Deploy

### Render
1. Go to https://render.com
2. Create new Web Service
3. Connect repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `python workshop_signup_bot.py`
6. Add environment variables

### Heroku
1. Install Heroku CLI
2. Create Procfile: `worker: python workshop_signup_bot.py`
3. Deploy: `git push heroku main`

### DigitalOcean App Platform
1. Create app
2. Connect repo
3. Set run command
4. Add env vars

## Option 6: VPS (Virtual Private Server)

Rent a VPS and run the bot there:
- DigitalOcean Droplet ($5/month)
- AWS EC2
- Google Cloud Compute
- Azure VM

Then use PM2 or systemd to keep it running.

## Quick Start (Right Now)

**Easiest immediate solution:**
```bash
python run_bot_background.py
```

This opens the bot in a separate window. Just don't close that window!

## Monitoring

### Check if bot is running:
```bash
# Windows Task Manager
# Look for python.exe process

# Or with PM2
pm2 list
```

### View logs:
```bash
# If using PM2
pm2 logs workshop-bot

# Or check the bot window output
```

## Recommended Setup

For development/testing:
- Use `run_bot_background.py` (separate window)

For production:
- Use PM2 (easy to manage)
- Or deploy to cloud (Railway/Render)

## Troubleshooting

### Bot stops unexpectedly:
- Check logs for errors
- Verify internet connection
- Check Supabase connection
- Verify Telegram API is accessible

### Bot not responding:
- Restart the bot
- Check if process is running
- Verify BOT_TOKEN is correct
- Check firewall settings

