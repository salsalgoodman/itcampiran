# -*- coding: utf-8 -*-
"""
Alternative method: Try using subprocess with curl to insert data
"""

import os
import json
import subprocess
from dotenv import load_dotenv
from lessons_content import get_all_lessons

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip().rstrip('/')
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()

def test_curl_connection():
    """Test if curl can connect"""
    test_url = f"{SUPABASE_URL}/rest/v1/lessons?select=id&limit=1"
    
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-X", "GET",
                "-H", f"apikey: {SUPABASE_KEY}",
                "-H", f"Authorization: Bearer {SUPABASE_KEY}",
                test_url
            ],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print("✅ curl connection successful!")
            return True
        else:
            print(f"❌ curl failed: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ curl not found - cannot use this method")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 70)
    print("Testing curl connection...")
    print("=" * 70)
    
    if test_curl_connection():
        print("\n✅ curl works! You can use curl to insert data.")
        print("💡 However, the SQL file method is easier:")
        print("   → Use insert_lessons.sql in Supabase SQL Editor")
    else:
        print("\n💡 Best solution: Use the SQL file")
        print("   1. Open insert_lessons.sql")
        print("   2. Copy all content")
        print("   3. Paste in Supabase SQL Editor")
        print("   4. Click Run")
        print("\n✅ This will insert all 23 lessons automatically!")


