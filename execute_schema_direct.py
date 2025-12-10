# -*- coding: utf-8 -*-
"""
Execute SQL Schema directly via Supabase REST API
"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()

def execute_sql_direct(sql_content: str) -> bool:
    """Execute SQL via Supabase REST API"""
    try:
        # Supabase doesn't expose a direct SQL execution endpoint via REST API
        # We need to use the Management API or SQL Editor API
        
        # Extract project reference
        if not SUPABASE_URL:
            return False
        
        project_ref = SUPABASE_URL.replace("https://", "").replace("http://", "").split(".")[0]
        
        # Try Management API endpoint
        # Note: This typically requires service role key
        management_api_url = f"https://api.supabase.com/v1/projects/{project_ref}/database/query"
        
        headers = {
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "apikey": SUPABASE_KEY
        }
        
        # Split SQL into statements
        statements = [s.strip() for s in sql_content.split(';') if s.strip() and not s.strip().startswith('--')]
        
        print(f"📋 Found {len(statements)} SQL statements")
        
        # Try executing via PostgREST (won't work for DDL)
        # Or use Supabase Dashboard SQL Editor
        
        # Actually, the best approach is to use psql or Supabase CLI
        # But since we're in Python, let's try the Management API
        
        # Management API requires different authentication
        # Let's try using the project's REST API with RPC
        
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_tables_via_http():
    """Try to create tables using HTTP requests"""
    # Read SQL file
    sql_file = "supabase/migrations/20251201000000_learning_path_schema.sql"
    
    if not os.path.exists(sql_file):
        print(f"❌ SQL file not found: {sql_file}")
        return False
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    print("=" * 70)
    print("Executing Learning Path Schema")
    print("=" * 70)
    
    # Since Supabase REST API doesn't support DDL operations directly,
    # we'll use a workaround: create an RPC function first, then call it
    # OR use the Supabase Dashboard SQL Editor
    
    # For now, let's provide the SQL and instructions
    print("\n⚠️  Direct SQL execution via Python is limited.")
    print("   Supabase REST API doesn't support CREATE TABLE operations.")
    print("\n✅ However, I can help you execute it via Supabase Dashboard:")
    print("\n" + "=" * 70)
    print("SQL CONTENT (Ready to execute)")
    print("=" * 70)
    print(sql_content)
    print("=" * 70)
    
    print("\n📝 Steps to execute:")
    print("1. Open: https://app.supabase.com")
    print("2. Select your project")
    print("3. Go to: SQL Editor → New query")
    print("4. Paste the SQL above")
    print("5. Click 'Run'")
    print("\n✅ After that, run: python populate_lessons.py")
    
    return False

if __name__ == "__main__":
    create_tables_via_http()


