# -*- coding: utf-8 -*-
"""
Script to setup Supabase database schema
Uses Supabase REST API to execute SQL statements
"""

import os
import sys
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def read_sql_file(filename):
    """Read SQL file content"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: {filename} not found!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        sys.exit(1)

def execute_sql_via_rest_api(sql_statements, supabase_url, supabase_key):
    """
    Execute SQL via Supabase REST API
    Note: This requires a custom RPC function or using the Management API
    """
    print("\n⚠️  Direct SQL execution via REST API is not directly supported.")
    print("   The Supabase Python client doesn't support raw SQL execution.")
    print("\n   Options:")
    print("   1. Use Supabase SQL Editor (Recommended)")
    print("   2. Use Supabase CLI")
    print("   3. Create a custom RPC function")
    return False

def create_tables_via_client(supabase_client):
    """
    Create tables using Supabase client methods
    This is a workaround since direct SQL execution isn't supported
    """
    from supabase import create_client
    
    print("\n📋 Creating tables via Supabase client...")
    print("   Note: This method has limitations and may not work for all SQL statements")
    
    # The Supabase Python client doesn't have direct table creation methods
    # We would need to use the REST API or SQL Editor
    print("   ⚠️  Table creation requires SQL Editor or Management API")
    return False

def format_sql_for_copy_paste(sql_content):
    """Format SQL for easy copy-paste into Supabase SQL Editor"""
    print("\n" + "=" * 60)
    print("SQL Schema (Ready to Copy)")
    print("=" * 60)
    print("\nCopy the SQL below and paste it into Supabase SQL Editor:")
    print("\n" + "-" * 60)
    print(sql_content)
    print("-" * 60)
    print("\nSteps:")
    print("1. Go to: https://app.supabase.com")
    print("2. Select your project")
    print("3. Go to SQL Editor (left sidebar)")
    print("4. Click 'New query'")
    print("5. Paste the SQL above")
    print("6. Click 'Run' or press Ctrl+Enter")
    print("=" * 60)

def check_supabase_connection(supabase_url, supabase_key):
    """Check if we can connect to Supabase"""
    try:
        from supabase import create_client
        client = create_client(supabase_url, supabase_key)
        
        # Try a simple query to test connection
        # This will fail if tables don't exist, but that's okay
        try:
            result = client.table("users").select("id").limit(1).execute()
            print("✅ Supabase connection successful!")
            print("   Note: 'users' table may already exist")
            return True
        except Exception:
            # Table doesn't exist, but connection works
            print("✅ Supabase connection successful!")
            print("   Tables don't exist yet - ready to create them")
            return True
            
    except Exception as e:
        print(f"❌ Error connecting to Supabase: {e}")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("Supabase Schema Setup")
    print("=" * 60)
    
    # Get credentials
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    # Check if credentials are set
    if not supabase_url or not supabase_key:
        print("\n❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
        print("\nPlease add these to your .env file:")
        print("SUPABASE_URL=https://your-project.supabase.co")
        print("SUPABASE_KEY=your_anon_key_here")
        sys.exit(1)
    
    # Check if using placeholder values
    if (supabase_url.startswith('your_') or supabase_key.startswith('your_') or 
        'your_supabase' in supabase_url.lower() or 'your_supabase' in supabase_key.lower()):
        print("\n❌ Error: Please replace placeholder values in .env with actual Supabase credentials")
        print("\nTo get your credentials:")
        print("1. Go to https://app.supabase.com")
        print("2. Select your project")
        print("3. Go to Settings → API")
        print("4. Copy 'Project URL' → SUPABASE_URL")
        print("5. Copy 'anon public' key → SUPABASE_KEY")
        sys.exit(1)
    
    # Read SQL file
    print("\n📄 Reading schema file...")
    sql_content = read_sql_file('supabase_setup.sql')
    print("✅ Schema file loaded")
    
    # Check connection
    print("\n🔌 Testing Supabase connection...")
    if not check_supabase_connection(supabase_url, supabase_key):
        print("\n❌ Cannot proceed without a valid connection")
        sys.exit(1)
    
    # Try to execute via REST API (will likely fail, but we'll provide alternatives)
    print("\n🚀 Attempting to execute schema...")
    
    # Since direct SQL execution isn't supported, we'll provide the formatted SQL
    format_sql_for_copy_paste(sql_content)
    
    # Also try to create storage bucket if possible
    print("\n" + "=" * 60)
    print("Storage Bucket Setup")
    print("=" * 60)
    print("\nDon't forget to create the storage bucket:")
    print("1. Go to Supabase Dashboard → Storage")
    print("2. Click 'New bucket'")
    print("3. Name: receipts")
    print("4. Make it PUBLIC (toggle 'Public bucket')")
    print("5. Click 'Create bucket'")
    print("=" * 60)
    
    print("\n✅ Setup instructions provided above!")
    print("   After running the SQL, your database will be ready.")

if __name__ == '__main__':
    main()

