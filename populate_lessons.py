# -*- coding: utf-8 -*-
"""
Script to populate database with lessons from lessons_content.py
Run this after setting up the database schema
"""

import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from lessons_content import get_all_lessons

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def populate_lessons():
    """Populate lessons table"""
    lessons = get_all_lessons()
    
    print(f"📚 Found {len(lessons)} lessons to populate")
    
    for lesson_data in lessons:
        try:
            # Check if lesson already exists
            existing = supabase.table("lessons").select("id").eq("lesson_number", lesson_data["lesson_number"]).execute()
            
            if existing.data:
                print(f"⏭️  Lesson {lesson_data['lesson_number']} already exists, skipping...")
                lesson_id = existing.data[0]["id"]
            else:
                # Insert lesson
                lesson_record = {
                    "lesson_number": lesson_data["lesson_number"],
                    "title": lesson_data["title"],
                    "content": json.dumps(lesson_data["content"], ensure_ascii=False),  # Store as JSON
                    "lesson_type": lesson_data["lesson_type"],
                    "section": lesson_data["section"],
                    "is_free": lesson_data["is_free"],
                    "code_examples": json.dumps(lesson_data.get("code_examples", []), ensure_ascii=False),
                    "expected_outputs": json.dumps(lesson_data.get("expected_outputs", []), ensure_ascii=False)
                }
                
                result = supabase.table("lessons").insert(lesson_record).execute()
                lesson_id = result.data[0]["id"]
                print(f"✅ Inserted lesson {lesson_data['lesson_number']}: {lesson_data['title']}")
            
            # Insert questions
            questions = lesson_data.get("questions", [])
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
                    print(f"   ✅ Inserted question {question_data['question_number']}")
                except Exception as e:
                    print(f"   ❌ Error inserting question {question_data['question_number']}: {e}")
                    
        except Exception as e:
            print(f"❌ Error inserting lesson {lesson_data['lesson_number']}: {e}")
    
    print("\n🎉 Done populating lessons!")

if __name__ == "__main__":
    populate_lessons()


