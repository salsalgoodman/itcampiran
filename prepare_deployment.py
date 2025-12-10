# -*- coding: utf-8 -*-
"""
Prepare project for deployment to Render.com
Checks all required files and creates deployment checklist
"""

import os
import sys

def check_file_exists(filename, required=True):
    """Check if a file exists"""
    exists = os.path.exists(filename)
    status = "✅" if exists else ("❌" if required else "⚠️")
    print(f"{status} {filename}")
    return exists

def main():
    print("=" * 70)
    print("🔍 بررسی فایل‌های لازم برای استقرار")
    print("=" * 70)
    print()
    
    required_files = [
        ("workshop_signup_bot.py", True),
        ("requirements.txt", True),
        ("Procfile", True),
        ("runtime.txt", False),
        (".gitignore", False),
    ]
    
    all_ok = True
    for filename, required in required_files:
        if not check_file_exists(filename, required):
            if required:
                all_ok = False
    
    print()
    print("=" * 70)
    
    if all_ok:
        print("✅ همه فایل‌های لازم موجود است!")
        print()
        print("📋 مراحل بعدی:")
        print("1. git add .")
        print("2. git commit -m 'Bot ready for deployment'")
        print("3. ایجاد Repository در GitHub")
        print("4. git push")
        print("5. استقرار در Render.com")
        print()
        print("📖 برای راهنمای کامل، فایل DEPLOY_TO_RENDER.md را بخوانید")
    else:
        print("❌ برخی فایل‌های لازم موجود نیست!")
        print("لطفاً فایل‌های گم شده را ایجاد کنید.")
        sys.exit(1)
    
    print("=" * 70)

if __name__ == "__main__":
    main()

