# -*- coding: utf-8 -*-
"""
Populate lessons using direct REST API calls with retry and error handling
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

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env")
    exit(1)

# Extract the project reference
project_ref = SUPABASE_URL.replace("https://", "").replace("http://", "").split(".")[0]
rest_url = f"{SUPABASE_URL}/rest/v1"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

def make_request(method, endpoint, data=None, max_retries=5, delay=2):
    """Make HTTP request with retry logic"""
    url = f"{rest_url}/{endpoint}"
    
    for attempt in range(max_retries):
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=30)
            elif method == "PATCH":
                response = requests.patch(url, headers=headers, json=data, timeout=30)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            if response.status_code in [200, 201]:
                return True, response.json() if response.content else {}
            elif response.status_code == 409:  # Conflict - already exists
                return True, {"exists": True}
            else:
                error_msg = response.text[:200]
                if attempt < max_retries - 1:
                    print(f"   ⚠️  Attempt {attempt + 1} failed (status {response.status_code}), retrying...")
                    time.sleep(delay * (attempt + 1))  # Exponential backoff
                else:
                    return False, f"HTTP {response.status_code}: {error_msg}"
                    
        except requests.exceptions.ConnectionError as e:
            error_msg = str(e)
            if "getaddrinfo" in error_msg or "11001" in error_msg:
                if attempt < max_retries - 1:
                    wait_time = delay * (attempt + 1)
                    print(f"   ⚠️  DNS error (attempt {attempt + 1}/{max_retries}), waiting {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    return False, "DNS resolution failed - check internet connection"
            else:
                return False, f"Connection error: {error_msg}"
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                print(f"   ⚠️  Timeout (attempt {attempt + 1}/{max_retries}), retrying...")
                time.sleep(delay)
            else:
                return False, "Request timeout"
        except Exception as e:
            return False, str(e)
    
    return False, "Max retries exceeded"

def check_lesson_exists(lesson_number):
    """Check if lesson already exists"""
    endpoint = f"lessons?lesson_number=eq.{lesson_number}&select=id"
    success, result = make_request("GET", endpoint, max_retries=3)
    
    if success and isinstance(result, list) and len(result) > 0:
        return result[0].get("id")
    return None

def insert_lesson(lesson_data):
    """Insert a lesson"""
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
    
    endpoint = "lessons"
    success, result = make_request("POST", endpoint, lesson_record, max_retries=5, delay=3)
    
    if success:
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("id")
        elif isinstance(result, dict) and "id" in result:
            return result["id"]
        elif isinstance(result, dict) and result.get("exists"):
            # Already exists, need to fetch ID
            lesson_id = check_lesson_exists(lesson_data["lesson_number"])
            return lesson_id
    return None

def insert_question(question_data, lesson_id):
    """Insert a question"""
    question_record = {
        "lesson_id": lesson_id,
        "question_number": question_data["question_number"],
        "question_text": question_data["question_text"],
        "correct_answer": question_data["correct_answer"],
        "options": json.dumps(question_data.get("options", []), ensure_ascii=False) if question_data.get("options") else None,
        "question_type": question_data.get("question_type", "text"),
        "explanation": question_data.get("explanation", "")
    }
    
    endpoint = "questions"
    success, result = make_request("POST", endpoint, question_record, max_retries=3)
    return success

def populate_lessons():
    """Main function to populate lessons"""
    print("=" * 70)
    print("Learning Path Lessons Populator (Direct API)")
    print("=" * 70)
    print(f"\n📡 Supabase URL: {SUPABASE_URL[:50]}...")
    print(f"🔑 Using REST API endpoint\n")
    
    # Test connection first
    print("🔄 Testing connection...")
    success, result = make_request("GET", "lessons?select=id&limit=1", max_retries=3)
    
    if not success:
        print(f"❌ Connection test failed: {result}")
        print("\n💡 Troubleshooting:")
        print("   1. Check internet connection")
        print("   2. Verify SUPABASE_URL and SUPABASE_KEY in .env")
        print("   3. Check firewall/proxy settings")
        print("   4. Try accessing Supabase Dashboard in browser")
        return False
    
    print("✅ Connection successful!\n")
    
    lessons = get_all_lessons()
    print(f"📚 Found {len(lessons)} lessons to populate\n")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for idx, lesson_data in enumerate(lessons, 1):
        lesson_num = lesson_data["lesson_number"]
        print(f"[{idx}/{len(lessons)}] Processing lesson {lesson_num}: {lesson_data['title'][:50]}...")
        
        try:
            # Check if exists
            lesson_id = check_lesson_exists(lesson_num)
            
            if lesson_id:
                print(f"   ⏭️  Already exists (ID: {lesson_id}), skipping...")
                skip_count += 1
            else:
                # Insert lesson
                lesson_id = insert_lesson(lesson_data)
                
                if lesson_id:
                    print(f"   ✅ Inserted lesson (ID: {lesson_id})")
                    success_count += 1
                else:
                    print(f"   ❌ Failed to insert lesson")
                    error_count += 1
                    continue
            
            # Insert questions
            questions = lesson_data.get("questions", [])
            question_success = 0
            
            for q_data in questions:
                # Check if question exists
                check_q_endpoint = f"questions?lesson_id=eq.{lesson_id}&question_number=eq.{q_data['question_number']}&select=id"
                q_success, q_result = make_request("GET", check_q_endpoint, max_retries=2)
                
                if q_success and isinstance(q_result, list) and len(q_result) > 0:
                    continue  # Question already exists
                
                if insert_question(q_data, lesson_id):
                    question_success += 1
            
            if question_success > 0:
                print(f"   ✅ Inserted {question_success} questions")
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:100]}")
            error_count += 1
    
    print("\n" + "=" * 70)
    print("📊 Summary:")
    print(f"   ✅ Successfully inserted: {success_count}")
    print(f"   ⏭️  Already existed (skipped): {skip_count}")
    print(f"   ❌ Errors: {error_count}")
    print("=" * 70)
    
    if success_count > 0 or skip_count == len(lessons):
        print("\n🎉 Done! Lessons are ready to use.")
        return True
    else:
        print("\n⚠️  No lessons were inserted. Please check your connection.")
        return False

if __name__ == "__main__":
    populate_lessons()


