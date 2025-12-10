# -*- coding: utf-8 -*-
"""
Generate SQL INSERT statements for all lessons
This can be run directly in Supabase SQL Editor
"""

import json
from lessons_content import get_all_lessons

def escape_sql_string(s):
    """Escape single quotes for SQL"""
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

def generate_sql():
    """Generate SQL INSERT statements"""
    lessons = get_all_lessons()
    
    sql_statements = []
    sql_statements.append("-- Learning Path Lessons SQL")
    sql_statements.append("-- Run this in Supabase SQL Editor")
    sql_statements.append("-- This will insert all lessons and questions\n")
    
    sql_statements.append("BEGIN;\n")
    
    for lesson_data in lessons:
        # Insert lesson
        lesson_number = lesson_data["lesson_number"]
        title = escape_sql_string(lesson_data["title"])
        content = escape_sql_string(json.dumps(lesson_data["content"], ensure_ascii=False))
        lesson_type = escape_sql_string(lesson_data["lesson_type"])
        section = escape_sql_string(lesson_data["section"])
        is_free = "true" if lesson_data["is_free"] else "false"
        code_examples = escape_sql_string(json.dumps(lesson_data.get("code_examples", []), ensure_ascii=False))
        expected_outputs = escape_sql_string(json.dumps(lesson_data.get("expected_outputs", []), ensure_ascii=False))
        
        sql_statements.append(f"""
-- Lesson {lesson_number}: {lesson_data['title']}
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES ({lesson_number}, {title}, {content}, {lesson_type}, {section}, {is_free}, {code_examples}, {expected_outputs})
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;
""")
        
        # Insert questions
        questions = lesson_data.get("questions", [])
        for q_data in questions:
            question_number = q_data["question_number"]
            question_text = escape_sql_string(q_data["question_text"])
            correct_answer = escape_sql_string(q_data["correct_answer"])
            options = escape_sql_string(json.dumps(q_data.get("options", []), ensure_ascii=False)) if q_data.get("options") else "NULL"
            question_type = escape_sql_string(q_data.get("question_type", "text"))
            explanation = escape_sql_string(q_data.get("explanation", ""))
            
            sql_statements.append(f"""
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, {question_number}, {question_text}, {correct_answer}, {options}, {question_type}, {explanation}
FROM lessons WHERE lesson_number = {lesson_number}
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;
""")
    
    sql_statements.append("COMMIT;")
    
    return "\n".join(sql_statements)

if __name__ == "__main__":
    print("Generating SQL file...")
    sql_content = generate_sql()
    
    output_file = "insert_lessons.sql"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sql_content)
    
    print(f"✅ SQL file generated: {output_file}")
    print(f"📊 Contains {len(get_all_lessons())} lessons")
    print("\n📝 Next steps:")
    print("1. Go to: https://app.supabase.com")
    print("2. Select your project")
    print("3. Go to: SQL Editor → New query")
    print(f"4. Open {output_file} and copy all content")
    print("5. Paste in SQL Editor and click 'Run'")
    print("\n✅ This will insert all lessons and questions automatically!")


