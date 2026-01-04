"""
اضافه کردن سوالات گمشده برای درس‌های ۹ به بعد
"""

import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ SUPABASE_URL یا SUPABASE_KEY یافت نشد!")
    exit(1)

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("✅ اتصال به Supabase موفق بود")
except Exception as e:
    print(f"❌ خطا در اتصال: {e}")
    exit(1)

# Import lessons
from lessons_content_new import get_all_lessons

lessons = get_all_lessons()
print(f"\n📚 تعداد درس‌ها: {len(lessons)}")

# فقط درس‌های ۹ به بعد
lessons_to_process = [l for l in lessons if l["lesson_number"] >= 9]
print(f"📝 درس‌های ۹ به بعد: {len(lessons_to_process)} درس\n")

for lesson in lessons_to_process:
    lesson_number = lesson["lesson_number"]
    title = lesson["title"]
    
    print(f"📚 درس {lesson_number}: {title}")
    
    # Get lesson ID from database
    try:
        lesson_result = supabase.table("lessons").select("id").eq("lesson_number", lesson_number).execute()
        if not lesson_result.data:
            print(f"  ⚠️ درس {lesson_number} در دیتابیس یافت نشد!")
            continue
        
        lesson_id = lesson_result.data[0]["id"]
        print(f"  ✅ درس پیدا شد (ID: {lesson_id})")
        
        # Check existing questions
        existing_questions = supabase.table("questions").select("question_number").eq("lesson_id", lesson_id).execute()
        existing_numbers = {q["question_number"] for q in existing_questions.data}
        
        # Insert questions
        questions = lesson.get("questions", [])
        if not questions:
            print(f"  ⚠️ هیچ سوالی در فایل برای این درس وجود ندارد!")
            continue
        
        question_count = 0
        for q in questions:
            question_num = q["question_number"]
            
            # Skip if already exists
            if question_num in existing_numbers:
                print(f"    ⏭️ سوال {question_num} از قبل وجود دارد")
                continue
            
            # Handle options - if it's already a JSON string, use it; otherwise convert
            options = q.get("options", None)
            if options is not None:
                if isinstance(options, str):
                    # Already a JSON string (from json.dumps in lessons_content_new.py)
                    options_json = options
                else:
                    # Convert list/dict to JSON string
                    options_json = json.dumps(options, ensure_ascii=False)
            else:
                options_json = None
            
            question_data = {
                "lesson_id": lesson_id,
                "question_number": question_num,
                "question_text": q["question_text"],
                "question_type": q.get("question_type", "text"),
                "correct_answer": q["correct_answer"],
                "options": options_json,
                "explanation": q.get("explanation", None)
            }
            
            try:
                supabase.table("questions").insert(question_data).execute()
                question_count += 1
                print(f"    ✅ سوال {question_num} اضافه شد")
            except Exception as e:
                print(f"    ❌ خطا در اضافه کردن سوال {question_num}: {e}")
        
        print(f"  ✅ {question_count} سوال جدید اضافه شد (از {len(questions)} سوال)\n")
        
    except Exception as e:
        print(f"  ❌ خطا در پردازش درس {lesson_number}: {e}\n")

print("\n" + "=" * 70)
print("✅ پردازش کامل شد!")
print("=" * 70)

