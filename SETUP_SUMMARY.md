# ✅ Supabase Setup Complete!

## What Has Been Done

### ✅ 1. Project Created
- **Project Name**: workshop-registration-bot
- **Project Reference**: `npzffoovhbmikjwrzdhw`
- **Project URL**: `https://npzffoovhbmikjwrzdhw.supabase.co`
- **Region**: East US (North Virginia)
- **Status**: ✅ Active and linked

### ✅ 2. Database Schema Executed
- ✅ `users` table created
- ✅ `receipts` table created
- ✅ All indexes created
- ✅ All comments added

### ⏳ 3. Next Steps (Manual)

#### Step 1: Get API Keys
1. Go to: https://app.supabase.com/project/npzffoovhbmikjwrzdhw/settings/api
2. Copy the **"anon public"** key
3. Copy the **"service_role"** key (keep this secret!)

#### Step 2: Update .env File
Edit your `.env` file and add:
```env
SUPABASE_URL=https://npzffoovhbmikjwrzdhw.supabase.co
SUPABASE_KEY=your_anon_public_key_here
```

#### Step 3: Create Storage Bucket ✅ DONE
1. Go to: https://app.supabase.com/project/npzffoovhbmikjwrzdhw/storage/buckets
2. Click **"New bucket"**
3. Name: `itcamptel` ✅ (Already created)
4. Toggle **"Public bucket"** to **ON**
5. Click **"Create bucket"**

#### Step 4: Verify Setup
Run:
```bash
python setup_check.py
```

#### Step 5: Start Bot
```bash
python workshop_signup_bot.py
```

## Project Information

- **Database Password**: `WorkshopBot2024!Secure` (saved during creation)
- **Project Dashboard**: https://app.supabase.com/project/npzffoovhbmikjwrzdhw
- **SQL Editor**: https://app.supabase.com/project/npzffoovhbmikjwrzdhw/sql/new

## Tables Created

### users
- id (BIGSERIAL PRIMARY KEY)
- telegram_id (BIGINT UNIQUE)
- name (TEXT)
- phone (TEXT)
- plan (TEXT)
- payment_method (TEXT)
- timestamp (TIMESTAMPTZ)
- status (TEXT)

### receipts
- id (BIGSERIAL PRIMARY KEY)
- user_id (BIGINT FK)
- image_url (TEXT)
- status (TEXT)
- admin_id (BIGINT)
- created_at (TIMESTAMPTZ)

## Quick Commands

```bash
# Check project status
npx --yes supabase projects list

# Link to project (already done)
npx --yes supabase link --project-ref npzffoovhbmikjwrzdhw

# View database
npx --yes supabase db pull
```

## All Done! 🎉

Your Supabase project is ready. Just complete the steps above to get your API keys and create the storage bucket, then you can start using the bot!

