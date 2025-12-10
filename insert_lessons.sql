-- Learning Path Lessons SQL
-- Run this in Supabase SQL Editor
-- This will insert all lessons and questions

BEGIN;


-- Lesson 0: مقدمه: تفاوت PyCharm، Notepad و Jupyter Notebook
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (0, 'مقدمه: تفاوت PyCharm، Notepad و Jupyter Notebook', '["🎓 **درس 0: انتخاب محیط برنامه‌نویسی**\n\nسلام! قبل از شروع یادگیری پایتون، باید با محیط‌های مختلف برنامه‌نویسی آشنا شویم.\n\n**1. Notepad (دفترچه یادداشت)**\n- یک ویرایشگر متن ساده\n- ❌ هیچ ویژگی خاصی برای برنامه‌نویسی ندارد\n- ❌ خطاها را نشان نمی‌دهد\n- ❌ کد را اجرا نمی‌کند\n- فقط برای نوشتن متن ساده مناسب است\n\n**2. PyCharm**\n- یک IDE (محیط توسعه یکپارچه) حرفه‌ای\n- ✅ خطاها را قبل از اجرا نشان می‌دهد\n- ✅ پیشنهادات کد می‌دهد\n- ✅ مدیریت پروژه‌های بزرگ\n- ❌ برای مبتدیان پیچیده است\n- ❌ نیاز به نصب و تنظیمات دارد\n\n**3. Jupyter Notebook**\n- بهترین انتخاب برای یادگیری! 🎯\n- ✅ کد را به صورت بخش‌بخش اجرا می‌کند\n- ✅ خروجی هر بخش را جداگانه نشان می‌دهد\n- ✅ می‌توانید توضیحات فارسی بنویسید\n- ✅ برای یادگیری و آزمایش عالی است\n- ✅ رایگان و ساده\n\n**چرا Jupyter Notebook؟**\nدر این دوره از Jupyter Notebook استفاده می‌کنیم چون:\n- یادگیری را آسان‌تر می‌کند\n- می‌توانید کد را خط به خط تست کنید\n- خروجی هر بخش را فوراً می‌بینید\n- برای پروژه‌های علمی و داده‌کاوی عالی است", "📦 **نصب Jupyter Notebook با CMD**\n\nحالا بیایید Jupyter Notebook را نصب کنیم:\n\n**مرحله 1: باز کردن Command Prompt**\n- کلید Windows + R را بزنید\n- `cmd` را تایپ کنید و Enter بزنید\n- یا در منوی Start، \"Command Prompt\" را جستجو کنید\n\n**مرحله 2: بررسی نصب Python**\nدر CMD تایپ کنید:\n```\npython --version\n```\nاگر Python نصب نیست، از python.org دانلود کنید.\n\n**مرحله 3: نصب Jupyter**\nدر CMD تایپ کنید:\n```\npip install jupyter\n```\nصبر کنید تا نصب کامل شود (چند دقیقه طول می‌کشد)\n\n**مرحله 4: اجرای Jupyter**\nدر CMD تایپ کنید:\n```\njupyter notebook\n```\nیک صفحه مرورگر باز می‌شود - این Jupyter Notebook شماست!\n\n**نکته مهم:** \n- CMD را نبندید (باید باز بماند)\n- برای بستن Jupyter، در CMD کلید Ctrl+C را بزنید\n\n**تست نصب:**\nدر Jupyter Notebook، یک سلول جدید بسازید و بنویسید:\n```python\nprint(\"سلام دنیا!\")\n```\nسپس Shift+Enter بزنید. باید \"سلام دنیا!\" را ببینید! 🎉"]', 'intro', 'intro', true, '["print(''سلام دنیا!'')"]', '["سلام دنیا!"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'کدام محیط برای یادگیری پایتون بهتر است؟', 'Jupyter Notebook', '["Notepad", "PyCharm", "Jupyter Notebook", "Word"]', 'multiple_choice', 'Jupyter Notebook بهترین انتخاب برای یادگیری است چون کد را بخش‌بخش اجرا می‌کند و خروجی را فوراً نشان می‌دهد.'
FROM lessons WHERE lesson_number = 0
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'برای نصب Jupyter Notebook چه دستوری باید در CMD تایپ کنیم؟', 'pip install jupyter', NULL, 'text', 'دستور pip install jupyter برای نصب Jupyter Notebook استفاده می‌شود.'
FROM lessons WHERE lesson_number = 0
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, 'برای اجرای Jupyter Notebook چه دستوری باید تایپ کنیم؟', 'jupyter notebook', NULL, 'text', 'دستور jupyter notebook برای اجرای Jupyter Notebook استفاده می‌شود.'
FROM lessons WHERE lesson_number = 0
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 1: انواع داده‌ها (Data Types) - بخش 1: Integer و String
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (1, 'انواع داده‌ها (Data Types) - بخش 1: Integer و String', '["📚 **درس 1: انواع داده‌ها - Integer و String**\n\nدر پایتون، هر داده یک نوع دارد. بیایید با دو نوع مهم شروع کنیم:\n\n**1. Integer (عدد صحیح)**\nاعداد صحیح بدون اعشار هستند:\n```python\nage = 25\ncount = 100\ntemperature = -10\n```\n\n**2. String (رشته متنی)**\nمتن‌ها که بین علامت نقل‌قول قرار می‌گیرند:\n```python\nname = \"علی\"\nmessage = ''سلام''\ntext = \"این یک متن است\"\n```\n\n**مثال عملی:**\n```python\n# Integer\nmy_age = 20\nprint(my_age)\nprint(type(my_age))  # نوع داده را نشان می‌دهد\n\n# String\nmy_name = \"سارا\"\nprint(my_name)\nprint(type(my_name))\n```\n\n**خروجی:**\n```\n20\n<class ''int''>\nسارا\n<class ''str''>\n```\n\n**نکات مهم:**\n- Integer برای محاسبات ریاضی استفاده می‌شود\n- String برای متن و کلمات استفاده می‌شود\n- String باید بین \" یا '' قرار بگیرد\n- Integer نیازی به علامت نقل‌قول ندارد"]', 'lesson', 'data_types', true, '["age = 25\nprint(age)\nprint(type(age))", "name = ''علی''\nprint(name)\nprint(type(name))"]', '["25\n<class ''int''>", "علی\n<class ''str''>"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'کدام یک Integer است؟', '25', '["\"25\"", "25", "''25''", "25.0"]', 'multiple_choice', '25 یک Integer است چون عدد صحیح است و بین علامت نقل‌قول نیست.'
FROM lessons WHERE lesson_number = 1
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کدام یک String است؟', '"سلام"', '["\"سلام\"", "123", "45.6", "سلام"]', 'multiple_choice', '"سلام" یک String است چون بین علامت نقل‌قول قرار دارد.'
FROM lessons WHERE lesson_number = 1
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, 'کد زیر چه خروجی می‌دهد؟
```python
x = 10
print(type(x))```', '<class ''int''>', NULL, 'text', 'عدد 10 یک Integer است، پس type آن int خواهد بود.'
FROM lessons WHERE lesson_number = 1
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 2: انواع داده‌ها - بخش 2: Float و Boolean
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (2, 'انواع داده‌ها - بخش 2: Float و Boolean', '["📚 **درس 2: Float و Boolean**\n\n**3. Float (عدد اعشاری)**\nاعداد با اعشار:\n```python\nprice = 19.99\npi = 3.14\nheight = 175.5\n```\n\n**4. Boolean (درست/غلط)**\nفقط دو مقدار دارد: True یا False\n```python\nis_student = True\nis_adult = False\nhas_car = True\n```\n\n**مثال عملی:**\n```python\n# Float\nprice = 29.99\nprint(price)\nprint(type(price))\n\n# Boolean\nis_active = True\nprint(is_active)\nprint(type(is_active))\n\n# مقایسه Boolean\nage = 20\nis_adult = age >= 18\nprint(is_adult)  # True\n```\n\n**خروجی:**\n```\n29.99\n<class ''float''>\nTrue\n<class ''bool''>\nTrue\n```\n\n**نکات مهم:**\n- Float برای اعداد اعشاری استفاده می‌شود\n- Boolean برای شرایط True/False استفاده می‌شود\n- True و False باید با حرف بزرگ شروع شوند\n- Boolean از مقایسه‌ها به دست می‌آید"]', 'lesson', 'data_types', true, '["price = 19.99\nprint(type(price))", "is_student = True\nprint(is_student)\nprint(type(is_student))"]', '["<class ''float''>", "True\n<class ''bool''>"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'کدام یک Float است؟', '10.5', '["10", "10.5", "\"10.5\"", "True"]', 'multiple_choice', '10.5 یک Float است چون عدد اعشاری است.'
FROM lessons WHERE lesson_number = 2
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'Boolean چند مقدار دارد؟', '2', '["1", "2", "3", "بی‌نهایت"]', 'multiple_choice', 'Boolean فقط دو مقدار دارد: True و False.'
FROM lessons WHERE lesson_number = 2
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, 'کد زیر چه خروجی می‌دهد؟
```python
x = 5 > 3
print(x)```', 'True', NULL, 'text', '5 بزرگتر از 3 است، پس نتیجه True می‌شود.'
FROM lessons WHERE lesson_number = 2
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 3: تبدیل انواع داده‌ها (Type Conversion)
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (3, 'تبدیل انواع داده‌ها (Type Conversion)', '["🔄 **درس 3: تبدیل انواع داده‌ها**\n\nگاهی باید یک نوع داده را به نوع دیگر تبدیل کنیم:\n\n**تبدیل‌های ممکن:**\n```python\n# String به Integer\nage_str = \"25\"\nage_int = int(age_str)\nprint(age_int)  # 25\n\n# Integer به String\nage = 25\nage_str = str(age)\nprint(age_str)  # \"25\"\n\n# Integer به Float\nnum = 10\nnum_float = float(num)\nprint(num_float)  # 10.0\n\n# Float به Integer (اعشار حذف می‌شود)\nprice = 19.99\nprice_int = int(price)\nprint(price_int)  # 19\n```\n\n**تبدیل‌های غیرممکن:**\n```python\n# این کار نمی‌کند!\ntext = \"سلام\"\nnumber = int(text)  # ❌ خطا می‌دهد\n\n# این هم نمی‌کند!\ntext2 = \"abc\"\nnumber2 = float(text2)  # ❌ خطا می‌دهد\n```\n\n**مثال عملی:**\n```python\n# دریافت ورودی از کاربر (همیشه String است)\nuser_input = input(\"سن خود را وارد کنید: \")\n# فرض کنید کاربر \"20\" وارد کرده\n\n# تبدیل به Integer\nage = int(user_input)\nnext_year = age + 1\nprint(f\"سال بعد {next_year} ساله می‌شوید\")\n\n# ترکیب String و Integer\nmessage = \"سن شما: \" + str(age)\nprint(message)\n```\n\n**خروجی:**\n```\nسال بعد 21 ساله می‌شوید\nسن شما: 20\n```\n\n**نکات مهم:**\n- int() برای تبدیل به Integer\n- str() برای تبدیل به String\n- float() برای تبدیل به Float\n- فقط اعداد قابل تبدیل به Integer/Float هستند"]', 'lesson', 'data_types', true, '["age_str = ''25''\nage = int(age_str)\nprint(age + 5)", "num = 10\nnum_str = str(num)\nprint(''عدد: '' + num_str)"]', '["30", "عدد: 10"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای تبدیل ''25'' به عدد، چه تابعی استفاده می‌شود؟', 'int', NULL, 'text', 'تابع int() برای تبدیل String به Integer استفاده می‌شود.'
FROM lessons WHERE lesson_number = 3
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کد زیر چه خروجی می‌دهد؟
```python
x = int(''10'')
print(x + 5)```', '15', NULL, 'text', '''10'' به 10 تبدیل می‌شود و 10 + 5 = 15 می‌شود.'
FROM lessons WHERE lesson_number = 3
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, 'کدام تبدیل غیرممکن است؟', 'int(''abc'')', '["int(''25'')", "str(25)", "int(''abc'')", "float(''10.5'')"]', 'multiple_choice', 'تبدیل ''abc'' به Integer غیرممکن است چون ''abc'' یک عدد نیست.'
FROM lessons WHERE lesson_number = 3
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 4: عملگرها و عملیات - بخش 1: عملگرهای ریاضی
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (4, 'عملگرها و عملیات - بخش 1: عملگرهای ریاضی', '["➕ **درس 4: عملگرهای ریاضی**\n\nپایتون عملگرهای ریاضی مختلفی دارد:\n\n**عملگرهای اصلی:**\n```python\n# جمع (+)\nresult = 10 + 5\nprint(result)  # 15\n\n# تفریق (-)\nresult = 10 - 5\nprint(result)  # 5\n\n# ضرب (*)\nresult = 10 * 5\nprint(result)  # 50\n\n# تقسیم (/)\nresult = 10 / 5\nprint(result)  # 2.0\n\n# تقسیم صحیح (//) - فقط قسمت صحیح\nresult = 10 // 3\nprint(result)  # 3\n\n# باقیمانده (%)\nresult = 10 % 3\nprint(result)  # 1\n\n# توان (**)\nresult = 2 ** 3\nprint(result)  # 8\n```\n\n**مثال عملی:**\n```python\n# محاسبه قیمت با تخفیف\nprice = 100000\ndiscount = 20\nfinal_price = price - (price * discount / 100)\nprint(f\"قیمت نهایی: {final_price} تومان\")\n\n# بررسی زوج یا فرد بودن\nnumber = 15\nis_even = number % 2 == 0\nprint(f\"زوج است؟ {is_even}\")  # False\n```\n\n**خروجی:**\n```\nقیمت نهایی: 80000.0 تومان\nزوج است؟ False\n```\n\n**نکات مهم:**\n- / همیشه Float برمی‌گرداند\n- // فقط قسمت صحیح را برمی‌گرداند\n- % باقیمانده تقسیم را می‌دهد\n- ** برای توان استفاده می‌شود"]', 'lesson', 'operators', true, '["result = 10 + 5 * 2\nprint(result)", "remainder = 17 % 5\nprint(remainder)"]', '["20", "2"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, '10 // 3 چه مقداری دارد؟', '3', NULL, 'text', '// تقسیم صحیح است، پس 10 تقسیم بر 3 می‌شود 3 (بدون اعشار).'
FROM lessons WHERE lesson_number = 4
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, '10 % 3 چه مقداری دارد؟', '1', NULL, 'text', '% باقیمانده تقسیم است، پس 10 تقسیم بر 3 می‌شود 3 باقیمانده 1.'
FROM lessons WHERE lesson_number = 4
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, '2 ** 4 چه مقداری دارد؟', '16', NULL, 'text', '** توان است، پس 2 به توان 4 می‌شود 16.'
FROM lessons WHERE lesson_number = 4
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 5: عملگرها - بخش 2: عملگرهای مقایسه و انتساب
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (5, 'عملگرها - بخش 2: عملگرهای مقایسه و انتساب', '["⚖️ **درس 5: عملگرهای مقایسه و انتساب**\n\n**عملگرهای مقایسه:**\n```python\n# مساوی (==)\nprint(5 == 5)  # True\nprint(5 == 3)  # False\n\n# نامساوی (!=)\nprint(5 != 3)  # True\nprint(5 != 5)  # False\n\n# بزرگتر (>)\nprint(5 > 3)  # True\nprint(3 > 5)  # False\n\n# کوچکتر (<)\nprint(3 < 5)  # True\nprint(5 < 3)  # False\n\n# بزرگتر یا مساوی (>=)\nprint(5 >= 5)  # True\nprint(5 >= 3)  # True\n\n# کوچکتر یا مساوی (<=)\nprint(3 <= 5)  # True\nprint(5 <= 3)  # False\n```\n\n**عملگرهای انتساب:**\n```python\n# انتساب ساده (=)\nx = 10\n\n# جمع و انتساب (+=)\nx += 5  # معادل x = x + 5\nprint(x)  # 15\n\n# تفریق و انتساب (-=)\nx -= 3  # معادل x = x - 3\nprint(x)  # 12\n\n# ضرب و انتساب (*=)\nx *= 2  # معادل x = x * 2\nprint(x)  # 24\n```\n\n**مثال عملی:**\n```python\n# بررسی سن\nage = 20\nis_adult = age >= 18\ncan_vote = age >= 18\nprint(f\"بزرگسال است؟ {is_adult}\")\n\n# شمارنده\ncount = 0\ncount += 1  # count = 1\ncount += 1  # count = 2\nprint(f\"تعداد: {count}\")\n```\n\n**خروجی:**\n```\nبزرگسال است؟ True\nتعداد: 2\n```\n\n**نکات مهم:**\n- == برای مقایسه (نه =)\n- = برای انتساب مقدار\n- != یعنی نامساوی\n- عملگرهای انتساب کوتاه‌تر هستند"]', 'lesson', 'operators', true, '["x = 10\nx += 5\nprint(x)", "age = 20\nis_adult = age >= 18\nprint(is_adult)"]', '["15", "True"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'کدام عملگر برای مقایسه استفاده می‌شود؟', '==', '["=", "==", "===", "="]', 'multiple_choice', '== برای مقایسه استفاده می‌شود، = برای انتساب است.'
FROM lessons WHERE lesson_number = 5
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کد زیر چه خروجی می‌دهد؟
```python
x = 5
x += 3
print(x)```', '8', NULL, 'text', 'x += 3 معادل x = x + 3 است، پس 5 + 3 = 8.'
FROM lessons WHERE lesson_number = 5
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, '10 != 10 چه مقداری دارد؟', 'False', NULL, 'text', '10 مساوی 10 است، پس != False می‌شود.'
FROM lessons WHERE lesson_number = 5
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 6: ورودی از کاربر (Input) و متغیرها
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (6, 'ورودی از کاربر (Input) و متغیرها', '["⌨️ **درس 6: Input و متغیرها**\n\n**تابع input():**\nبرای دریافت ورودی از کاربر استفاده می‌شود:\n```python\nname = input(\"نام خود را وارد کنید: \")\nprint(f\"سلام {name}!\")\n```\n\n**نکته مهم:** input() همیشه String برمی‌گرداند!\n\n**تبدیل ورودی:**\n```python\n# دریافت عدد از کاربر\nage_str = input(\"سن خود را وارد کنید: \")\nage = int(age_str)  # تبدیل به Integer\nprint(f\"سال بعد {age + 1} ساله می‌شوید\")\n\n# یا به صورت کوتاه:\nage = int(input(\"سن خود را وارد کنید: \"))\n```\n\n**متغیرها:**\n```python\n# تعریف متغیر\nname = \"علی\"\nage = 20\nis_student = True\n\n# تغییر مقدار\nage = 21  # مقدار جدید\n\n# استفاده از متغیرها\nprint(f\"نام: {name}, سن: {age}\")\n```\n\n**مثال عملی:**\n```python\n# دریافت اطلاعات از کاربر\nname = input(\"نام شما: \")\nage = int(input(\"سن شما: \"))\ncity = input(\"شهر شما: \")\n\n# نمایش اطلاعات\nprint(f\"\nاطلاعات شما:\")\nprint(f\"نام: {name}\")\nprint(f\"سن: {age}\")\nprint(f\"شهر: {city}\")\nprint(f\"سال تولد: {1403 - age}\")\n```\n\n**خروجی (اگر کاربر وارد کند: علی، 25، تهران):**\n```\nاطلاعات شما:\nنام: علی\nسن: 25\nشهر: تهران\nسال تولد: 1378\n```\n\n**نکات مهم:**\n- input() همیشه String برمی‌گرداند\n- برای اعداد باید تبدیل کنیم\n- متغیرها می‌توانند تغییر کنند\n- نام متغیر باید معنادار باشد"]', 'lesson', 'operators', true, '["name = input(''نام: '')\nprint(f''سلام {name}'')", "age = int(input(''سن: ''))\nprint(f''سال بعد: {age + 1}'')"]', '["سلام [نام وارد شده]", "سال بعد: [سن + 1]"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'input() چه نوع داده‌ای برمی‌گرداند؟', 'String', '["Integer", "Float", "String", "Boolean"]', 'multiple_choice', 'input() همیشه String برمی‌گرداند، حتی اگر عدد وارد شود.'
FROM lessons WHERE lesson_number = 6
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'برای دریافت عدد از کاربر چه باید کرد؟', 'int(input())', NULL, 'text', 'باید input() را با int() تبدیل کنیم تا String به Integer تبدیل شود.'
FROM lessons WHERE lesson_number = 6
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 3, 'کد زیر چه مشکلی دارد؟
```python
age = input(''سن: '')
next_age = age + 1```', 'age یک String است و نمی‌توان با عدد جمع کرد', NULL, 'text', 'input() String برمی‌گرداند، باید با int() تبدیل کنیم.'
FROM lessons WHERE lesson_number = 6
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 7: پروژه ترکیبی 1: ماشین حساب ساده
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (7, 'پروژه ترکیبی 1: ماشین حساب ساده', '["🎯 **پروژه 1: ماشین حساب ساده**\n\nبیایید یک ماشین حساب ساده بسازیم که:\n1. دو عدد از کاربر بگیرد\n2. عملگر را بگیرد\n3. نتیجه را نمایش دهد\n\n**کد کامل:**\n```python\n# دریافت اعداد از کاربر\nnum1 = float(input(\"عدد اول را وارد کنید: \"))\nnum2 = float(input(\"عدد دوم را وارد کنید: \"))\n\n# دریافت عملگر\noperator = input(\"عملگر را وارد کنید (+, -, *, /): \")\n\n# انجام محاسبه\nif operator == \"+\":\n    result = num1 + num2\nelif operator == \"-\":\n    result = num1 - num2\nelif operator == \"*\":\n    result = num1 * num2\nelif operator == \"/\":\n    if num2 != 0:\n        result = num1 / num2\n    else:\n        result = \"خطا: تقسیم بر صفر!\"\nelse:\n    result = \"عملگر نامعتبر!\"\n\n# نمایش نتیجه\nprint(f\"نتیجه: {result}\")\n```\n\n**مثال اجرا:**\n```\nعدد اول را وارد کنید: 10\nعدد دوم را وارد کنید: 5\nعملگر را وارد کنید (+, -, *, /): +\nنتیجه: 15.0\n```\n\n**چالش:**\n- بررسی کنید که عدد دوم برای تقسیم صفر نباشد\n- پیام خطای مناسب نمایش دهید\n- از توابع int() و float() به درستی استفاده کنید"]', 'project', 'operators', true, '["num1 = float(input(''عدد اول: ''))\nnum2 = float(input(''عدد دوم: ''))\noperator = input(''عملگر: '')\nif operator == ''+'':\n    print(num1 + num2)"]', '["[نتیجه محاسبه]"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'چرا از float() به جای int() استفاده کردیم؟', 'برای پشتیبانی از اعداد اعشاری', NULL, 'text', 'float() هم اعداد صحیح و هم اعشاری را می‌پذیرد.'
FROM lessons WHERE lesson_number = 7
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'چرا باید تقسیم بر صفر را بررسی کنیم؟', 'تقسیم بر صفر خطا می‌دهد', NULL, 'text', 'تقسیم بر صفر در پایتون خطا می‌دهد، باید بررسی کنیم.'
FROM lessons WHERE lesson_number = 7
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 8: توابع تبدیل نوع - int(), str(), float()
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (8, 'توابع تبدیل نوع - int(), str(), float()', '["🔧 **درس 8: توابع تبدیل نوع**\n\nما قبلاً با این توابع آشنا شدیم، حالا بیشتر یاد می‌گیریم:\n\n**int() - تبدیل به عدد صحیح:**\n```python\n# String به Integer\nage = int(\"25\")\nprint(age)  # 25\n\n# Float به Integer (اعشار حذف می‌شود)\nprice = int(19.99)\nprint(price)  # 19\n\n# Boolean به Integer\nprint(int(True))   # 1\nprint(int(False))  # 0\n```\n\n**str() - تبدیل به رشته:**\n```python\n# Integer به String\nage = str(25)\nprint(f\"سن: {age}\")  # سن: 25\n\n# Float به String\nprice = str(19.99)\nprint(f\"قیمت: {price}\")  # قیمت: 19.99\n\n# Boolean به String\nprint(str(True))   # \"True\"\n```\n\n**float() - تبدیل به عدد اعشاری:**\n```python\n# Integer به Float\nnum = float(10)\nprint(num)  # 10.0\n\n# String به Float\nprice = float(\"19.99\")\nprint(price)  # 19.99\n```\n\n**مثال عملی:**\n```python\n# دریافت ورودی و تبدیل\nuser_input = input(\"عدد را وارد کنید: \")\nnumber = int(user_input)\ndouble = number * 2\nprint(f\"دو برابر: {double}\")\n\n# ترکیب انواع\nage = 25\nmessage = \"سن شما: \" + str(age) + \" سال\"\nprint(message)\n```\n\n**خروجی:**\n```\nدو برابر: [عدد * 2]\nسن شما: 25 سال\n```\n\n**نکات مهم:**\n- int() اعشار را حذف می‌کند\n- str() هر چیزی را به متن تبدیل می‌کند\n- float() همیشه اعشار دارد"]', 'lesson', 'functions', true, '["age = int(''25'')\nprint(age + 5)", "price = float(''19.99'')\nprint(price * 2)"]', '["30", "39.98"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'int(19.99) چه مقداری دارد؟', '19', NULL, 'text', 'int() اعشار را حذف می‌کند، پس 19.99 می‌شود 19.'
FROM lessons WHERE lesson_number = 8
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'str(25) + str(10) چه مقداری دارد؟', '''2510''', NULL, 'text', 'str() اعداد را به رشته تبدیل می‌کند و + رشته‌ها را به هم می‌چسباند.'
FROM lessons WHERE lesson_number = 8
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 9: شرط if و else
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (9, 'شرط if و else', '["🔀 **درس 9: شرط if و else**\n\nشرط‌ها برای تصمیم‌گیری در برنامه استفاده می‌شوند:\n\n**if ساده:**\n```python\nage = 20\nif age >= 18:\n    print(\"بزرگسال هستید\")\n```\n\n**if و else:**\n```python\nage = 15\nif age >= 18:\n    print(\"بزرگسال هستید\")\nelse:\n    print(\"نوجوان هستید\")\n```\n\n**if، elif و else:**\n```python\nscore = 85\nif score >= 90:\n    print(\"عالی\")\nelif score >= 70:\n    print(\"خوب\")\nelif score >= 50:\n    print(\"قابل قبول\")\nelse:\n    print(\"نیاز به تلاش بیشتر\")\n```\n\n**مثال عملی:**\n```python\n# بررسی سن\nage = int(input(\"سن خود را وارد کنید: \"))\nif age >= 18:\n    print(\"شما می‌توانید رای دهید\")\n    if age >= 65:\n        print(\"شما بازنشسته هستید\")\nelse:\n    print(\"شما هنوز نوجوان هستید\")\n```\n\n**خروجی (اگر 20 وارد شود):**\n```\nشما می‌توانید رای دهید\n```\n\n**نکات مهم:**\n- بعد از if باید : بگذارید\n- کد داخل if باید indent (فاصله) داشته باشد\n- elif برای چند شرط استفاده می‌شود\n- else برای حالت پیش‌فرض است"]', 'lesson', 'functions', true, '["age = 20\nif age >= 18:\n    print(''بزرگسال'')\nelse:\n    print(''نوجوان'')", "score = 85\nif score >= 90:\n    print(''عالی'')\nelif score >= 70:\n    print(''خوب'')"]', '["بزرگسال", "خوب"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'بعد از if چه علامتی باید بگذاریم؟', ':', NULL, 'text', 'بعد از if باید : بگذاریم تا پایتون بداند شرط تمام شده.'
FROM lessons WHERE lesson_number = 9
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کد زیر چه خروجی می‌دهد؟
```python
x = 10
if x > 5:
    print(''بزرگ'')
else:
    print(''کوچک'')```', 'بزرگ', NULL, 'text', '10 بزرگتر از 5 است، پس شرط True می‌شود و ''بزرگ'' چاپ می‌شود.'
FROM lessons WHERE lesson_number = 9
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 10: Try و Except - مدیریت خطا
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (10, 'Try و Except - مدیریت خطا', '["⚠️ **درس 10: Try و Except**\n\nگاهی کد ما خطا می‌دهد. با try/except می‌توانیم خطاها را مدیریت کنیم:\n\n**ساختار try/except:**\n```python\ntry:\n    # کدی که ممکن است خطا بدهد\n    number = int(input(\"عدد را وارد کنید: \"))\n    result = 10 / number\n    print(f\"نتیجه: {result}\")\nexcept:\n    # اگر خطا داد، این قسمت اجرا می‌شود\n    print(\"خطا! لطفاً عدد معتبر وارد کنید\")\n```\n\n**انواع خطاها:**\n```python\ntry:\n    age = int(input(\"سن: \"))\n    print(f\"سن شما: {age}\")\nexcept ValueError:\n    print(\"خطا: باید عدد وارد کنید\")\nexcept ZeroDivisionError:\n    print(\"خطا: تقسیم بر صفر!\")\nexcept Exception as e:\n    print(f\"خطای ناشناخته: {e}\")\n```\n\n**مثال عملی:**\n```python\n# دریافت عدد با مدیریت خطا\nwhile True:\n    try:\n        age = int(input(\"سن خود را وارد کنید: \"))\n        if age > 0:\n            print(f\"سن شما: {age}\")\n            break\n        else:\n            print(\"سن باید مثبت باشد\")\n    except ValueError:\n        print(\"لطفاً یک عدد معتبر وارد کنید\")\n```\n\n**خروجی (اگر ''abc'' وارد شود):**\n```\nلطفاً یک عدد معتبر وارد کنید\n```\n\n**نکات مهم:**\n- try: کدی که ممکن است خطا بدهد\n- except: کدی که در صورت خطا اجرا می‌شود\n- می‌توانیم نوع خطا را مشخص کنیم\n- Exception برای همه خطاها است"]', 'lesson', 'functions', true, '["try:\n    x = int(''abc'')\nexcept:\n    print(''خطا'')", "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(''تقسیم بر صفر'')"]', '["خطا", "تقسیم بر صفر"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'try/except برای چه استفاده می‌شود؟', 'مدیریت خطا', NULL, 'text', 'try/except برای مدیریت خطاها و جلوگیری از crash برنامه استفاده می‌شود.'
FROM lessons WHERE lesson_number = 10
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'اگر int(''abc'') خطا بدهد، چه نوع خطایی است؟', 'ValueError', NULL, 'text', 'تبدیل ''abc'' به int خطای ValueError می‌دهد.'
FROM lessons WHERE lesson_number = 10
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 11: حلقه While
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (11, 'حلقه While', '["🔄 **درس 11: حلقه While**\n\nحلقه while تا زمانی که شرط True باشد، تکرار می‌شود:\n\n**ساختار while:**\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n```\n\n**خروجی:**\n```\n0\n1\n2\n3\n4\n```\n\n**مثال عملی:**\n```python\n# دریافت ورودی تا زمانی که معتبر باشد\nwhile True:\n    age = input(\"سن خود را وارد کنید (برای خروج ''q'' بزنید): \")\n    if age == ''q'':\n        break\n    try:\n        age_num = int(age)\n        if age_num > 0:\n            print(f\"سن شما: {age_num}\")\n            break\n        else:\n            print(\"سن باید مثبت باشد\")\n    except ValueError:\n        print(\"لطفاً عدد معتبر وارد کنید\")\n```\n\n**break و continue:**\n```python\n# break: خروج از حلقه\ncount = 0\nwhile count < 10:\n    if count == 5:\n        break  # حلقه متوقف می‌شود\n    print(count)\n    count += 1\n\n# continue: رفتن به دور بعد\ncount = 0\nwhile count < 5:\n    count += 1\n    if count == 3:\n        continue  # دور بعد شروع می‌شود\n    print(count)\n```\n\n**نکات مهم:**\n- while تا زمانی که شرط True باشد ادامه می‌دهد\n- باید شرط را تغییر دهیم وگرنه حلقه بی‌نهایت می‌شود\n- break برای خروج از حلقه\n- continue برای رد کردن دور فعلی"]', 'lesson', 'functions', true, '["count = 0\nwhile count < 3:\n    print(count)\n    count += 1", "x = 0\nwhile x < 5:\n    x += 1\n    if x == 3:\n        continue\n    print(x)"]', '["0\n1\n2", "1\n2\n4\n5"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'while تا چه زمانی ادامه می‌دهد؟', 'تا زمانی که شرط True باشد', NULL, 'text', 'while تا زمانی که شرط True باشد، کد را تکرار می‌کند.'
FROM lessons WHERE lesson_number = 11
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'break چه کاری می‌کند؟', 'خروج از حلقه', NULL, 'text', 'break حلقه را متوقف می‌کند و از آن خارج می‌شود.'
FROM lessons WHERE lesson_number = 11
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 12: حلقه For
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (12, 'حلقه For', '["🔁 **درس 12: حلقه For**\n\nحلقه for برای تکرار روی یک دنباله استفاده می‌شود:\n\n**for با range():**\n```python\n# تکرار از 0 تا 4\nfor i in range(5):\n    print(i)\n```\n\n**خروجی:**\n```\n0\n1\n2\n3\n4\n```\n\n**range() با شروع و پایان:**\n```python\n# از 1 تا 5\nfor i in range(1, 6):\n    print(i)\n```\n\n**range() با گام:**\n```python\n# از 0 تا 10 با گام 2\nfor i in range(0, 11, 2):\n    print(i)\n# خروجی: 0, 2, 4, 6, 8, 10\n```\n\n**for روی String:**\n```python\nname = \"علی\"\nfor char in name:\n    print(char)\n# خروجی: ع، ل، ی\n```\n\n**مثال عملی:**\n```python\n# جمع اعداد از 1 تا 10\ntotal = 0\nfor i in range(1, 11):\n    total += i\nprint(f\"جمع: {total}\")  # 55\n\n# چاپ جدول ضرب 5\nfor i in range(1, 11):\n    print(f\"5 × {i} = {5 * i}\")\n```\n\n**نکات مهم:**\n- for برای تکرار روی دنباله‌ها استفاده می‌شود\n- range(5) یعنی 0 تا 4\n- range(1, 6) یعنی 1 تا 5\n- range(0, 11, 2) یعنی از 0 تا 10 با گام 2"]', 'lesson', 'functions', true, '["for i in range(3):\n    print(i)", "total = 0\nfor i in range(1, 6):\n    total += i\nprint(total)"]', '["0\n1\n2", "15"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'range(5) چه اعدادی تولید می‌کند؟', '0, 1, 2, 3, 4', NULL, 'text', 'range(5) از 0 شروع می‌شود و تا 4 ادامه می‌دهد.'
FROM lessons WHERE lesson_number = 12
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'range(1, 6) چه اعدادی تولید می‌کند؟', '1, 2, 3, 4, 5', NULL, 'text', 'range(1, 6) از 1 شروع می‌شود و تا 5 ادامه می‌دهد.'
FROM lessons WHERE lesson_number = 12
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 13: تعریف تابع - def
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (13, 'تعریف تابع - def', '["📝 **درس 13: تعریف تابع با def**\n\nتابع یک بلوک کد قابل استفاده مجدد است:\n\n**تعریف تابع ساده:**\n```python\ndef greet():\n    print(\"سلام!\")\n    print(\"خوش آمدید\")\n\n# فراخوانی تابع\ngreet()\n```\n\n**تابع با پارامتر:**\n```python\ndef greet(name):\n    print(f\"سلام {name}!\")\n\ngreet(\"علی\")  # سلام علی!\ngreet(\"سارا\")  # سلام سارا!\n```\n\n**تابع با چند پارامتر:**\n```python\ndef add(a, b):\n    result = a + b\n    print(f\"جمع: {result}\")\n\nadd(5, 3)  # جمع: 8\n```\n\n**مثال عملی:**\n```python\n# تابع محاسبه مساحت مستطیل\ndef rectangle_area(width, height):\n    area = width * height\n    return area\n\n# استفاده از تابع\narea1 = rectangle_area(5, 10)\narea2 = rectangle_area(3, 7)\nprint(f\"مساحت اول: {area1}\")  # 50\nprint(f\"مساحت دوم: {area2}\")  # 21\n```\n\n**نکات مهم:**\n- def برای تعریف تابع استفاده می‌شود\n- بعد از def باید : بگذاریم\n- پارامترها در پرانتز قرار می‌گیرند\n- تابع را با نام آن فراخوانی می‌کنیم"]', 'lesson', 'functions', true, '["def greet(name):\n    print(f''سلام {name}'')\ngreet(''علی'')", "def add(a, b):\n    return a + b\nresult = add(5, 3)\nprint(result)"]', '["سلام علی", "8"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'برای تعریف تابع چه کلمه کلیدی استفاده می‌شود؟', 'def', NULL, 'text', 'def کلمه کلیدی برای تعریف تابع در پایتون است.'
FROM lessons WHERE lesson_number = 13
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کد زیر چه خروجی می‌دهد؟
```python
def multiply(x, y):
    return x * y
print(multiply(3, 4))```', '12', NULL, 'text', 'تابع multiply دو عدد را ضرب می‌کند: 3 * 4 = 12.'
FROM lessons WHERE lesson_number = 13
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 14: Return در توابع
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (14, 'Return در توابع', '["↩️ **درس 14: Return در توابع**\n\nreturn برای برگرداندن مقدار از تابع استفاده می‌شود:\n\n**تابع بدون return:**\n```python\ndef greet(name):\n    print(f\"سلام {name}!\")\n\nresult = greet(\"علی\")\nprint(result)  # None\n```\n\n**تابع با return:**\n```python\ndef add(a, b):\n    return a + b\n\nresult = add(5, 3)\nprint(result)  # 8\n```\n\n**return چند مقدار:**\n```python\ndef calculate(a, b):\n    sum_result = a + b\n    product = a * b\n    return sum_result, product\n\nsum_val, prod_val = calculate(5, 3)\nprint(f\"جمع: {sum_val}, ضرب: {prod_val}\")\n```\n\n**return زودرس:**\n```python\ndef check_age(age):\n    if age < 0:\n        return \"سن نامعتبر\"\n    if age < 18:\n        return \"نوجوان\"\n    return \"بزرگسال\"\n\nprint(check_age(20))  # بزرگسال\nprint(check_age(15))  # نوجوان\n```\n\n**مثال عملی:**\n```python\n# تابع محاسبه میانگین\ndef average(numbers):\n    if len(numbers) == 0:\n        return 0\n    total = sum(numbers)\n    return total / len(numbers)\n\nscores = [85, 90, 78, 92]\navg = average(scores)\nprint(f\"میانگین: {avg}\")\n```\n\n**نکات مهم:**\n- return مقدار را برمی‌گرداند\n- می‌توانیم چند مقدار برگردانیم\n- return فوراً تابع را تمام می‌کند\n- اگر return نباشد، تابع None برمی‌گرداند"]', 'lesson', 'functions', true, '["def multiply(x, y):\n    return x * y\nprint(multiply(4, 5))", "def get_info():\n    return ''علی'', 25\nname, age = get_info()\nprint(f''{name}: {age}'')"]', '["20", "علی: 25"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'return چه کاری می‌کند؟', 'مقدار را از تابع برمی‌گرداند', NULL, 'text', 'return مقدار را از تابع برمی‌گرداند و تابع را تمام می‌کند.'
FROM lessons WHERE lesson_number = 14
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'اگر تابع return نداشته باشد، چه برمی‌گرداند؟', 'None', NULL, 'text', 'اگر تابع return نداشته باشد، به طور پیش‌فرض None برمی‌گرداند.'
FROM lessons WHERE lesson_number = 14
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 15: پروژه ترکیبی 2: بازی حدس عدد
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (15, 'پروژه ترکیبی 2: بازی حدس عدد', '["🎮 **پروژه 2: بازی حدس عدد**\n\nبیایید یک بازی حدس عدد بسازیم:\n1. برنامه یک عدد تصادفی انتخاب می‌کند\n2. کاربر باید آن را حدس بزند\n3. برنامه می‌گوید بزرگتر یا کوچکتر است\n\n**کد کامل:**\n```python\nimport random\n\ndef guess_number_game():\n    # انتخاب عدد تصادفی بین 1 تا 100\n    secret_number = random.randint(1, 100)\n    attempts = 0\n    \n    print(\"بازی حدس عدد!\")\n    print(\"یک عدد بین 1 تا 100 انتخاب شده است.\")\n    \n    while True:\n        try:\n            guess = int(input(\"حدس خود را وارد کنید: \"))\n            attempts += 1\n            \n            if guess < secret_number:\n                print(\"بزرگتر!\")\n            elif guess > secret_number:\n                print(\"کوچکتر!\")\n            else:\n                print(f\"🎉 درست حدس زدید! در {attempts} تلاش\")\n                break\n        except ValueError:\n            print(\"لطفاً عدد معتبر وارد کنید\")\n\n# اجرای بازی\nguess_number_game()\n```\n\n**چالش:**\n- محدودیت تعداد تلاش اضافه کنید\n- پیام‌های تشویقی اضافه کنید\n- امتیازدهی بر اساس تعداد تلاش"]', 'project', 'functions', true, '["import random\nsecret = random.randint(1, 10)\nguess = int(input(''حدس: ''))\nif guess == secret:\n    print(''درست!'')\nelse:\n    print(''غلط!'')"]', '["[بسته به حدس کاربر]"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'random.randint(1, 100) چه کاری می‌کند؟', 'یک عدد تصادفی بین 1 تا 100 برمی‌گرداند', NULL, 'text', 'randint یک عدد تصادفی در بازه مشخص شده برمی‌گرداند.'
FROM lessons WHERE lesson_number = 15
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 16: لیست (List) - بخش 1: مقدمه و روش‌های پایه
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (16, 'لیست (List) - بخش 1: مقدمه و روش‌های پایه', '["📋 **درس 16: لیست (List)**\n\nلیست یک ساختار داده برای ذخیره چند مقدار است:\n\n**ایجاد لیست:**\n```python\n# لیست خالی\nmy_list = []\n\n# لیست با مقادیر\nnumbers = [1, 2, 3, 4, 5]\nnames = [\"علی\", \"سارا\", \"رضا\"]\nmixed = [1, \"علی\", 3.14, True]\n```\n\n**دسترسی به عناصر:**\n```python\nnumbers = [10, 20, 30, 40, 50]\nprint(numbers[0])  # 10 (اولین عنصر)\nprint(numbers[2])  # 30 (سومین عنصر)\nprint(numbers[-1])  # 50 (آخرین عنصر)\n```\n\n**تغییر عناصر:**\n```python\nnumbers = [1, 2, 3]\nnumbers[0] = 10\nprint(numbers)  # [10, 2, 3]\n```\n\n**مثال عملی:**\n```python\n# لیست نمرات\nscores = [85, 90, 78, 92, 88]\nprint(f\"اولین نمره: {scores[0]}\")\nprint(f\"آخرین نمره: {scores[-1]}\")\n\n# تغییر نمره\nscores[2] = 85\nprint(f\"نمرات جدید: {scores}\")\n```\n\n**خروجی:**\n```\nاولین نمره: 85\nآخرین نمره: 88\nنمرات جدید: [85, 90, 85, 92, 88]\n```\n\n**نکات مهم:**\n- لیست‌ها با [] ساخته می‌شوند\n- اندیس از 0 شروع می‌شود\n- می‌توانند انواع مختلف داده داشته باشند\n- قابل تغییر هستند (mutable)"]', 'lesson', 'data_structures', true, '["numbers = [1, 2, 3, 4, 5]\nprint(numbers[0])\nprint(numbers[-1])", "names = [''علی'', ''سارا'']\nnames[0] = ''رضا''\nprint(names)"]', '["1\n5", "[''رضا'', ''سارا'']"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'numbers[0] به کدام عنصر دسترسی دارد؟', 'اولین عنصر', NULL, 'text', 'اندیس 0 به اولین عنصر لیست اشاره می‌کند.'
FROM lessons WHERE lesson_number = 16
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'numbers[-1] به کدام عنصر دسترسی دارد؟', 'آخرین عنصر', NULL, 'text', 'اندیس منفی از انتها شمارش می‌کند، -1 آخرین عنصر است.'
FROM lessons WHERE lesson_number = 16
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 17: لیست - بخش 2: متدهای append، insert، remove
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (17, 'لیست - بخش 2: متدهای append، insert، remove', '["🔧 **درس 17: متدهای لیست**\n\n**append() - اضافه کردن به انتها:**\n```python\nnumbers = [1, 2, 3]\nnumbers.append(4)\nprint(numbers)  # [1, 2, 3, 4]\n```\n\n**insert() - اضافه کردن در موقعیت خاص:**\n```python\nnumbers = [1, 2, 3]\nnumbers.insert(1, 10)  # در موقعیت 1، عدد 10 را اضافه کن\nprint(numbers)  # [1, 10, 2, 3]\n```\n\n**remove() - حذف مقدار:**\n```python\nnumbers = [1, 2, 3, 2]\nnumbers.remove(2)  # اولین 2 را حذف می‌کند\nprint(numbers)  # [1, 3, 2]\n```\n\n**pop() - حذف و برگرداندن:**\n```python\nnumbers = [1, 2, 3]\nlast = numbers.pop()  # آخرین عنصر را حذف و برمی‌گرداند\nprint(last)  # 3\nprint(numbers)  # [1, 2]\n```\n\n**مثال عملی:**\n```python\n# لیست خرید\nshopping = []\nshopping.append(\"نان\")\nshopping.append(\"شیر\")\nshopping.insert(1, \"تخم مرغ\")\nprint(f\"لیست: {shopping}\")\n\nshopping.remove(\"شیر\")\nprint(f\"بعد از حذف: {shopping}\")\n```\n\n**خروجی:**\n```\nلیست: [''نان'', ''تخم مرغ'', ''شیر'']\nبعد از حذف: [''نان'', ''تخم مرغ'']\n```\n\n**نکات مهم:**\n- append() به انتها اضافه می‌کند\n- insert() در موقعیت خاص اضافه می‌کند\n- remove() مقدار را حذف می‌کند\n- pop() عنصر را حذف و برمی‌گرداند"]', 'lesson', 'data_structures', true, '["numbers = [1, 2, 3]\nnumbers.append(4)\nprint(numbers)", "numbers = [1, 2, 3]\nnumbers.insert(1, 10)\nprint(numbers)"]', '["[1, 2, 3, 4]", "[1, 10, 2, 3]"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'append() چه کاری می‌کند؟', 'مقدار را به انتهای لیست اضافه می‌کند', NULL, 'text', 'append() یک عنصر را به انتهای لیست اضافه می‌کند.'
FROM lessons WHERE lesson_number = 17
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کد زیر چه خروجی می‌دهد؟
```python
numbers = [1, 2, 3]
numbers.insert(0, 10)
print(numbers)```', '[10, 1, 2, 3]', NULL, 'text', 'insert(0, 10) عدد 10 را در ابتدای لیست اضافه می‌کند.'
FROM lessons WHERE lesson_number = 17
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 18: لیست - بخش 3: لیست‌های تو در تو و map/filter/zip
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (18, 'لیست - بخش 3: لیست‌های تو در تو و map/filter/zip', '["🔗 **درس 18: لیست‌های پیشرفته**\n\n**لیست‌های تو در تو (Nested Lists):**\n```python\nmatrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nprint(matrix[0][1])  # 2 (ردیف اول، ستون دوم)\n```\n\n**map() - اعمال تابع روی همه عناصر:**\n```python\nnumbers = [1, 2, 3, 4]\ndoubled = list(map(lambda x: x * 2, numbers))\nprint(doubled)  # [2, 4, 6, 8]\n```\n\n**filter() - فیلتر کردن:**\n```python\nnumbers = [1, 2, 3, 4, 5, 6]\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(evens)  # [2, 4, 6]\n```\n\n**zip() - ترکیب لیست‌ها:**\n```python\nnames = [\"علی\", \"سارا\"]\nages = [25, 30]\ncombined = list(zip(names, ages))\nprint(combined)  # [(''علی'', 25), (''سارا'', 30)]\n```\n\n**مثال عملی:**\n```python\n# تبدیل درجه به فارنهایت\ncelsius = [0, 10, 20, 30]\nfahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))\nprint(f\"فارنهایت: {fahrenheit}\")\n\n# فیلتر اعداد مثبت\nnumbers = [-5, 2, -1, 8, -3, 10]\npositive = list(filter(lambda x: x > 0, numbers))\nprint(f\"مثبت‌ها: {positive}\")\n```\n\n**خروجی:**\n```\nفارنهایت: [32.0, 50.0, 68.0, 86.0]\nمثبت‌ها: [2, 8, 10]\n```\n\n**نکات مهم:**\n- لیست‌های تو در تو برای ماتریس استفاده می‌شوند\n- map() تابع را روی همه عناصر اعمال می‌کند\n- filter() عناصری که شرط دارند را برمی‌گرداند\n- zip() لیست‌ها را جفت می‌کند"]', 'lesson', 'data_structures', true, '["matrix = [[1, 2], [3, 4]]\nprint(matrix[0][1])", "numbers = [1, 2, 3]\ndoubled = list(map(lambda x: x*2, numbers))\nprint(doubled)"]', '["2", "[2, 4, 6]"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'map() چه کاری می‌کند؟', 'تابع را روی همه عناصر لیست اعمال می‌کند', NULL, 'text', 'map() یک تابع را روی همه عناصر یک لیست اعمال می‌کند.'
FROM lessons WHERE lesson_number = 18
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'filter() چه کاری می‌کند؟', 'عناصری که شرط دارند را برمی‌گرداند', NULL, 'text', 'filter() فقط عناصری را که شرط را برآورده می‌کنند برمی‌گرداند.'
FROM lessons WHERE lesson_number = 18
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 19: Tuple - ساختار و کاربرد
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (19, 'Tuple - ساختار و کاربرد', '["📌 **درس 19: Tuple**\n\nTuple شبیه لیست است اما قابل تغییر نیست (immutable):\n\n**ایجاد Tuple:**\n```python\n# با پرانتز\nmy_tuple = (1, 2, 3)\n\n# بدون پرانتز (کاما مهم است)\nmy_tuple = 1, 2, 3\n\n# Tuple تک عنصری (باید کاما بگذاریم)\nsingle = (5,)  # نه (5)\n```\n\n**دسترسی به عناصر:**\n```python\ncoordinates = (10, 20)\nx = coordinates[0]  # 10\ny = coordinates[1]  # 20\n```\n\n**Tuple قابل تغییر نیست:**\n```python\nmy_tuple = (1, 2, 3)\n# my_tuple[0] = 10  # ❌ خطا می‌دهد!\n```\n\n**Tuple تو در تو:**\n```python\nnested = ((1, 2), (3, 4))\nprint(nested[0][1])  # 2\n```\n\n**مثال عملی:**\n```python\n# مختصات نقطه\npoint = (5, 10)\nprint(f\"X: {point[0]}, Y: {point[1]}\")\n\n# بازگشت چند مقدار از تابع\ndef get_name_age():\n    return \"علی\", 25\n\nname, age = get_name_age()\nprint(f\"{name}: {age}\")\n```\n\n**خروجی:**\n```\nX: 5, Y: 10\nعلی: 25\n```\n\n**نکات مهم:**\n- Tuple با () ساخته می‌شود\n- قابل تغییر نیست (immutable)\n- برای داده‌های ثابت مناسب است\n- می‌تواند چند مقدار از تابع برگرداند"]', 'lesson', 'data_structures', true, '["point = (10, 20)\nprint(point[0])", "def get_info():\n    return ''علی'', 25\nname, age = get_info()\nprint(name)"]', '["10", "علی"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'Tuple قابل تغییر است؟', 'خیر', '["بله", "خیر", "گاهی", "بستگی دارد"]', 'multiple_choice', 'Tuple قابل تغییر نیست (immutable)، برخلاف لیست.'
FROM lessons WHERE lesson_number = 19
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'تفاوت اصلی Tuple و List چیست؟', 'Tuple قابل تغییر نیست، List قابل تغییر است', NULL, 'text', 'Tuple immutable است و نمی‌توان عناصر آن را تغییر داد، اما List mutable است.'
FROM lessons WHERE lesson_number = 19
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 20: Dictionary - ساختار و کاربرد
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (20, 'Dictionary - ساختار و کاربرد', '["📖 **درس 20: Dictionary**\n\nDictionary برای ذخیره داده‌ها به صورت کلید-مقدار استفاده می‌شود:\n\n**ایجاد Dictionary:**\n```python\n# خالی\nmy_dict = {}\n\n# با مقادیر\nstudent = {\n    \"name\": \"علی\",\n    \"age\": 25,\n    \"city\": \"تهران\"\n}\n```\n\n**دسترسی به مقادیر:**\n```python\nstudent = {\"name\": \"علی\", \"age\": 25}\nprint(student[\"name\"])  # علی\nprint(student.get(\"age\"))  # 25\nprint(student.get(\"phone\", \"ندارد\"))  # ندارد (مقدار پیش‌فرض)\n```\n\n**تغییر و اضافه کردن:**\n```python\nstudent = {\"name\": \"علی\"}\nstudent[\"age\"] = 25  # تغییر یا اضافه\nstudent[\"city\"] = \"تهران\"\nprint(student)  # {''name'': ''علی'', ''age'': 25, ''city'': ''تهران''}\n```\n\n**حذف:**\n```python\nstudent = {\"name\": \"علی\", \"age\": 25}\ndel student[\"age\"]\n# یا\nstudent.pop(\"name\")\n```\n\n**مثال عملی:**\n```python\n# اطلاعات دانشجو\nstudent = {\n    \"name\": \"سارا\",\n    \"age\": 20,\n    \"scores\": [85, 90, 88]\n}\n\nprint(f\"نام: {student[''name'']}\")\nprint(f\"میانگین: {sum(student[''scores'']) / len(student[''scores''])}\")\n```\n\n**خروجی:**\n```\nنام: سارا\nمیانگین: 87.66666666666667\n```\n\n**نکات مهم:**\n- Dictionary با {} ساخته می‌شود\n- کلید-مقدار ذخیره می‌کند\n- کلیدها باید یکتا باشند\n- برای داده‌های ساختاریافته مناسب است"]', 'lesson', 'data_structures', true, '["student = {''name'': ''علی'', ''age'': 25}\nprint(student[''name''])", "student = {''name'': ''علی''}\nstudent[''age''] = 25\nprint(student)"]', '["علی", "{''name'': ''علی'', ''age'': 25}"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'Dictionary با چه علامتی ساخته می‌شود؟', '{}', NULL, 'text', 'Dictionary با {} ساخته می‌شود و شامل جفت‌های کلید-مقدار است.'
FROM lessons WHERE lesson_number = 20
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'کد زیر چه خروجی می‌دهد؟
```python
d = {''a'': 1, ''b'': 2}
print(d.get(''c'', 0))```', '0', NULL, 'text', 'get() اگر کلید وجود نداشته باشد، مقدار پیش‌فرض (0) را برمی‌گرداند.'
FROM lessons WHERE lesson_number = 20
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 21: Dictionary - تو در تو و Set
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (21, 'Dictionary - تو در تو و Set', '["🔗 **درس 21: Dictionary تو در تو و Set**\n\n**Dictionary تو در تو:**\n```python\nstudents = {\n    \"علی\": {\n        \"age\": 25,\n        \"scores\": [85, 90]\n    },\n    \"سارا\": {\n        \"age\": 20,\n        \"scores\": [92, 88]\n    }\n}\n\nprint(students[\"علی\"][\"age\"])  # 25\nprint(students[\"سارا\"][\"scores\"][0])  # 92\n```\n\n**Set - مجموعه بدون تکرار:**\n```python\n# ایجاد Set\nmy_set = {1, 2, 3, 3, 4}  # تکرار حذف می‌شود\nprint(my_set)  # {1, 2, 3, 4}\n\n# اضافه کردن\nmy_set.add(5)\nprint(my_set)  # {1, 2, 3, 4, 5}\n\n# حذف\nmy_set.remove(3)\nprint(my_set)  # {1, 2, 4, 5}\n```\n\n**عملیات Set:**\n```python\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\n\n# اجتماع (union)\nunion = set1 | set2  # {1, 2, 3, 4, 5}\n\n# اشتراک (intersection)\nintersection = set1 & set2  # {3}\n\n# تفاضل (difference)\ndifference = set1 - set2  # {1, 2}\n```\n\n**مثال عملی:**\n```python\n# حذف تکرارها از لیست\nnumbers = [1, 2, 2, 3, 3, 4]\nunique = list(set(numbers))\nprint(unique)  # [1, 2, 3, 4]\n\n# بررسی عضویت\nfruits = {\"سیب\", \"موز\", \"پرتقال\"}\nprint(\"سیب\" in fruits)  # True\n```\n\n**نکات مهم:**\n- Dictionary می‌تواند تو در تو باشد\n- Set تکرار ندارد\n- Set برای عملیات مجموعه‌ای مناسب است\n- Set با {} ساخته می‌شود اما خالی نیست"]', 'lesson', 'data_structures', true, '["students = {''علی'': {''age'': 25}}\nprint(students[''علی''][''age''])", "my_set = {1, 2, 2, 3}\nprint(my_set)"]', '["25", "{1, 2, 3}"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'Set چه ویژگی دارد؟', 'تکرار ندارد', NULL, 'text', 'Set به طور خودکار تکرارها را حذف می‌کند.'
FROM lessons WHERE lesson_number = 21
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 2, 'برای حذف تکرار از لیست چه باید کرد؟', 'تبدیل به Set و برگرداندن به لیست', NULL, 'text', 'list(set(numbers)) تکرارها را حذف می‌کند.'
FROM lessons WHERE lesson_number = 21
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;


-- Lesson 22: پروژه ترکیبی 3: مدیریت لیست دانشجویان
INSERT INTO lessons (lesson_number, title, content, lesson_type, section, is_free, code_examples, expected_outputs)
VALUES (22, 'پروژه ترکیبی 3: مدیریت لیست دانشجویان', '["🎯 **پروژه 3: مدیریت لیست دانشجویان**\n\nبیایید یک سیستم مدیریت دانشجویان بسازیم:\n1. اضافه کردن دانشجو\n2. نمایش لیست\n3. جستجو\n4. حذف\n\n**کد کامل:**\n```python\nstudents = []\n\ndef add_student():\n    name = input(\"نام دانشجو: \")\n    age = int(input(\"سن: \"))\n    score = float(input(\"نمره: \"))\n    student = {\n        \"name\": name,\n        \"age\": age,\n        \"score\": score\n    }\n    students.append(student)\n    print(\"دانشجو اضافه شد!\")\n\ndef show_students():\n    if not students:\n        print(\"لیست خالی است\")\n        return\n    for i, student in enumerate(students, 1):\n        print(f\"{i}. {student[''name'']} - سن: {student[''age'']} - نمره: {student[''score'']}\")\n\ndef search_student():\n    name = input(\"نام برای جستجو: \")\n    found = [s for s in students if name.lower() in s[''name''].lower()]\n    if found:\n        for student in found:\n            print(f\"{student[''name'']} - نمره: {student[''score'']}\")\n    else:\n        print(\"یافت نشد\")\n\n# استفاده\nadd_student()\nadd_student()\nshow_students()\nsearch_student()\n```\n\n**چالش:**\n- محاسبه میانگین نمرات\n- مرتب‌سازی بر اساس نمره\n- ذخیره در فایل"]', 'project', 'data_structures', true, '["students = [{''name'': ''علی'', ''score'': 85}]\nfor s in students:\n    print(s[''name''])"]', '["علی"]')
ON CONFLICT (lesson_number) DO UPDATE SET
    title = EXCLUDED.title,
    content = EXCLUDED.content,
    lesson_type = EXCLUDED.lesson_type,
    section = EXCLUDED.section,
    is_free = EXCLUDED.is_free,
    code_examples = EXCLUDED.code_examples,
    expected_outputs = EXCLUDED.expected_outputs;


INSERT INTO questions (lesson_id, question_number, question_text, correct_answer, options, question_type, explanation)
SELECT id, 1, 'چرا از Dictionary برای دانشجو استفاده کردیم؟', 'برای ذخیره اطلاعات ساختاریافته', NULL, 'text', 'Dictionary برای داده‌های ساختاریافته با کلید-مقدار مناسب است.'
FROM lessons WHERE lesson_number = 22
ON CONFLICT (lesson_id, question_number) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    correct_answer = EXCLUDED.correct_answer,
    options = EXCLUDED.options,
    question_type = EXCLUDED.question_type,
    explanation = EXCLUDED.explanation;

COMMIT;