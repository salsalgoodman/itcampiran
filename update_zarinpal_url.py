# -*- coding: utf-8 -*-
"""
Update Zarinpal URL in .env file
"""

import os
import re

ZARINPAL_URL = "https://zarinp.al/itcampiran.ir"
ENV_FILE = ".env"

def update_env_file():
    """Update or add ZARINPAL_URL in .env file"""
    
    if not os.path.exists(ENV_FILE):
        print(f"❌ {ENV_FILE} file not found!")
        print("Please create .env file from env_template.txt first")
        return False
    
    # Read current .env
    with open(ENV_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if ZARINPAL_URL exists
    if "ZARINPAL_URL=" in content:
        # Update existing
        content = re.sub(
            r'ZARINPAL_URL=.*',
            f'ZARINPAL_URL={ZARINPAL_URL}',
            content
        )
        print("✅ Updated ZARINPAL_URL")
    else:
        # Add new
        if content and not content.endswith('\n'):
            content += '\n'
        content += f'\n# Zarinpal Payment Gateway\nZARINPAL_URL={ZARINPAL_URL}\n'
        print("✅ Added ZARINPAL_URL")
    
    # Update individual plan URLs if they exist
    for plan in ['ECONOMY', 'STANDARD', 'PROFESSIONAL']:
        pattern = f'ZARINPAL_URL_{plan}=.*'
        if re.search(pattern, content):
            content = re.sub(
                pattern,
                f'ZARINPAL_URL_{plan}={ZARINPAL_URL}',
                content
            )
            print(f"✅ Updated ZARINPAL_URL_{plan}")
    
    # Write back
    with open(ENV_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Zarinpal URL updated to: {ZARINPAL_URL}")
    print("✅ All payment plans will use this URL")
    return True

if __name__ == "__main__":
    print("=" * 70)
    print("Updating Zarinpal Payment Gateway URL")
    print("=" * 70)
    print(f"\nURL: {ZARINPAL_URL}\n")
    
    if update_env_file():
        print("\n✅ Done! You can now restart the bot.")
    else:
        print("\n⚠️  Please manually add to .env file:")
        print(f"   ZARINPAL_URL={ZARINPAL_URL}")

