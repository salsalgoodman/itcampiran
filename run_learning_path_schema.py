# -*- coding: utf-8 -*-
"""
Execute Learning Path Schema via Supabase
Uses HTTP requests to execute SQL via Supabase REST API
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "").strip()  # Service role key for admin operations

def execute_sql_via_rpc(sql_statement: str) -> bool:
    """Try to execute SQL via RPC function"""
    try:
        # First, we need to create an RPC function that can execute SQL
        # But this requires admin access
        if not SUPABASE_SERVICE_KEY:
            return False
        
        # Use Management API endpoint
        # Supabase Management API: https://supabase.com/docs/reference/api/introduction
        project_ref = SUPABASE_URL.split("//")[1].split(".")[0] if "." in SUPABASE_URL else None
        if not project_ref:
            return False
        
        # Try using the REST API with service role key
        headers = {
            "apikey": SUPABASE_SERVICE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
            "Content-Type": "application/json"
        }
        
        # Supabase doesn't have a direct SQL execution endpoint via REST
        # We need to use the SQL Editor API or create tables programmatically
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_tables_programmatically():
    """Create tables using Supabase client operations"""
    try:
        from supabase import create_client, Client
        
        if not SUPABASE_URL or not SUPABASE_KEY:
            print("❌ SUPABASE_URL and SUPABASE_KEY required")
            return False
        
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Unfortunately, Supabase Python client doesn't support CREATE TABLE
        # We need to use the SQL Editor or Management API
        print("⚠️  Supabase Python client doesn't support CREATE TABLE operations")
        print("   We need to use Supabase SQL Editor or Management API")
        
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def execute_via_management_api():
    """Try to execute SQL via Supabase Management API"""
    try:
        if not SUPABASE_SERVICE_KEY:
            print("⚠️  SUPABASE_SERVICE_KEY not found in .env")
            print("   Using anon key - this may not work for schema operations")
            api_key = SUPABASE_KEY
        else:
            api_key = SUPABASE_SERVICE_KEY
        
        # Extract project reference from URL
        # URL format: https://xxxxx.supabase.co
        project_ref = None
        if SUPABASE_URL:
            parts = SUPABASE_URL.replace("https://", "").replace("http://", "").split(".")
            if len(parts) > 0:
                project_ref = parts[0]
        
        if not project_ref:
            print("❌ Could not extract project reference from SUPABASE_URL")
            return False
        
        print(f"📋 Project Reference: {project_ref}")
        
        # Supabase Management API endpoint for executing SQL
        # Note: This requires a service role key and proper API setup
        # The Management API is typically accessed via: https://api.supabase.com/v1/projects/{ref}/database/query
        
        # Alternative: Use PostgREST to create tables
        # But PostgREST doesn't support DDL (CREATE TABLE) operations
        
        # Best approach: Use Supabase Dashboard SQL Editor
        print("\n" + "=" * 70)
        print("RECOMMENDED: Execute SQL via Supabase Dashboard")
        print("=" * 70)
        print("\n1. Go to: https://app.supabase.com")
        print("2. Select your project")
        print("3. Go to: SQL Editor → New query")
        print("4. Copy and paste the SQL from the migration file")
        print("5. Click 'Run'\n")
        
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 70)
    print("Learning Path Schema Setup")
    print("=" * 70)
    
    # Read SQL file
    sql_file = "supabase/migrations/20251201000000_learning_path_schema.sql"
    
    if not os.path.exists(sql_file):
        print(f"❌ SQL file not found: {sql_file}")
        return
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    print(f"\n✅ SQL file loaded: {sql_file}")
    print(f"   Size: {len(sql_content)} characters\n")
    
    # Check credentials
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("❌ SUPABASE_URL and SUPABASE_KEY required in .env")
        print("\nSQL Content (copy to Supabase SQL Editor):")
        print("=" * 70)
        print(sql_content)
        print("=" * 70)
        return
    
    print(f"✅ Supabase URL: {SUPABASE_URL[:40]}...")
    
    # Try to execute
    print("\n🔄 Attempting to execute schema...")
    
    # Since Supabase Python client doesn't support DDL, we'll provide instructions
    execute_via_management_api()
    
    # Show SQL for manual execution
    print("\n" + "=" * 70)
    print("SQL TO EXECUTE (Copy this to Supabase SQL Editor)")
    print("=" * 70)
    print(sql_content)
    print("=" * 70)
    
    print("\n💡 After executing the SQL:")
    print("   1. Run: python populate_lessons.py")
    print("   2. Start bot: python workshop_signup_bot.py")

if __name__ == "__main__":
    main()


