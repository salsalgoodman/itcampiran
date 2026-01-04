-- اضافه کردن سوالات برای درس‌های ۹ به بعد
-- این فایل را در Supabase SQL Editor اجرا کنید

-- درس 9: فایل‌ها و مدیریت خطا
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای مدیریت خطا از چه دستوری استفاده می‌کنیم؟', 'try/except', '["if", "try/except", "for", "while"]'::jsonb, 'multiple_choice', 'try/except برای مدیریت خطا استفاده می‌شود.'
FROM lessons WHERE lesson_number = 9
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- درس 10: ماژول‌ها و کتابخانه‌ها
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای نصب کتابخانه از چه دستوری استفاده می‌کنیم؟', 'pip install', NULL, 'text', 'pip install برای نصب کتابخانه‌های Python استفاده می‌شود.'
FROM lessons WHERE lesson_number = 10
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- درس 11: برنامه‌نویسی شی‌گرا
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'متد __init__ چه کاری انجام می‌دهد؟', 'مقداردهی اولیه', NULL, 'text', '__init__ متد سازنده است که هنگام ساخت شیء اجرا می‌شود.'
FROM lessons WHERE lesson_number = 11
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- درس 12: مقدمه ربات تلگرام
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای ساخت ربات تلگرام باید به کجا برویم؟', '@BotFather', '["@BotFather", "@Telegram", "@Python", "@Bot"]'::jsonb, 'multiple_choice', '@BotFather ربات رسمی تلگرام برای ساخت ربات است.'
FROM lessons WHERE lesson_number = 12
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- درس 13: دستورات و پیام‌ها
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای ساخت دستور از چه Handler استفاده می‌کنیم؟', 'CommandHandler', '["CommandHandler", "MessageHandler", "CallbackHandler", "QueryHandler"]'::jsonb, 'multiple_choice', 'CommandHandler برای مدیریت دستورات (commands) استفاده می‌شود.'
FROM lessons WHERE lesson_number = 13
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- درس 14: دکمه‌ها و منو
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای مدیریت کلیک روی دکمه inline از چه Handler استفاده می‌کنیم؟', 'CallbackQueryHandler', '["CallbackQueryHandler", "CommandHandler", "MessageHandler", "ButtonHandler"]'::jsonb, 'multiple_choice', 'CallbackQueryHandler برای مدیریت کلیک روی دکمه‌های inline استفاده می‌شود.'
FROM lessons WHERE lesson_number = 14
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- درس 15: ربات کامل با دیتابیس
INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای اتصال به Supabase از چه کتابخانه‌ای استفاده می‌کنیم؟', 'supabase', NULL, 'text', 'کتابخانه supabase برای اتصال به Supabase استفاده می‌شود.'
FROM lessons WHERE lesson_number = 15
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

-- نمایش نتیجه
SELECT 
    l.lesson_number,
    l.title,
    COUNT(q.id) as question_count
FROM lessons l
LEFT JOIN questions q ON q.lesson_id = l.id
WHERE l.lesson_number >= 9
GROUP BY l.lesson_number, l.title
ORDER BY l.lesson_number;

