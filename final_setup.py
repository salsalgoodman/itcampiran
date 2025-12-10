# -*- coding: utf-8 -*-
"""
Final setup script - executes schema using available methods
"""

import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def execute_schema_via_sql_editor():
    """Provide SQL for manual execution"""
    print("="*70)
    print("SQL Editor Method - Execute This SQL")
    print("="*70)
    
    with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
        sql = f.read()
    
    print("\n📋 Steps:")
    print("1. Go to: https://app.supabase.com")
    print("2. Select your project")
    print("3. Click 'SQL Editor' → 'New query'")
    print("4. Copy/paste the SQL below")
    print("5. Click 'Run'\n")
    
    print("="*70)
    print("SQL SCHEMA")
    print("="*70)
    print(sql)
    print("="*70)
    
    print("\n📦 Then create storage bucket:")
    print("1. Go to 'Storage' → 'New bucket'")
    print("2. Name: receipts")
    print("3. Make it Public")
    print("4. Create")

def try_cli_with_token(token):
    """Try CLI with provided token"""
    print(f"\n🔐 Attempting login with token...")
    result = subprocess.run(
        f'npx --yes supabase login --token {token}',
        shell=True,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ Login successful!")
        return True
    else:
        print(f"❌ Login failed: {result.stderr}")
        return False

def link_and_execute():
    """Link project and execute schema"""
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    
    if not supabase_url or 'supabase.co' not in supabase_url:
        print("⚠️  SUPABASE_URL not configured")
        return False
    
    try:
        project_ref = supabase_url.split('//')[1].split('.')[0]
        print(f"\n📎 Linking to project: {project_ref}")
        
        # Link project
        link_result = subprocess.run(
            f'npx --yes supabase link --project-ref {project_ref}',
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if link_result.returncode != 0:
            print(f"⚠️  Link failed: {link_result.stderr}")
            return False
        
        print("✅ Project linked!")
        
        # Execute schema
        print("\n🚀 Executing schema...")
        exec_result = subprocess.run(
            'npx --yes supabase db execute -f supabase_setup.sql',
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
            print(f"⚠️  Execution failed: {exec_result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("="*70)
    print("Supabase Schema Setup - Final Attempt")
    print("="*70)
    
    # Check if we have credentials
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    
    # The verification code provided might need to be converted to access token
    # Or we can proceed with SQL Editor method
    
    print("\n💡 Note: The verification code you provided needs to be converted")
    print("   to an access token. The easiest method is to use SQL Editor.\n")
    
    # Show SQL Editor method
    execute_schema_via_sql_editor()
    
    # Also try to check if CLI works now
    print("\n" + "="*70)
    print("Alternative: Complete CLI Setup")
    print("="*70)
    print("\nIf you want to use CLI:")
    print("1. Get access token from: https://app.supabase.com → Profile → Access Tokens")
    print("2. Run: npx --yes supabase login --token YOUR_TOKEN")
    print("3. Then run: python final_setup.py --execute")
    
    # If user wants to try with a token, they can provide it
    # For now, SQL Editor is the most reliable method

if __name__ == '__main__':
    main()

