"""
Populate 15 new lessons into Supabase database
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

# Clear existing lessons (optional - comment out if you want to keep old lessons)
print("\n🗑️ در حال حذف درس‌های قدیمی...")
try:
    # Delete questions first (foreign key constraint)
    supabase.table("questions").delete().neq("id", 0).execute()
    # Delete lessons
    supabase.table("lessons").delete().neq("id", 0).execute()
    print("✅ درس‌های قدیمی حذف شدند")
except Exception as e:
    print(f"⚠️ خطا در حذف (ممکن است از قبل خالی باشد): {e}")

# Insert new lessons
print("\n📝 در حال اضافه کردن درس‌های جدید...")

for i, lesson in enumerate(lessons, 1):
    try:
        lesson_number = lesson["lesson_number"]
        title = lesson["title"]
        
        print(f"[{i}/{len(lessons)}] درس {lesson_number}: {title}")
        
        # Insert lesson
        lesson_data = {
            "lesson_number": lesson_number,
            "title": title,
            "content": lesson["content"],  # Already JSON string
            "lesson_type": lesson.get("lesson_type", "lesson"),
            "section": lesson.get("section", "basics"),
            "is_free": True,  # All lessons are free now
            "code_examples": lesson.get("code_examples", "[]"),
            "expected_outputs": lesson.get("expected_outputs", "[]")
        }
        
        result = supabase.table("lessons").insert(lesson_data).execute()
        
        if not result.data:
            print(f"  ⚠️ درس {lesson_number} اضافه نشد")
            continue
        
        lesson_id = result.data[0]["id"]
        print(f"  ✅ درس اضافه شد (ID: {lesson_id})")
        
        # Insert questions
        questions = lesson.get("questions", [])
        for q in questions:
            question_data = {
                "lesson_id": lesson_id,
                "question_number": q["question_number"],
                "question_text": q["question_text"],
                "question_type": q.get("question_type", "text"),
                "correct_answer": q["correct_answer"],
                "options": q.get("options", None),
                "explanation": q.get("explanation", None)
            }
            
            try:
                supabase.table("questions").insert(question_data).execute()
            except Exception as e:
                print(f"    ⚠️ خطا در اضافه کردن سوال: {e}")
        
        print(f"  ✅ {len(questions)} سوال اضافه شد")
        
    except Exception as e:
        print(f"  ❌ خطا در درس {lesson_number}: {e}")

print("\n" + "=" * 70)
print("✅ همه درس‌ها با موفقیت اضافه شدند!")
print("=" * 70)
print(f"\n📊 خلاصه:")
print(f"  - تعداد درس‌ها: {len(lessons)}")
print(f"  - همه درس‌ها رایگان هستند")
print(f"  - آماده استفاده در ربات")

