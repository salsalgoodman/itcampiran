# -*- coding: utf-8 -*-
"""
Prepare project for cloud deployment
Shows all environment variables needed
"""

import os
from dotenv import load_dotenv

load_dotenv()

def show_env_vars():
    """Show all environment variables needed for cloud deployment"""
    print("="*70)
    print("Environment Variables for Cloud Deployment")
    print("="*70)
    print("\nCopy these values and add them to your cloud platform:\n")
    
    vars_to_show = [
        'BOT_TOKEN',
        'SUPABASE_URL',
        'SUPABASE_KEY',
        'ADMIN_IDS',
        'ZARINPAL_URL_ECONOMY',
        'ZARINPAL_URL_STANDARD',
        'ZARINPAL_URL_PROFESSIONAL',
        'BANK_NAME',
        'BANK_ACCOUNT',
        'ACCOUNT_HOLDER',
    ]
    
    for var in vars_to_show:
        value = os.environ.get(var, 'NOT SET')
        if value and value != 'NOT SET':
            # Mask sensitive values
            if 'TOKEN' in var or 'KEY' in var:
                display_value = value[:20] + '...' if len(value) > 20 else value
            else:
                display_value = value
            print(f"{var}={display_value}")
        else:
            print(f"{var}=NOT SET")
    
    print("\n" + "="*70)
    print("Deployment Steps:")
    print("="*70)
    print("\n1. Go to Railway.app (or Render.com)")
    print("2. Create new project")
    print("3. Connect GitHub repository")
    print("4. Add the environment variables above")
    print("5. Deploy!")
    print("\nYour bot will run 24/7 in the cloud! 🚀")

if __name__ == '__main__':
    show_env_vars()

