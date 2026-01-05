-- اضافه کردن فیلدهای مورد نیاز برای سیستم پرداخت
-- این فایل را در Supabase SQL Editor اجرا کنید

-- اضافه کردن فیلدهای پرداخت به جدول users
ALTER TABLE users 
ADD COLUMN IF NOT EXISTS payment_method TEXT,
ADD COLUMN IF NOT EXISTS payment_amount INTEGER,
ADD COLUMN IF NOT EXISTS payment_receipt_url TEXT,
ADD COLUMN IF NOT EXISTS has_paid_for_lessons BOOLEAN DEFAULT FALSE,
ADD COLUMN IF NOT EXISTS payment_status TEXT DEFAULT 'pending',
ADD COLUMN IF NOT EXISTS payment_approved_at TIMESTAMPTZ;

-- ایجاد ایندکس برای جستجوی سریع‌تر
CREATE INDEX IF NOT EXISTS idx_users_payment_status ON users(payment_status);
CREATE INDEX IF NOT EXISTS idx_users_has_paid ON users(has_paid_for_lessons);

-- نمایش نتیجه
SELECT 
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'users'
AND column_name IN (
    'payment_method',
    'payment_amount',
    'payment_receipt_url',
    'has_paid_for_lessons',
    'payment_status',
    'payment_approved_at'
)
ORDER BY column_name;

