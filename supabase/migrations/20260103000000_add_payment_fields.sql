-- Migration: اضافه کردن فیلدهای مورد نیاز برای سیستم پرداخت
-- Created: 2026-01-03
-- Description: اضافه کردن فیلدهای پرداخت به جدول users

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

-- کامنت برای مستندسازی
COMMENT ON COLUMN users.payment_method IS 'روش پرداخت: card_to_card, online, etc.';
COMMENT ON COLUMN users.payment_amount IS 'مبلغ پرداخت شده به تومان';
COMMENT ON COLUMN users.payment_receipt_url IS 'لینک فیش واریزی در Supabase Storage';
COMMENT ON COLUMN users.has_paid_for_lessons IS 'آیا کاربر برای درس‌ها پرداخت کرده است';
COMMENT ON COLUMN users.payment_status IS 'وضعیت پرداخت: pending, approved, rejected';
COMMENT ON COLUMN users.payment_approved_at IS 'زمان تایید پرداخت توسط ادمین';

