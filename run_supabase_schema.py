# -*- coding: utf-8 -*-
"""
Run Supabase schema - Attempts multiple methods to execute SQL
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    supabase_key = os.environ.get("SUPABASE_KEY", "").strip()
    
    print("=" * 70)
    print("Supabase Schema Execution")
    print("=" * 70)
    
    # Check credentials
    if not supabase_url or not supabase_key or 'your_' in supabase_url.lower():
        print("\n⚠️  Supabase credentials not configured in .env")
        print("\nTo configure:")
        print("1. Get your Supabase URL and API key from:")
        print("   https://app.supabase.com → Your Project → Settings → API")
        print("2. Edit .env file and add:")
        print("   SUPABASE_URL=https://xxxxx.supabase.co")
        print("   SUPABASE_KEY=your_anon_key_here")
        print("\n" + "=" * 70)
        print("SQL SCHEMA (Copy to Supabase SQL Editor)")
        print("=" * 70)
        with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
            print(f.read())
        print("=" * 70)
        print("\nThen:")
        print("1. Go to: https://app.supabase.com → SQL Editor")
        print("2. Paste the SQL above")
        print("3. Click 'Run'")
        return
    
    print(f"\n✅ Credentials found")
    print(f"   URL: {supabase_url[:40]}...")
    
    # Test connection
    try:
        from supabase import create_client
        client = create_client(supabase_url, supabase_key)
        print("✅ Connected to Supabase")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # Read SQL
    with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    print("\n" + "=" * 70)
    print("IMPORTANT: Direct SQL Execution Limitation")
    print("=" * 70)
    print("\nThe Supabase Python client doesn't support executing raw SQL.")
    print("You need to run the SQL in Supabase SQL Editor.\n")
    
    print("Quick Steps:")
    print("1. Open: https://app.supabase.com")
    print("2. Select your project")
    print("3. Click 'SQL Editor' in left sidebar")
    print("4. Click 'New query'")
    print("5. Copy the SQL below")
    print("6. Paste and click 'Run' (or Ctrl+Enter)\n")
    
    print("=" * 70)
    print("SQL TO EXECUTE (Copy this)")
    print("=" * 70)
    print(sql_content)
    print("=" * 70)
    
    # Try to verify tables after (if user runs SQL manually)
    print("\n" + "=" * 70)
    print("After running SQL, verify tables:")
    print("=" * 70)
    print("\nRun this command to check:")
    print("  python -c \"from supabase import create_client; import os; from dotenv import load_dotenv; load_dotenv(); c = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY')); print('Tables:', c.table('users').select('id').limit(1).execute())\"")

if __name__ == '__main__':
    main()

