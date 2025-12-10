-- Supabase Database Setup for Workshop Registration Bot
-- Run this script in Supabase SQL Editor

-- Create users table
CREATE TABLE IF NOT EXISTS users (
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
CREATE TABLE IF NOT EXISTS receipts (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    admin_id BIGINT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_telegram_id ON users(telegram_id);
CREATE INDEX IF NOT EXISTS idx_users_status ON users(status);
CREATE INDEX IF NOT EXISTS idx_users_timestamp ON users(timestamp);
CREATE INDEX IF NOT EXISTS idx_receipts_user_id ON receipts(user_id);
CREATE INDEX IF NOT EXISTS idx_receipts_status ON receipts(status);
CREATE INDEX IF NOT EXISTS idx_receipts_admin_id ON receipts(admin_id);

-- Add comments for documentation
COMMENT ON TABLE users IS 'Stores user registration information';
COMMENT ON TABLE receipts IS 'Stores payment receipt images for offline payments';
COMMENT ON COLUMN users.telegram_id IS 'Telegram user ID (unique identifier)';
COMMENT ON COLUMN users.plan IS 'Selected plan: اقتصادی, استاندارد, or حرفه‌ای';
COMMENT ON COLUMN users.payment_method IS 'Payment method: online or offline';
COMMENT ON COLUMN users.status IS 'Registration status: pending, confirmed, or rejected';
COMMENT ON COLUMN receipts.status IS 'Receipt status: pending, approved, or rejected';
COMMENT ON COLUMN receipts.admin_id IS 'Telegram ID of admin who processed this receipt';

