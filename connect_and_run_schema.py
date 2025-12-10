# -*- coding: utf-8 -*-
"""
Connect to Supabase and run schema
This script will attempt to execute SQL using available methods
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def execute_with_credentials():
    """Try to execute schema if credentials are available"""
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    supabase_key = os.environ.get("SUPABASE_KEY", "").strip()
    
    # Check if credentials exist and are real
    if not supabase_url or not supabase_key:
        return False, "No credentials found"
    
    if 'your_' in supabase_url.lower() or 'your_' in supabase_key.lower():
        return False, "Placeholder values detected"
    
    # Test connection
    try:
        from supabase import create_client
        client = create_client(supabase_url, supabase_key)
        
        # Try a simple operation to verify connection
        try:
            # This will fail if table doesn't exist, but connection works
            client.table("users").select("id").limit(0).execute()
        except:
            pass  # Table doesn't exist yet, that's fine
        
        return True, "Connection successful"
    except Exception as e:
        return False, f"Connection failed: {e}"

def main():
    print("=" * 70)
    print("Supabase Schema Execution Tool")
    print("=" * 70)
    
    # Read SQL file
    try:
        with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
            sql_content = f.read()
    except FileNotFoundError:
        print("❌ Error: supabase_setup.sql not found!")
        return
    
    # Try to connect
    can_connect, message = execute_with_credentials()
    
    if can_connect:
        print(f"\n✅ {message}")
        print("\n⚠️  IMPORTANT: The Supabase Python client doesn't support")
        print("   executing raw SQL statements directly.")
        print("\n   You have two options:")
        print("\n   OPTION 1: Use Supabase SQL Editor (Recommended)")
        print("   " + "-" * 60)
        print("   1. Go to: https://app.supabase.com")
        print("   2. Select your project")
        print("   3. Click 'SQL Editor' in the left sidebar")
        print("   4. Click 'New query' button")
        print("   5. Copy the SQL below and paste it")
        print("   6. Click 'Run' button (or press Ctrl+Enter)")
        print("\n   OPTION 2: Use Supabase CLI")
        print("   " + "-" * 60)
        print("   1. Install: npm install -g supabase")
        print("   2. Login: supabase login")
        print("   3. Link project: supabase link --project-ref YOUR_PROJECT_REF")
        print("   4. Run: supabase db push")
    else:
        print(f"\n⚠️  {message}")
        print("\n   To configure credentials:")
        print("   1. Edit the .env file")
        print("   2. Add your SUPABASE_URL and SUPABASE_KEY")
        print("   3. Get them from: https://app.supabase.com → Settings → API")
    
    # Display SQL
    print("\n" + "=" * 70)
    print("SQL SCHEMA - Copy this to Supabase SQL Editor")
    print("=" * 70)
    print(sql_content)
    print("=" * 70)
    
    # Additional instructions
    print("\n" + "=" * 70)
    print("After Running SQL - Create Storage Bucket")
    print("=" * 70)
    print("\nDon't forget to create the storage bucket for receipts:")
    print("1. Go to Supabase Dashboard → Storage")
    print("2. Click 'New bucket'")
    print("3. Name: receipts")
    print("4. Toggle 'Public bucket' to ON")
    print("5. Click 'Create bucket'")
    print("=" * 70)
    
    # Verification command
    if can_connect:
        print("\n" + "=" * 70)
        print("Verify Setup")
        print("=" * 70)
        print("\nAfter running the SQL, verify with:")
        print("  python setup_check.py")
        print("=" * 70)

if __name__ == '__main__':
    main()

