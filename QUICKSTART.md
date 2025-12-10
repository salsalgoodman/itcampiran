# Quick Start Guide

## Step-by-Step Setup

### 1. ✅ Install Dependencies (DONE)
```bash
pip install -r requirements.txt
```
**Status**: ✅ Completed

### 2. ⚙️ Configure Environment Variables

Edit the `.env` file and fill in your actual values:

#### Get Telegram Bot Token:
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
5. Paste it in `.env` as `BOT_TOKEN=your_token_here`

#### Get Supabase Credentials:
1. Go to [supabase.com](https://supabase.com) and sign up/login
2. Create a new project (or use existing)
3. Go to Project Settings → API
4. Copy:
   - **Project URL** → `SUPABASE_URL` in `.env`
   - **anon/public key** → `SUPABASE_KEY` in `.env`

#### Set Admin IDs:
1. In Telegram, search for `@userinfobot`
2. Send `/start` to get your Telegram user ID
3. Repeat for all admins
4. Add all IDs (comma-separated, no spaces) to `ADMIN_IDS` in `.env`
   Example: `ADMIN_IDS=123456789,987654321,111222333`

#### Configure Payment URLs:
- Replace Zarinpal URLs with your actual payment gateway links
- Update bank account information for manual transfers

### 3. 🗄️ Setup Supabase Database

#### Option A: Using SQL File (Recommended)
1. Go to Supabase Dashboard → SQL Editor
2. Open `supabase_setup.sql` file
3. Copy all SQL commands
4. Paste into SQL Editor
5. Click "Run" to execute

#### Option B: Manual Setup
Run these commands in Supabase SQL Editor:

```sql
-- Create users table
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

-- Create receipts table
CREATE TABLE receipts (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    admin_id BIGINT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes
CREATE INDEX idx_users_telegram_id ON users(telegram_id);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_receipts_user_id ON receipts(user_id);
CREATE INDEX idx_receipts_status ON receipts(status);
```

### 4. 📦 Setup Supabase Storage

1. Go to Supabase Dashboard → Storage
2. Click "New bucket"
3. Name it: `receipts`
4. **Important**: Make it **Public** (toggle "Public bucket")
5. Click "Create bucket"

### 5. ✅ Verify Setup

Run the setup verification script:
```bash
python setup_check.py
```

This will check:
- ✅ Environment file exists
- ✅ Python packages installed
- ✅ Environment variables configured
- ✅ Supabase connection working

### 6. 🚀 Start the Bot

```bash
python workshop_signup_bot.py
```

You should see:
```
INFO - Bot started!
```

### 7. 🧪 Test the Bot

1. Open Telegram
2. Search for your bot (the username you gave it)
3. Send `/start`
4. You should see the plan selection menu

## Troubleshooting

### Bot doesn't respond
- Check if `BOT_TOKEN` is correct in `.env`
- Make sure bot is running (check terminal for errors)
- Verify internet connection

### Supabase connection errors
- Verify `SUPABASE_URL` and `SUPABASE_KEY` are correct
- Check if tables exist (go to Table Editor in Supabase)
- Ensure your network can reach Supabase

### Image upload fails
- Verify `receipts` bucket exists in Supabase Storage
- Check bucket is set to **Public**
- Check file permissions in Supabase Storage settings

### Admin commands don't work
- Verify your Telegram user ID is in `ADMIN_IDS`
- Make sure IDs are comma-separated with no spaces
- Restart the bot after changing `.env`

## Next Steps

1. ✅ Configure your payment gateway (Zarinpal)
2. ✅ Update bank account information
3. ✅ Test the complete registration flow
4. ✅ Deploy to a server (optional) for 24/7 operation

## Deployment Options

For production, consider deploying to:
- **Heroku**: Easy deployment with git
- **Railway**: Simple container deployment
- **DigitalOcean**: VPS with more control
- **AWS/GCP**: Enterprise solutions

Remember to:
- Set environment variables in your hosting platform
- Keep `.env` file secure (never commit to git)
- Set up logging/monitoring
- Consider using a process manager (PM2, supervisor)

## Support

If you encounter issues:
1. Check the logs in terminal
2. Run `python setup_check.py` to verify setup
3. Review the README.md for detailed documentation
4. Check Supabase and Telegram Bot API documentation

