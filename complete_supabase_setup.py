# -*- coding: utf-8 -*-
"""
Complete Supabase setup - handles both CLI and manual methods
"""

import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def show_cli_login_instructions():
    """Show instructions for CLI login"""
    print("="*70)
    print("Supabase CLI Login Instructions")
    print("="*70)
    print("\nTo login to Supabase CLI:")
    print("1. Run: npx --yes supabase login --no-browser")
    print("2. Copy the login link that appears")
    print("3. Open it in your browser")
    print("4. Authenticate with your Supabase account")
    print("5. Copy the verification code")
    print("6. Paste it back in the terminal")
    print("\nAfter login, you can:")
    print("- Link project: npx --yes supabase link --project-ref YOUR_REF")
    print("- Execute schema: npx --yes supabase db execute -f supabase_setup.sql")

def show_sql_editor_instructions():
    """Show instructions for SQL Editor method"""
    print("="*70)
    print("SQL Editor Method (Easiest)")
    print("="*70)
    
    # Read SQL file
    try:
        with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        print("\n📋 Steps:")
        print("1. Go to: https://app.supabase.com")
        print("2. Select your project (or create one)")
        print("3. Click 'SQL Editor' in the left sidebar")
        print("4. Click 'New query' button")
        print("5. Copy the SQL below and paste it")
        print("6. Click 'Run' button (or press Ctrl+Enter)")
        
        print("\n" + "="*70)
        print("SQL SCHEMA (Copy this)")
        print("="*70)
        print(sql_content)
        print("="*70)
        
        print("\n📦 After running SQL, create storage bucket:")
        print("1. Go to 'Storage' in left sidebar")
        print("2. Click 'New bucket'")
        print("3. Name: receipts")
        print("4. Toggle 'Public bucket' to ON")
        print("5. Click 'Create bucket'")
        
    except FileNotFoundError:
        print("❌ supabase_setup.sql not found!")

def check_credentials():
    """Check if credentials are configured"""
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    supabase_key = os.environ.get("SUPABASE_KEY", "").strip()
    
    if supabase_url and supabase_key and 'your_' not in supabase_url.lower():
        return True, supabase_url
    return False, None

def try_cli_execution():
    """Try to execute using CLI if logged in"""
    print("\n" + "="*70)
    print("Attempting CLI Execution")
    print("="*70)
    
    # Check if user is logged in
    try:
        result = subprocess.run(
            "npx --yes supabase projects list",
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print("✅ CLI is authenticated!")
            print(result.stdout)
            
            # Try to execute schema
            supabase_url, _ = check_credentials()
            if supabase_url and 'supabase.co' in supabase_url:
                try:
                    project_ref = supabase_url.split('//')[1].split('.')[0]
                    print(f"\n📎 Linking to project: {project_ref}")
                    
                    link_result = subprocess.run(
                        f"npx --yes supabase link --project-ref {project_ref}",
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    if link_result.returncode == 0:
                        print("✅ Project linked!")
                        
                        # Execute schema
                        print("\n🚀 Executing schema...")
                        exec_result = subprocess.run(
                            "npx --yes supabase db execute -f supabase_setup.sql",
                            shell=True,
                            capture_output=True,
                            text=True,
                            timeout=30
                        )
                        
                        if exec_result.returncode == 0:
                            print("✅ Schema executed successfully!")
                            print(exec_result.stdout)
                            return True
                        else:
                            print("⚠️  Schema execution failed:")
                            print(exec_result.stderr)
                    else:
                        print("⚠️  Project linking failed:")
                        print(link_result.stderr)
                except Exception as e:
                    print(f"⚠️  Error: {e}")
        else:
            print("⚠️  SUPABASE_URL not configured in .env")
            
    except subprocess.TimeoutExpired:
        print("⚠️  CLI command timed out")
    except Exception as e:
        print(f"⚠️  CLI not available or not logged in: {e}")
    
    return False

def main():
    print("="*70)
    print("Complete Supabase Setup")
    print("="*70)
    
    # Check credentials
    has_creds, supabase_url = check_credentials()
    
    if has_creds:
        print(f"\n✅ Credentials found: {supabase_url[:40]}...")
        
        # Try CLI execution first
        if try_cli_execution():
            print("\n" + "="*70)
            print("✅ Setup Complete via CLI!")
            print("="*70)
            print("\nNext steps:")
            print("1. Create storage bucket 'receipts' (if not done)")
            print("2. Run: python setup_check.py to verify")
            print("3. Run: python workshop_signup_bot.py to start bot")
            return
        else:
            print("\n⚠️  CLI execution not available")
            print("   Using SQL Editor method instead...\n")
    else:
        print("\n⚠️  Credentials not fully configured in .env")
        print("   Showing SQL Editor method...\n")
    
    # Show SQL Editor instructions
    show_sql_editor_instructions()
    
    # Also show CLI instructions as alternative
    print("\n" + "="*70)
    print("Alternative: Use Supabase CLI")
    print("="*70)
    show_cli_login_instructions()

if __name__ == '__main__':
    main()

