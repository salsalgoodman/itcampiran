# -*- coding: utf-8 -*-
"""
Create Supabase tables directly using Python client
This bypasses the need for CLI authentication
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

def create_tables_via_api():
    """Create tables using Supabase REST API"""
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    supabase_key = os.environ.get("SUPABASE_KEY", "").strip()
    
    if not supabase_url or not supabase_key:
        print("❌ SUPABASE_URL and SUPABASE_KEY required in .env")
        return False
    
    if 'your_' in supabase_url.lower() or 'your_' in supabase_key.lower():
        print("❌ Please configure actual Supabase credentials in .env")
        return False
    
    print("="*70)
    print("Creating Tables via Supabase API")
    print("="*70)
    print(f"\nConnecting to: {supabase_url[:40]}...")
    
    try:
        client: Client = create_client(supabase_url, supabase_key)
        print("✅ Connected to Supabase")
        
        # Read SQL file
        with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        print("\n⚠️  IMPORTANT: The Supabase Python client doesn't support")
        print("   executing raw SQL statements directly.")
        print("\n   However, we can verify your connection and provide")
        print("   the SQL ready to execute.\n")
        
        # Test connection by trying to query (will fail if tables don't exist, but connection works)
        try:
            result = client.table("users").select("id").limit(1).execute()
            print("✅ Connection verified - 'users' table may already exist")
        except Exception as e:
            if "relation" in str(e).lower() or "does not exist" in str(e).lower():
                print("✅ Connection verified - tables don't exist yet (ready to create)")
            else:
                print(f"⚠️  Connection test: {e}")
        
        print("\n" + "="*70)
        print("SQL TO EXECUTE IN SUPABASE SQL EDITOR")
        print("="*70)
        print(sql_content)
        print("="*70)
        
        print("\n📋 Instructions:")
        print("1. Go to: https://app.supabase.com")
        print("2. Select your project")
        print("3. Click 'SQL Editor' → 'New query'")
        print("4. Copy the SQL above and paste it")
        print("5. Click 'Run' (or Ctrl+Enter)")
        print("\n✅ After running SQL, your tables will be created!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPlease check:")
        print("1. SUPABASE_URL is correct")
        print("2. SUPABASE_KEY is correct (use 'anon public' key)")
        print("3. Your internet connection is working")
        return False

def main():
    print("="*70)
    print("Direct Table Creation via Supabase API")
    print("="*70)
    
    if create_tables_via_api():
        print("\n" + "="*70)
        print("Next Steps")
        print("="*70)
        print("\n1. ✅ Execute SQL in Supabase SQL Editor (see above)")
        print("2. 📦 Create storage bucket:")
        print("   → Go to Storage → New bucket")
        print("   → Name: receipts")
        print("   → Make it Public")
        print("   → Create")
        print("3. ✅ Verify setup:")
        print("   → Run: python setup_check.py")
        print("4. 🚀 Start bot:")
        print("   → Run: python workshop_signup_bot.py")
    else:
        print("\n⚠️  Setup incomplete. Please configure .env file first.")

if __name__ == '__main__':
    main()

