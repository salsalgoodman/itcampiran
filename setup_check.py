# -*- coding: utf-8 -*-
"""
Setup verification script for Workshop Registration Bot
Checks if all required configurations are in place
"""

import os
import sys
from dotenv import load_dotenv

def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("   Please create .env file from env_template.txt")
        return False
    print("✅ .env file exists")
    return True

def check_env_variables():
    """Check if all required environment variables are set"""
    load_dotenv()
    
    required_vars = {
        'BOT_TOKEN': 'Telegram Bot Token',
        'SUPABASE_URL': 'Supabase Project URL',
        'SUPABASE_KEY': 'Supabase API Key',
        'ADMIN_IDS': 'Admin Telegram User IDs',
    }
    
    missing = []
    for var, description in required_vars.items():
        value = os.environ.get(var)
        if not value or value.startswith('your_') or value.startswith('YOUR_'):
            missing.append(f"  - {var} ({description})")
        else:
            print(f"✅ {var} is set")
    
    if missing:
        print("\n❌ Missing or not configured environment variables:")
        for var in missing:
            print(var)
        print("\nPlease update your .env file with actual values.")
        return False
    
    return True

def check_packages():
    """Check if required packages are installed"""
    required_packages = [
        'telegram',
        'supabase',
        'dotenv',
        'jdatetime'
    ]
    
    missing = []
    for package in required_packages:
        try:
            if package == 'telegram':
                __import__('telegram')
            elif package == 'dotenv':
                __import__('dotenv')
            else:
                __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            missing.append(package)
            print(f"❌ {package} is not installed")
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    return True

def check_supabase_connection():
    """Check Supabase connection"""
    try:
        from supabase import create_client
        load_dotenv()
        
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        
        if not url or not key or url.startswith('your_') or key.startswith('your_'):
            print("⚠️  Supabase credentials not configured, skipping connection test")
            return True
        
        client = create_client(url, key)
        # Try a simple query
        result = client.table("users").select("id").limit(1).execute()
        print("✅ Supabase connection successful")
        return True
    except Exception as e:
        print(f"⚠️  Supabase connection test failed: {e}")
        print("   Make sure:")
        print("   1. SUPABASE_URL and SUPABASE_KEY are correct")
        print("   2. The 'users' table exists in your database")
        print("   3. Your network connection is working")
        return False

def main():
    """Run all checks"""
    print("=" * 50)
    print("Workshop Registration Bot - Setup Verification")
    print("=" * 50)
    print()
    
    checks = [
        ("Environment File", check_env_file),
        ("Python Packages", check_packages),
        ("Environment Variables", check_env_variables),
        ("Supabase Connection", check_supabase_connection),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n[{name}]")
        print("-" * 30)
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error during check: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
        if not result:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 All checks passed! You're ready to run the bot.")
        print("   Run: python workshop_signup_bot.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above before running the bot.")
        sys.exit(1)

if __name__ == '__main__':
    main()

