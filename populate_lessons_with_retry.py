# -*- coding: utf-8 -*-
"""
Populate lessons with retry mechanism and better error handling
"""

import os
import json
import time
from dotenv import load_dotenv
from supabase import create_client, Client
from lessons_content import get_all_lessons

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env")
    exit(1)

def test_connection(max_retries=3, delay=2):
    """Test Supabase connection with retries"""
    for attempt in range(max_retries):
        try:
            print(f"🔄 Testing connection (attempt {attempt + 1}/{max_retries})...")
            client = create_client(SUPABASE_URL, SUPABASE_KEY)
            # Try a simple query
            result = client.table("lessons").select("id").limit(1).execute()
            print("✅ Connection successful!")
            return client
        except Exception as e:
            error_msg = str(e)
            if "getaddrinfo" in error_msg or "11001" in error_msg:
                print(f"   ⚠️  DNS resolution failed - check internet connection")
            elif "timeout" in error_msg.lower():
                print(f"   ⚠️  Connection timeout")
            else:
                print(f"   ⚠️  Error: {error_msg[:100]}")
            
            if attempt < max_retries - 1:
                print(f"   ⏳ Waiting {delay} seconds before retry...")
                time.sleep(delay)
            else:
                print(f"\n❌ Failed to connect after {max_retries} attempts")
                print("\n💡 Troubleshooting:")
                print("   1. Check your internet connection")
                print("   2. Verify SUPABASE_URL in .env file")
                print("   3. Try accessing https://app.supabase.com in browser")
                print("   4. Check firewall/proxy settings")
                return None
    
    return None

def populate_lessons():
    """Populate lessons table with retry mechanism"""
    # Test connection first
    supabase = test_connection()
    if not supabase:
        return False
    
    lessons = get_all_lessons()
    print(f"\n📚 Found {len(lessons)} lessons to populate\n")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for lesson_data in lessons:
        try:
            # Check if lesson already exists
            existing = supabase.table("lessons").select("id").eq("lesson_number", lesson_data["lesson_number"]).execute()
            
            if existing.data:
                print(f"⏭️  Lesson {lesson_data['lesson_number']} already exists, skipping...")
                lesson_id = existing.data[0]["id"]
                skip_count += 1
            else:
                # Insert lesson
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
                
                result = supabase.table("lessons").insert(lesson_record).execute()
                lesson_id = result.data[0]["id"]
                print(f"✅ Inserted lesson {lesson_data['lesson_number']}: {lesson_data['title'][:50]}...")
                success_count += 1
            
            # Insert questions
            questions = lesson_data.get("questions", [])
            question_success = 0
            for question_data in questions:
                try:
                    # Check if question already exists
                    existing_q = supabase.table("questions").select("id").eq("lesson_id", lesson_id).eq("question_number", question_data["question_number"]).execute()
                    
                    if existing_q.data:
                        continue
                    
                    question_record = {
                        "lesson_id": lesson_id,
                        "question_number": question_data["question_number"],
                        "question_text": question_data["question_text"],
                        "correct_answer": question_data["correct_answer"],
                        "options": json.dumps(question_data.get("options", []), ensure_ascii=False) if question_data.get("options") else None,
                        "question_type": question_data.get("question_type", "text"),
                        "explanation": question_data.get("explanation", "")
                    }
                    
                    supabase.table("questions").insert(question_record).execute()
                    question_success += 1
                except Exception as e:
                    print(f"   ⚠️  Error inserting question {question_data['question_number']}: {str(e)[:50]}")
            
            if question_success > 0:
                print(f"   ✅ Inserted {question_success} questions")
                    
        except Exception as e:
            error_msg = str(e)
            if "getaddrinfo" in error_msg or "11001" in error_msg:
                print(f"❌ DNS error for lesson {lesson_data['lesson_number']} - connection lost")
                error_count += 1
                # Try to reconnect
                supabase = test_connection(max_retries=1, delay=1)
                if not supabase:
                    print("   ❌ Cannot reconnect. Stopping...")
                    break
            else:
                print(f"❌ Error inserting lesson {lesson_data['lesson_number']}: {error_msg[:100]}")
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
        print("\n⚠️  No lessons were inserted. Please check your connection and try again.")
        return False

if __name__ == "__main__":
    print("=" * 70)
    print("Learning Path Lessons Populator")
    print("=" * 70)
    populate_lessons()


