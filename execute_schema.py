# -*- coding: utf-8 -*-
"""
Execute Supabase schema using REST API
This script will attempt to create tables via Supabase API
"""

import os
import sys
import json
from dotenv import load_dotenv
import httpx

load_dotenv()

def get_sql_statements():
    """Parse SQL file into executable statements"""
    with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove comments and split by semicolon
    statements = []
    current = []
    
    for line in content.split('\n'):
        line = line.strip()
        if not line or line.startswith('--'):
            continue
        current.append(line)
        if line.endswith(';'):
            stmt = ' '.join(current).replace(';', '').strip()
            if stmt:
                statements.append(stmt)
            current = []
    
    return statements

def execute_via_rpc(supabase_url, supabase_key, sql):
    """Execute SQL via RPC (requires custom function)"""
    url = f"{supabase_url}/rest/v1/rpc/exec_sql"
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json"
    }
    data = {"query": sql}
    
    try:
        response = httpx.post(url, headers=headers, json=data, timeout=10)
        return response.status_code == 200, response.text
    except Exception as e:
        return False, str(e)

def create_table_directly(supabase_url, supabase_key, table_name, columns):
    """Create table using Supabase REST API (if supported)"""
    # This is a simplified approach - actual implementation would need
    # to parse CREATE TABLE statements and convert to API calls
    pass

def main():
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    supabase_key = os.environ.get("SUPABASE_KEY", "").strip()
    
    if not supabase_url or not supabase_key:
        print("❌ SUPABASE_URL and SUPABASE_KEY required in .env")
        return
    
    if 'your_' in supabase_url.lower() or 'your_' in supabase_key.lower():
        print("❌ Please configure actual Supabase credentials in .env")
        print("\nThe Supabase Python client doesn't support direct SQL execution.")
        print("You have two options:\n")
        print("OPTION 1: Use Supabase SQL Editor (Easiest)")
        print("-" * 50)
        print("1. Open: https://app.supabase.com")
        print("2. Select your project")
        print("3. Go to SQL Editor → New query")
        print("4. Copy/paste contents of supabase_setup.sql")
        print("5. Click Run\n")
        
        print("OPTION 2: Use Supabase CLI")
        print("-" * 50)
        print("1. Install: npm install -g supabase")
        print("2. Login: supabase login")
        print("3. Link: supabase link --project-ref your-project-ref")
        print("4. Run: supabase db push\n")
        
        # Show the SQL for easy copy
        print("SQL to execute:")
        print("=" * 50)
        with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
            print(f.read())
        print("=" * 50)
        return
    
    print("=" * 60)
    print("Executing Supabase Schema")
    print("=" * 60)
    print(f"URL: {supabase_url[:30]}...")
    print(f"Key: {supabase_key[:20]}...")
    print()
    
    # Test connection
    try:
        from supabase import create_client
        client = create_client(supabase_url, supabase_key)
        print("✅ Connected to Supabase")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # Get SQL statements
    statements = get_sql_statements()
    print(f"📋 Found {len(statements)} SQL statements\n")
    
    # Unfortunately, Supabase Python client doesn't support raw SQL
    # We need to use SQL Editor or create a custom RPC function
    print("⚠️  Direct SQL execution via Python client is not supported.")
    print("   The Supabase Python client is designed for querying, not schema management.\n")
    
    print("Please use one of these methods:")
    print("\n1. SUPABASE SQL EDITOR (Recommended):")
    print("   → https://app.supabase.com → Your Project → SQL Editor")
    print("   → Copy/paste the SQL from supabase_setup.sql")
    print("   → Click 'Run'\n")
    
    print("2. SUPABASE CLI:")
    print("   → supabase db push (if you have CLI set up)\n")
    
    print("3. CUSTOM RPC FUNCTION:")
    print("   → Create an RPC function in Supabase that accepts SQL")
    print("   → Then call it from Python (advanced)\n")
    
    # Display SQL for copy-paste
    print("\n" + "=" * 60)
    print("SQL SCHEMA (Copy this to SQL Editor)")
    print("=" * 60)
    with open('supabase_setup.sql', 'r', encoding='utf-8') as f:
        print(f.read())
    print("=" * 60)

if __name__ == '__main__':
    main()

