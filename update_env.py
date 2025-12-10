# -*- coding: utf-8 -*-
"""
Update .env file with Supabase credentials
"""

import os
import re

def update_env_file():
    """Update .env file with actual credentials"""
    env_file = '.env'
    
    # Read current .env if it exists
    env_content = {}
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_content[key.strip()] = value.strip()
    
    # Update Supabase credentials
    env_content['SUPABASE_URL'] = 'https://npzffoovhbmikjwrzdhw.supabase.co'
    env_content['SUPABASE_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5wemZmb292aGJtaWtqd3J6ZGh3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ1Mzc3MDYsImV4cCI6MjA4MDExMzcwNn0.RV8pVrHspveFIjlk-gFZei0vC3qA445xBCvwi_Qwf84'
    
    # Keep other values or use defaults
    defaults = {
        'BOT_TOKEN': env_content.get('BOT_TOKEN', 'your_telegram_bot_token_here'),
        'ADMIN_IDS': env_content.get('ADMIN_IDS', '11111111,22222222,33333333,44444444,55555555'),
        'ZARINPAL_URL_ECONOMY': env_content.get('ZARINPAL_URL_ECONOMY', 'https://www.zarinpal.com/pg/StartPay/ECONOMY_DEMO_LINK'),
        'ZARINPAL_URL_STANDARD': env_content.get('ZARINPAL_URL_STANDARD', 'https://www.zarinpal.com/pg/StartPay/STANDARD_DEMO_LINK'),
        'ZARINPAL_URL_PROFESSIONAL': env_content.get('ZARINPAL_URL_PROFESSIONAL', 'https://www.zarinpal.com/pg/StartPay/PRO_DEMO_LINK'),
        'BANK_NAME': env_content.get('BANK_NAME', 'بانک ملت'),
        'BANK_ACCOUNT': env_content.get('BANK_ACCOUNT', 'XXXX-XXXX-XXXX-XXXX'),
        'ACCOUNT_HOLDER': env_content.get('ACCOUNT_HOLDER', 'نام صاحب حساب'),
    }
    
    # Merge defaults with existing content
    for key, value in defaults.items():
        if key not in env_content:
            env_content[key] = value
    
    # Write updated .env file
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write("# Telegram Bot Configuration\n")
        f.write(f"BOT_TOKEN={env_content['BOT_TOKEN']}\n\n")
        f.write("# Supabase Configuration\n")
        f.write(f"SUPABASE_URL={env_content['SUPABASE_URL']}\n")
        f.write(f"SUPABASE_KEY={env_content['SUPABASE_KEY']}\n\n")
        f.write("# Admin Telegram User IDs (comma-separated, no spaces)\n")
        f.write(f"ADMIN_IDS={env_content['ADMIN_IDS']}\n\n")
        f.write("# Zarinpal Payment URLs (for each plan)\n")
        f.write(f"ZARINPAL_URL_ECONOMY={env_content['ZARINPAL_URL_ECONOMY']}\n")
        f.write(f"ZARINPAL_URL_STANDARD={env_content['ZARINPAL_URL_STANDARD']}\n")
        f.write(f"ZARINPAL_URL_PROFESSIONAL={env_content['ZARINPAL_URL_PROFESSIONAL']}\n\n")
        f.write("# Bank Account Information (for manual transfers)\n")
        f.write(f"BANK_NAME={env_content['BANK_NAME']}\n")
        f.write(f"BANK_ACCOUNT={env_content['BANK_ACCOUNT']}\n")
        f.write(f"ACCOUNT_HOLDER={env_content['ACCOUNT_HOLDER']}\n")
    
    print("✅ .env file updated successfully!")
    print(f"\nUpdated:")
    print(f"  SUPABASE_URL={env_content['SUPABASE_URL']}")
    print(f"  SUPABASE_KEY={env_content['SUPABASE_KEY'][:30]}...")
    
    # Also save service role key to a separate secure file (optional)
    service_role_file = '.env.service_role'
    with open(service_role_file, 'w', encoding='utf-8') as f:
        f.write("# Service Role Key - KEEP THIS SECRET!\n")
        f.write("# This key has full access to your Supabase project\n")
        f.write("# Never commit this file to git!\n\n")
        f.write("SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5wemZmb292aGJtaWtqd3J6ZGh3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDUzNzcwNiwiZXhwIjoyMDgwMTEzNzA2fQ.TBD28IscFMgjPxD0nillOtUJKYwRJITxXhDkb7oicm4\n")
    
    print(f"\n⚠️  Service role key saved to {service_role_file}")
    print("   Keep this file secure and never commit it to git!")

if __name__ == '__main__':
    update_env_file()

