-- Learning Path Database Schema
-- Run this script in Supabase SQL Editor after initial_schema.sql

-- Create lessons table
CREATE TABLE IF NOT EXISTS lessons (
    id SERIAL PRIMARY KEY,
    lesson_number INTEGER UNIQUE NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    lesson_type TEXT NOT NULL DEFAULT 'lesson', -- 'lesson', 'project', 'intro'
    section TEXT NOT NULL, -- 'intro', 'data_types', 'operators', 'functions', 'data_structures', 'methods_libraries', 'ml_theory'
    is_free BOOLEAN NOT NULL DEFAULT true,
    code_examples TEXT, -- JSON string with code examples
    expected_outputs TEXT, -- JSON string with expected outputs
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create questions table
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    lesson_id INTEGER NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    question_number INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    options TEXT, -- JSON array of options (if multiple choice)
    question_type TEXT NOT NULL DEFAULT 'text', -- 'text', 'multiple_choice', 'code'
    explanation TEXT, -- Explanation shown after answering
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(lesson_id, question_number)
);

-- Create user_progress table
CREATE TABLE IF NOT EXISTS user_progress (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    lesson_id INTEGER NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    completed_at TIMESTAMPTZ,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    is_completed BOOLEAN DEFAULT false,
    UNIQUE(telegram_id, lesson_id)
);

-- Create question_answers table
CREATE TABLE IF NOT EXISTS question_answers (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    user_answer TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    answered_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(telegram_id, question_id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_lessons_lesson_number ON lessons(lesson_number);
CREATE INDEX IF NOT EXISTS idx_lessons_section ON lessons(section);
CREATE INDEX IF NOT EXISTS idx_lessons_is_free ON lessons(is_free);
CREATE INDEX IF NOT EXISTS idx_questions_lesson_id ON questions(lesson_id);
CREATE INDEX IF NOT EXISTS idx_user_progress_telegram_id ON user_progress(telegram_id);
CREATE INDEX IF NOT EXISTS idx_user_progress_lesson_id ON user_progress(lesson_id);
CREATE INDEX IF NOT EXISTS idx_question_answers_telegram_id ON question_answers(telegram_id);
CREATE INDEX IF NOT EXISTS idx_question_answers_question_id ON question_answers(question_id);

-- Add comments for documentation
COMMENT ON TABLE lessons IS 'Stores all lesson content for Python learning path';
COMMENT ON TABLE questions IS 'Stores questions for each lesson';
COMMENT ON TABLE user_progress IS 'Tracks user progress through lessons';
COMMENT ON TABLE question_answers IS 'Stores user answers to questions';
COMMENT ON COLUMN lessons.lesson_type IS 'Type: lesson, project, or intro';
COMMENT ON COLUMN lessons.section IS 'Section: intro, data_types, operators, functions, data_structures, methods_libraries, ml_theory';
COMMENT ON COLUMN lessons.is_free IS 'Whether lesson is free (true) or requires payment (false)';
COMMENT ON COLUMN questions.question_type IS 'Type: text, multiple_choice, or code';


