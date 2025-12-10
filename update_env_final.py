# -*- coding: utf-8 -*-
"""
Update .env file with final credentials (bot token and admin ID)
"""

import os

def update_env_file():
    """Update .env file with bot token and admin ID"""
    env_file = '.env'
    
    # Read current .env
    env_content = {}
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_content[key.strip()] = value.strip()
    
    # Update bot token and admin ID
    env_content['BOT_TOKEN'] = '7967637047:AAFA0MXwYkHRzVqivdn7PiKAZLM771wL7sQ'
    env_content['ADMIN_IDS'] = '581327769'
    
    # Keep other values
    defaults = {
        'SUPABASE_URL': env_content.get('SUPABASE_URL', 'https://npzffoovhbmikjwrzdhw.supabase.co'),
        'SUPABASE_KEY': env_content.get('SUPABASE_KEY', ''),
        'ZARINPAL_URL_ECONOMY': env_content.get('ZARINPAL_URL_ECONOMY', 'https://www.zarinpal.com/pg/StartPay/ECONOMY_DEMO_LINK'),
        'ZARINPAL_URL_STANDARD': env_content.get('ZARINPAL_URL_STANDARD', 'https://www.zarinpal.com/pg/StartPay/STANDARD_DEMO_LINK'),
        'ZARINPAL_URL_PROFESSIONAL': env_content.get('ZARINPAL_URL_PROFESSIONAL', 'https://www.zarinpal.com/pg/StartPay/PRO_DEMO_LINK'),
        'BANK_NAME': env_content.get('BANK_NAME', 'بانک ملت'),
        'BANK_ACCOUNT': env_content.get('BANK_ACCOUNT', 'XXXX-XXXX-XXXX-XXXX'),
        'ACCOUNT_HOLDER': env_content.get('ACCOUNT_HOLDER', 'نام صاحب حساب'),
    }
    
    # Merge
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
    print(f"  BOT_TOKEN={env_content['BOT_TOKEN'][:20]}...")
    print(f"  ADMIN_IDS={env_content['ADMIN_IDS']}")

if __name__ == '__main__':
    update_env_file()

