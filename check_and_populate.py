# -*- coding: utf-8 -*-
"""Check existing lessons and try to populate"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Missing credentials")
    exit(1)

print("=" * 70)
print("Checking Lessons Status")
print("=" * 70)

try:
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("✅ Connected to Supabase\n")
    
    # Check existing lessons
    result = client.table("lessons").select("lesson_number,title").order("lesson_number").execute()
    
    if result.data:
        print(f"📚 Found {len(result.data)} existing lessons:")
        for lesson in result.data[:10]:  # Show first 10
            print(f"   - Lesson {lesson['lesson_number']}: {lesson['title'][:60]}")
        if len(result.data) > 10:
            print(f"   ... and {len(result.data) - 10} more")
    else:
        print("📭 No lessons found in database")
        print("\n💡 Run: python populate_lessons.py")
    
    print("\n" + "=" * 70)
    
except Exception as e:
    error_msg = str(e)
    if "getaddrinfo" in error_msg or "11001" in error_msg:
        print("❌ DNS/Network error - cannot connect to Supabase")
        print("   Please check your internet connection")
    else:
        print(f"❌ Error: {error_msg}")


