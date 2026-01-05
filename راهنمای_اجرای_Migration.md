# راهنمای اجرای Migration با Supabase CLI

## روش 1: استفاده از Supabase CLI (توصیه می‌شود)

### نصب Supabase CLI (اگر نصب نشده):

```bash
# Windows (با Chocolatey)
choco install supabase

# یا با npm
npm install -g supabase

# یا با Scoop
scoop install supabase
```

### اتصال به پروژه Supabase:

```bash
# اگر قبلاً link نشده
supabase link --project-ref YOUR_PROJECT_REF

# یا با URL کامل
supabase link --project-ref npzffoovhbmikjwrzdhw
```

### اجرای Migration:

```bash
# اجرای همه migration‌های جدید
supabase db push

# یا اجرای یک migration خاص
supabase migration up
```

### بررسی وضعیت:

```bash
# مشاهده migration‌های اجرا شده
supabase migration list

# مشاهده وضعیت دیتابیس
supabase db diff
```

## روش 2: استفاده از Supabase Dashboard

1. به **Supabase Dashboard** بروید
2. **SQL Editor** را باز کنید
3. محتوای فایل `add_payment_fields.sql` را کپی کنید
4. در SQL Editor paste کنید
5. روی **Run** کلیک کنید

## روش 3: استفاده از Supabase API

می‌توانید از Python script استفاده کنید:

```python
from supabase import create_client
import os

supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

# اجرای SQL
with open('add_payment_fields.sql', 'r', encoding='utf-8') as f:
    sql = f.read()
    # Note: Supabase Python client doesn't support raw SQL execution
    # You need to use Supabase Dashboard or CLI for migrations
```

## بررسی فیلدهای اضافه شده

بعد از اجرای migration، می‌توانید با این SQL بررسی کنید:

```sql
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
```

## نکات مهم

- Migration‌ها باید به ترتیب timestamp اجرا شوند
- فایل migration در `supabase/migrations/` قرار دارد
- بعد از اجرای migration، Railway به‌صورت خودکار تغییرات را دریافت می‌کند
- اگر از Supabase CLI استفاده می‌کنید، حتماً `supabase link` را انجام دهید

## عیب‌یابی

اگر migration اجرا نشد:

1. بررسی کنید که Supabase CLI نصب شده باشد
2. بررسی کنید که به پروژه درست link شده باشید
3. لاگ‌ها را بررسی کنید: `supabase migration list --verbose`
4. می‌توانید از Supabase Dashboard استفاده کنید

