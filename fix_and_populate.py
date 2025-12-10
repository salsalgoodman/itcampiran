# -*- coding: utf-8 -*-
"""
Fix schema cache issue and populate lessons
"""

import os
import json
import time
import requests
from dotenv import load_dotenv
from lessons_content import get_all_lessons

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip().rstrip('/')
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()

rest_url = f"{SUPABASE_URL}/rest/v1"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

def refresh_schema_cache():
    """Try to refresh PostgREST schema cache"""
    # PostgREST doesn't have a direct cache refresh endpoint
    # But we can try accessing the schema endpoint
    try:
        # Try to access the schema endpoint
        schema_url = f"{rest_url}/"
        response = requests.get(schema_url, headers=headers, timeout=10)
        print(f"Schema endpoint status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Schema refresh error: {e}")
        return False

def check_table_exists_direct():
    """Check if table exists by trying to query it"""
    try:
        # Try a simple query
        url = f"{rest_url}/lessons?select=id&limit=1"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ Table exists and is accessible")
            return True
        elif response.status_code == 404 or "PGRST205" in response.text:
            print("❌ Table not found in schema cache")
            print("💡 This might mean:")
            print("   1. Table doesn't exist - run the migration SQL")
            print("   2. Schema cache needs refresh - wait a few minutes")
            print("   3. Permissions issue - check RLS policies")
            return False
        else:
            print(f"⚠️  Status {response.status_code}: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"❌ Error checking table: {e}")
        return False

def insert_lesson_direct(lesson_data):
    """Insert lesson using direct REST API"""
    lesson_record = {
        "lesson_number": lesson_data["lesson_number"],
        "title": lesson_data["title"],
        "content": json.dumps(lesson_data["content"], ensure_ascii=False),
        "lesson_type": lesson_data["lesson_type"],
        "section": lesson_data["section"],
        "is_free": lesson_data["is_free"],
        "code_examples": json.dumps(lesson_data.get("code_examples", []), ensure_ascii=False),
        "expected_outputs": json.dumps(lesson_data.get("expected_outputs", []), ensure_ascii=False)
    }
    
    url = f"{rest_url}/lessons"
    
    try:
        response = requests.post(url, headers=headers, json=lesson_record, timeout=30)
        
        if response.status_code in [200, 201]:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("id")
            return True
        elif response.status_code == 409:
            # Already exists
            return "exists"
        else:
            print(f"   ⚠️  Status {response.status_code}: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}")
        return None

def main():
    print("=" * 70)
    print("Fix Schema Cache and Populate Lessons")
    print("=" * 70)
    
    # Check table
    print("\n🔍 Checking table access...")
    if not check_table_exists_direct():
        print("\n💡 Solution:")
        print("   1. Make sure you ran the migration SQL in Supabase SQL Editor")
        print("   2. Wait 1-2 minutes for schema cache to refresh")
        print("   3. Or use the SQL file method: insert_lessons.sql")
        return
    
    # Try to refresh cache
    print("\n🔄 Attempting to refresh schema cache...")
    refresh_schema_cache()
    time.sleep(2)
    
    # Try inserting lessons
    print("\n📚 Starting to populate lessons...")
    lessons = get_all_lessons()
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for idx, lesson_data in enumerate(lessons[:5], 1):  # Try first 5 as test
        lesson_num = lesson_data["lesson_number"]
        print(f"\n[{idx}/5] Testing lesson {lesson_num}...")
        
        result = insert_lesson_direct(lesson_data)
        
        if result == "exists":
            print(f"   ⏭️  Already exists")
            skip_count += 1
        elif result:
            print(f"   ✅ Inserted (ID: {result})")
            success_count += 1
        else:
            print(f"   ❌ Failed")
            error_count += 1
            break  # Stop on first error
    
    if success_count > 0:
        print(f"\n✅ Test successful! {success_count} lessons inserted.")
        print("💡 Continue with full population? Run: python populate_lessons.py")
    elif skip_count > 0:
        print(f"\n✅ Lessons already exist ({skip_count} found)")
    else:
        print(f"\n❌ Failed to insert. Use SQL file method instead.")

if __name__ == "__main__":
    main()


