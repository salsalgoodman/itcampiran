# -*- coding: utf-8 -*-
"""
Setup Learning Path Tables in Supabase
Attempts to create tables programmatically
"""

import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()

def check_table_exists(supabase: Client, table_name: str) -> bool:
    """Check if a table exists by trying to query it"""
    try:
        # Try to select from table (will fail if doesn't exist)
        result = supabase.table(table_name).select("id").limit(1).execute()
        return True
    except Exception as e:
        # Table doesn't exist or other error
        error_str = str(e).lower()
        if "relation" in error_str and "does not exist" in error_str:
            return False
        # Other error - assume table exists to be safe
        return True

def create_tables_via_sql_editor_api():
    """Try to execute SQL via Supabase SQL Editor API"""
    import requests
    
    # Read SQL file
    sql_file = "supabase/migrations/20251201000000_learning_path_schema.sql"
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # Supabase doesn't expose SQL Editor API publicly
    # We need to use the Dashboard or Management API
    
    print("=" * 70)
    print("Learning Path Schema Setup")
    print("=" * 70)
    print(f"\n✅ Supabase URL: {SUPABASE_URL[:40]}...")
    
    # Connect to Supabase
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Connected to Supabase")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False
    
    # Check if tables already exist
    print("\n🔍 Checking existing tables...")
    tables = ["lessons", "questions", "user_progress", "question_answers"]
    existing_tables = []
    missing_tables = []
    
    for table in tables:
        if check_table_exists(supabase, table):
            print(f"   ✅ Table '{table}' exists")
            existing_tables.append(table)
        else:
            print(f"   ❌ Table '{table}' does not exist")
            missing_tables.append(table)
    
    if not missing_tables:
        print("\n✅ All tables already exist!")
        return True
    
    print(f"\n📋 Need to create {len(missing_tables)} tables:")
    for table in missing_tables:
        print(f"   - {table}")
    
    # Since Supabase Python client doesn't support CREATE TABLE,
    # we need to provide SQL for manual execution
    print("\n" + "=" * 70)
    print("SQL TO EXECUTE (Copy to Supabase SQL Editor)")
    print("=" * 70)
    print(sql_content)
    print("=" * 70)
    
    print("\n📝 Steps:")
    print("1. Go to: https://app.supabase.com")
    print("2. Select your project")
    print("3. Go to: SQL Editor → New query")
    print("4. Paste the SQL above")
    print("5. Click 'Run'")
    print("\n💡 After executing SQL, run: python populate_lessons.py")
    
    return False

if __name__ == "__main__":
    create_tables_via_sql_editor_api()


