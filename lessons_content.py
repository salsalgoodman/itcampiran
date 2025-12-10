# -*- coding: utf-8 -*-
"""
Python Learning Path Content
All lessons in Farsi with examples, questions, and projects
"""

import json
from typing import Dict, List

# Lesson structure: {
#     "lesson_number": int,
#     "title": str,
#     "content": str (can be multiple messages),
#     "lesson_type": "lesson" | "project" | "intro",
#     "section": str,
#     "is_free": bool,
#     "code_examples": List[str],
#     "expected_outputs": List[str],
#     "questions": List[Dict]
# }

LESSONS = []

# ==================== INTRO LESSONS ====================

LESSONS.append({
    "lesson_number": 0,
    "title": "مقدمه: تفاوت PyCharm، Notepad و Jupyter Notebook",
    "content": [
        """🎓 **درس 0: انتخاب محیط برنامه‌نویسی**

سلام! قبل از شروع یادگیری پایتون، باید با محیط‌های مختلف برنامه‌نویسی آشنا شویم.

**1. Notepad (دفترچه یادداشت)**
- یک ویرایشگر متن ساده
- ❌ هیچ ویژگی خاصی برای برنامه‌نویسی ندارد
- ❌ خطاها را نشان نمی‌دهد
- ❌ کد را اجرا نمی‌کند
- فقط برای نوشتن متن ساده مناسب است

**2. PyCharm**
- یک IDE (محیط توسعه یکپارچه) حرفه‌ای
- ✅ خطاها را قبل از اجرا نشان می‌دهد
- ✅ پیشنهادات کد می‌دهد
- ✅ مدیریت پروژه‌های بزرگ
- ❌ برای مبتدیان پیچیده است
- ❌ نیاز به نصب و تنظیمات دارد

**3. Jupyter Notebook**
- بهترین انتخاب برای یادگیری! 🎯
- ✅ کد را به صورت بخش‌بخش اجرا می‌کند
- ✅ خروجی هر بخش را جداگانه نشان می‌دهد
- ✅ می‌توانید توضیحات فارسی بنویسید
- ✅ برای یادگیری و آزمایش عالی است
- ✅ رایگان و ساده

**چرا Jupyter Notebook؟**
در این دوره از Jupyter Notebook استفاده می‌کنیم چون:
- یادگیری را آسان‌تر می‌کند
- می‌توانید کد را خط به خط تست کنید
- خروجی هر بخش را فوراً می‌بینید
- برای پروژه‌های علمی و داده‌کاوی عالی است""",
        
        """📦 **نصب Jupyter Notebook با CMD**

حالا بیایید Jupyter Notebook را نصب کنیم:

**مرحله 1: باز کردن Command Prompt**
- کلید Windows + R را بزنید
- `cmd` را تایپ کنید و Enter بزنید
- یا در منوی Start، "Command Prompt" را جستجو کنید

**مرحله 2: بررسی نصب Python**
در CMD تایپ کنید:
```
python --version
```
اگر Python نصب نیست، از python.org دانلود کنید.

**مرحله 3: نصب Jupyter**
در CMD تایپ کنید:
```
pip install jupyter
```
صبر کنید تا نصب کامل شود (چند دقیقه طول می‌کشد)

**مرحله 4: اجرای Jupyter**
در CMD تایپ کنید:
```
jupyter notebook
```
یک صفحه مرورگر باز می‌شود - این Jupyter Notebook شماست!

**نکته مهم:** 
- CMD را نبندید (باید باز بماند)
- برای بستن Jupyter، در CMD کلید Ctrl+C را بزنید

**تست نصب:**
در Jupyter Notebook، یک سلول جدید بسازید و بنویسید:
```python
print("سلام دنیا!")
```
سپس Shift+Enter بزنید. باید "سلام دنیا!" را ببینید! 🎉"""
    ],
    "lesson_type": "intro",
    "section": "intro",
    "is_free": True,
    "code_examples": [
        "print('سلام دنیا!')"
    ],
    "expected_outputs": [
        "سلام دنیا!"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام محیط برای یادگیری پایتون بهتر است؟",
            "question_type": "multiple_choice",
            "options": ["Notepad", "PyCharm", "Jupyter Notebook", "Word"],
            "correct_answer": "Jupyter Notebook",
            "explanation": "Jupyter Notebook بهترین انتخاب برای یادگیری است چون کد را بخش‌بخش اجرا می‌کند و خروجی را فوراً نشان می‌دهد."
        },
        {
            "question_number": 2,
            "question_text": "برای نصب Jupyter Notebook چه دستوری باید در CMD تایپ کنیم؟",
            "question_type": "text",
            "correct_answer": "pip install jupyter",
            "explanation": "دستور pip install jupyter برای نصب Jupyter Notebook استفاده می‌شود."
        },
        {
            "question_number": 3,
            "question_text": "برای اجرای Jupyter Notebook چه دستوری باید تایپ کنیم؟",
            "question_type": "text",
            "correct_answer": "jupyter notebook",
            "explanation": "دستور jupyter notebook برای اجرای Jupyter Notebook استفاده می‌شود."
        }
    ]
})

# ==================== DATA TYPES LESSONS ====================

LESSONS.append({
    "lesson_number": 1,
    "title": "انواع داده‌ها (Data Types) - بخش 1: Integer و String",
    "content": [
        """📚 **درس 1: انواع داده‌ها - Integer و String**

در پایتون، هر داده یک نوع دارد. بیایید با دو نوع مهم شروع کنیم:

**1. Integer (عدد صحیح)**
اعداد صحیح بدون اعشار هستند:
```python
age = 25
count = 100
temperature = -10
```

**2. String (رشته متنی)**
متن‌ها که بین علامت نقل‌قول قرار می‌گیرند:
```python
name = "علی"
message = 'سلام'
text = "این یک متن است"
```

**مثال عملی:**
```python
# Integer
my_age = 20
print(my_age)
print(type(my_age))  # نوع داده را نشان می‌دهد

# String
my_name = "سارا"
print(my_name)
print(type(my_name))
```

**خروجی:**
```
20
<class 'int'>
سارا
<class 'str'>
```

**نکات مهم:**
- Integer برای محاسبات ریاضی استفاده می‌شود
- String برای متن و کلمات استفاده می‌شود
- String باید بین " یا ' قرار بگیرد
- Integer نیازی به علامت نقل‌قول ندارد"""
    ],
    "lesson_type": "lesson",
    "section": "data_types",
    "is_free": True,
    "code_examples": [
        "age = 25\nprint(age)\nprint(type(age))",
        "name = 'علی'\nprint(name)\nprint(type(name))"
    ],
    "expected_outputs": [
        "25\n<class 'int'>",
        "علی\n<class 'str'>"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام یک Integer است؟",
            "question_type": "multiple_choice",
            "options": ['"25"', "25", "'25'", "25.0"],
            "correct_answer": "25",
            "explanation": "25 یک Integer است چون عدد صحیح است و بین علامت نقل‌قول نیست."
        },
        {
            "question_number": 2,
            "question_text": "کدام یک String است؟",
            "question_type": "multiple_choice",
            "options": ['"سلام"', "123", "45.6", "سلام"],
            "correct_answer": '"سلام"',
            "explanation": '"سلام" یک String است چون بین علامت نقل‌قول قرار دارد.'
        },
        {
            "question_number": 3,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nx = 10\nprint(type(x))```",
            "question_type": "text",
            "correct_answer": "<class 'int'>",
            "explanation": "عدد 10 یک Integer است، پس type آن int خواهد بود."
        }
    ]
})

LESSONS.append({
    "lesson_number": 2,
    "title": "انواع داده‌ها - بخش 2: Float و Boolean",
    "content": [
        """📚 **درس 2: Float و Boolean**

**3. Float (عدد اعشاری)**
اعداد با اعشار:
```python
price = 19.99
pi = 3.14
height = 175.5
```

**4. Boolean (درست/غلط)**
فقط دو مقدار دارد: True یا False
```python
is_student = True
is_adult = False
has_car = True
```

**مثال عملی:**
```python
# Float
price = 29.99
print(price)
print(type(price))

# Boolean
is_active = True
print(is_active)
print(type(is_active))

# مقایسه Boolean
age = 20
is_adult = age >= 18
print(is_adult)  # True
```

**خروجی:**
```
29.99
<class 'float'>
True
<class 'bool'>
True
```

**نکات مهم:**
- Float برای اعداد اعشاری استفاده می‌شود
- Boolean برای شرایط True/False استفاده می‌شود
- True و False باید با حرف بزرگ شروع شوند
- Boolean از مقایسه‌ها به دست می‌آید"""
    ],
    "lesson_type": "lesson",
    "section": "data_types",
    "is_free": True,
    "code_examples": [
        "price = 19.99\nprint(type(price))",
        "is_student = True\nprint(is_student)\nprint(type(is_student))"
    ],
    "expected_outputs": [
        "<class 'float'>",
        "True\n<class 'bool'>"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام یک Float است؟",
            "question_type": "multiple_choice",
            "options": ["10", "10.5", '"10.5"', "True"],
            "correct_answer": "10.5",
            "explanation": "10.5 یک Float است چون عدد اعشاری است."
        },
        {
            "question_number": 2,
            "question_text": "Boolean چند مقدار دارد؟",
            "question_type": "multiple_choice",
            "options": ["1", "2", "3", "بی‌نهایت"],
            "correct_answer": "2",
            "explanation": "Boolean فقط دو مقدار دارد: True و False."
        },
        {
            "question_number": 3,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nx = 5 > 3\nprint(x)```",
            "question_type": "text",
            "correct_answer": "True",
            "explanation": "5 بزرگتر از 3 است، پس نتیجه True می‌شود."
        }
    ]
})

LESSONS.append({
    "lesson_number": 3,
    "title": "تبدیل انواع داده‌ها (Type Conversion)",
    "content": [
        """🔄 **درس 3: تبدیل انواع داده‌ها**

گاهی باید یک نوع داده را به نوع دیگر تبدیل کنیم:

**تبدیل‌های ممکن:**
```python
# String به Integer
age_str = "25"
age_int = int(age_str)
print(age_int)  # 25

# Integer به String
age = 25
age_str = str(age)
print(age_str)  # "25"

# Integer به Float
num = 10
num_float = float(num)
print(num_float)  # 10.0

# Float به Integer (اعشار حذف می‌شود)
price = 19.99
price_int = int(price)
print(price_int)  # 19
```

**تبدیل‌های غیرممکن:**
```python
# این کار نمی‌کند!
text = "سلام"
number = int(text)  # ❌ خطا می‌دهد

# این هم نمی‌کند!
text2 = "abc"
number2 = float(text2)  # ❌ خطا می‌دهد
```

**مثال عملی:**
```python
# دریافت ورودی از کاربر (همیشه String است)
user_input = input("سن خود را وارد کنید: ")
# فرض کنید کاربر "20" وارد کرده

# تبدیل به Integer
age = int(user_input)
next_year = age + 1
print(f"سال بعد {next_year} ساله می‌شوید")

# ترکیب String و Integer
message = "سن شما: " + str(age)
print(message)
```

**خروجی:**
```
سال بعد 21 ساله می‌شوید
سن شما: 20
```

**نکات مهم:**
- int() برای تبدیل به Integer
- str() برای تبدیل به String
- float() برای تبدیل به Float
- فقط اعداد قابل تبدیل به Integer/Float هستند"""
    ],
    "lesson_type": "lesson",
    "section": "data_types",
    "is_free": True,
    "code_examples": [
        "age_str = '25'\nage = int(age_str)\nprint(age + 5)",
        "num = 10\nnum_str = str(num)\nprint('عدد: ' + num_str)"
    ],
    "expected_outputs": [
        "30",
        "عدد: 10"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای تبدیل '25' به عدد، چه تابعی استفاده می‌شود؟",
            "question_type": "text",
            "correct_answer": "int",
            "explanation": "تابع int() برای تبدیل String به Integer استفاده می‌شود."
        },
        {
            "question_number": 2,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nx = int('10')\nprint(x + 5)```",
            "question_type": "text",
            "correct_answer": "15",
            "explanation": "'10' به 10 تبدیل می‌شود و 10 + 5 = 15 می‌شود."
        },
        {
            "question_number": 3,
            "question_text": "کدام تبدیل غیرممکن است؟",
            "question_type": "multiple_choice",
            "options": ["int('25')", "str(25)", "int('abc')", "float('10.5')"],
            "correct_answer": "int('abc')",
            "explanation": "تبدیل 'abc' به Integer غیرممکن است چون 'abc' یک عدد نیست."
        }
    ]
})

# ==================== OPERATORS LESSONS ====================

LESSONS.append({
    "lesson_number": 4,
    "title": "عملگرها و عملیات - بخش 1: عملگرهای ریاضی",
    "content": [
        """➕ **درس 4: عملگرهای ریاضی**

پایتون عملگرهای ریاضی مختلفی دارد:

**عملگرهای اصلی:**
```python
# جمع (+)
result = 10 + 5
print(result)  # 15

# تفریق (-)
result = 10 - 5
print(result)  # 5

# ضرب (*)
result = 10 * 5
print(result)  # 50

# تقسیم (/)
result = 10 / 5
print(result)  # 2.0

# تقسیم صحیح (//) - فقط قسمت صحیح
result = 10 // 3
print(result)  # 3

# باقیمانده (%)
result = 10 % 3
print(result)  # 1

# توان (**)
result = 2 ** 3
print(result)  # 8
```

**مثال عملی:**
```python
# محاسبه قیمت با تخفیف
price = 100000
discount = 20
final_price = price - (price * discount / 100)
print(f"قیمت نهایی: {final_price} تومان")

# بررسی زوج یا فرد بودن
number = 15
is_even = number % 2 == 0
print(f"زوج است؟ {is_even}")  # False
```

**خروجی:**
```
قیمت نهایی: 80000.0 تومان
زوج است؟ False
```

**نکات مهم:**
- / همیشه Float برمی‌گرداند
- // فقط قسمت صحیح را برمی‌گرداند
- % باقیمانده تقسیم را می‌دهد
- ** برای توان استفاده می‌شود"""
    ],
    "lesson_type": "lesson",
    "section": "operators",
    "is_free": True,
    "code_examples": [
        "result = 10 + 5 * 2\nprint(result)",
        "remainder = 17 % 5\nprint(remainder)"
    ],
    "expected_outputs": [
        "20",
        "2"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "10 // 3 چه مقداری دارد؟",
            "question_type": "text",
            "correct_answer": "3",
            "explanation": "// تقسیم صحیح است، پس 10 تقسیم بر 3 می‌شود 3 (بدون اعشار)."
        },
        {
            "question_number": 2,
            "question_text": "10 % 3 چه مقداری دارد؟",
            "question_type": "text",
            "correct_answer": "1",
            "explanation": "% باقیمانده تقسیم است، پس 10 تقسیم بر 3 می‌شود 3 باقیمانده 1."
        },
        {
            "question_number": 3,
            "question_text": "2 ** 4 چه مقداری دارد؟",
            "question_type": "text",
            "correct_answer": "16",
            "explanation": "** توان است، پس 2 به توان 4 می‌شود 16."
        }
    ]
})

LESSONS.append({
    "lesson_number": 5,
    "title": "عملگرها - بخش 2: عملگرهای مقایسه و انتساب",
    "content": [
        """⚖️ **درس 5: عملگرهای مقایسه و انتساب**

**عملگرهای مقایسه:**
```python
# مساوی (==)
print(5 == 5)  # True
print(5 == 3)  # False

# نامساوی (!=)
print(5 != 3)  # True
print(5 != 5)  # False

# بزرگتر (>)
print(5 > 3)  # True
print(3 > 5)  # False

# کوچکتر (<)
print(3 < 5)  # True
print(5 < 3)  # False

# بزرگتر یا مساوی (>=)
print(5 >= 5)  # True
print(5 >= 3)  # True

# کوچکتر یا مساوی (<=)
print(3 <= 5)  # True
print(5 <= 3)  # False
```

**عملگرهای انتساب:**
```python
# انتساب ساده (=)
x = 10

# جمع و انتساب (+=)
x += 5  # معادل x = x + 5
print(x)  # 15

# تفریق و انتساب (-=)
x -= 3  # معادل x = x - 3
print(x)  # 12

# ضرب و انتساب (*=)
x *= 2  # معادل x = x * 2
print(x)  # 24
```

**مثال عملی:**
```python
# بررسی سن
age = 20
is_adult = age >= 18
can_vote = age >= 18
print(f"بزرگسال است؟ {is_adult}")

# شمارنده
count = 0
count += 1  # count = 1
count += 1  # count = 2
print(f"تعداد: {count}")
```

**خروجی:**
```
بزرگسال است؟ True
تعداد: 2
```

**نکات مهم:**
- == برای مقایسه (نه =)
- = برای انتساب مقدار
- != یعنی نامساوی
- عملگرهای انتساب کوتاه‌تر هستند"""
    ],
    "lesson_type": "lesson",
    "section": "operators",
    "is_free": True,
    "code_examples": [
        "x = 10\nx += 5\nprint(x)",
        "age = 20\nis_adult = age >= 18\nprint(is_adult)"
    ],
    "expected_outputs": [
        "15",
        "True"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام عملگر برای مقایسه استفاده می‌شود؟",
            "question_type": "multiple_choice",
            "options": ["=", "==", "===", "="],
            "correct_answer": "==",
            "explanation": "== برای مقایسه استفاده می‌شود، = برای انتساب است."
        },
        {
            "question_number": 2,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nx = 5\nx += 3\nprint(x)```",
            "question_type": "text",
            "correct_answer": "8",
            "explanation": "x += 3 معادل x = x + 3 است، پس 5 + 3 = 8."
        },
        {
            "question_number": 3,
            "question_text": "10 != 10 چه مقداری دارد؟",
            "question_type": "text",
            "correct_answer": "False",
            "explanation": "10 مساوی 10 است، پس != False می‌شود."
        }
    ]
})

LESSONS.append({
    "lesson_number": 6,
    "title": "ورودی از کاربر (Input) و متغیرها",
    "content": [
        """⌨️ **درس 6: Input و متغیرها**

**تابع input():**
برای دریافت ورودی از کاربر استفاده می‌شود:
```python
name = input("نام خود را وارد کنید: ")
print(f"سلام {name}!")
```

**نکته مهم:** input() همیشه String برمی‌گرداند!

**تبدیل ورودی:**
```python
# دریافت عدد از کاربر
age_str = input("سن خود را وارد کنید: ")
age = int(age_str)  # تبدیل به Integer
print(f"سال بعد {age + 1} ساله می‌شوید")

# یا به صورت کوتاه:
age = int(input("سن خود را وارد کنید: "))
```

**متغیرها:**
```python
# تعریف متغیر
name = "علی"
age = 20
is_student = True

# تغییر مقدار
age = 21  # مقدار جدید

# استفاده از متغیرها
print(f"نام: {name}, سن: {age}")
```

**مثال عملی:**
```python
# دریافت اطلاعات از کاربر
name = input("نام شما: ")
age = int(input("سن شما: "))
city = input("شهر شما: ")

# نمایش اطلاعات
print(f"\nاطلاعات شما:")
print(f"نام: {name}")
print(f"سن: {age}")
print(f"شهر: {city}")
print(f"سال تولد: {1403 - age}")
```

**خروجی (اگر کاربر وارد کند: علی، 25، تهران):**
```
اطلاعات شما:
نام: علی
سن: 25
شهر: تهران
سال تولد: 1378
```

**نکات مهم:**
- input() همیشه String برمی‌گرداند
- برای اعداد باید تبدیل کنیم
- متغیرها می‌توانند تغییر کنند
- نام متغیر باید معنادار باشد"""
    ],
    "lesson_type": "lesson",
    "section": "operators",
    "is_free": True,
    "code_examples": [
        "name = input('نام: ')\nprint(f'سلام {name}')",
        "age = int(input('سن: '))\nprint(f'سال بعد: {age + 1}')"
    ],
    "expected_outputs": [
        "سلام [نام وارد شده]",
        "سال بعد: [سن + 1]"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "input() چه نوع داده‌ای برمی‌گرداند؟",
            "question_type": "multiple_choice",
            "options": ["Integer", "Float", "String", "Boolean"],
            "correct_answer": "String",
            "explanation": "input() همیشه String برمی‌گرداند، حتی اگر عدد وارد شود."
        },
        {
            "question_number": 2,
            "question_text": "برای دریافت عدد از کاربر چه باید کرد؟",
            "question_type": "text",
            "correct_answer": "int(input())",
            "explanation": "باید input() را با int() تبدیل کنیم تا String به Integer تبدیل شود."
        },
        {
            "question_number": 3,
            "question_text": "کد زیر چه مشکلی دارد؟\n```python\nage = input('سن: ')\nnext_age = age + 1```",
            "question_type": "text",
            "correct_answer": "age یک String است و نمی‌توان با عدد جمع کرد",
            "explanation": "input() String برمی‌گرداند، باید با int() تبدیل کنیم."
        }
    ]
})

# ==================== PROJECT 1 ====================

LESSONS.append({
    "lesson_number": 7,
    "title": "پروژه ترکیبی 1: ماشین حساب ساده",
    "content": [
        """🎯 **پروژه 1: ماشین حساب ساده**

بیایید یک ماشین حساب ساده بسازیم که:
1. دو عدد از کاربر بگیرد
2. عملگر را بگیرد
3. نتیجه را نمایش دهد

**کد کامل:**
```python
# دریافت اعداد از کاربر
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))

# دریافت عملگر
operator = input("عملگر را وارد کنید (+, -, *, /): ")

# انجام محاسبه
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "خطا: تقسیم بر صفر!"
else:
    result = "عملگر نامعتبر!"

# نمایش نتیجه
print(f"نتیجه: {result}")
```

**مثال اجرا:**
```
عدد اول را وارد کنید: 10
عدد دوم را وارد کنید: 5
عملگر را وارد کنید (+, -, *, /): +
نتیجه: 15.0
```

**چالش:**
- بررسی کنید که عدد دوم برای تقسیم صفر نباشد
- پیام خطای مناسب نمایش دهید
- از توابع int() و float() به درستی استفاده کنید"""
    ],
    "lesson_type": "project",
    "section": "operators",
    "is_free": True,
    "code_examples": [
        "num1 = float(input('عدد اول: '))\nnum2 = float(input('عدد دوم: '))\noperator = input('عملگر: ')\nif operator == '+':\n    print(num1 + num2)"
    ],
    "expected_outputs": [
        "[نتیجه محاسبه]"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "چرا از float() به جای int() استفاده کردیم؟",
            "question_type": "text",
            "correct_answer": "برای پشتیبانی از اعداد اعشاری",
            "explanation": "float() هم اعداد صحیح و هم اعشاری را می‌پذیرد."
        },
        {
            "question_number": 2,
            "question_text": "چرا باید تقسیم بر صفر را بررسی کنیم؟",
            "question_type": "text",
            "correct_answer": "تقسیم بر صفر خطا می‌دهد",
            "explanation": "تقسیم بر صفر در پایتون خطا می‌دهد، باید بررسی کنیم."
        }
    ]
})

# ==================== FUNCTIONS AND CONDITIONS LESSONS ====================

LESSONS.append({
    "lesson_number": 8,
    "title": "توابع تبدیل نوع - int(), str(), float()",
    "content": [
        """🔧 **درس 8: توابع تبدیل نوع**

ما قبلاً با این توابع آشنا شدیم، حالا بیشتر یاد می‌گیریم:

**int() - تبدیل به عدد صحیح:**
```python
# String به Integer
age = int("25")
print(age)  # 25

# Float به Integer (اعشار حذف می‌شود)
price = int(19.99)
print(price)  # 19

# Boolean به Integer
print(int(True))   # 1
print(int(False))  # 0
```

**str() - تبدیل به رشته:**
```python
# Integer به String
age = str(25)
print(f"سن: {age}")  # سن: 25

# Float به String
price = str(19.99)
print(f"قیمت: {price}")  # قیمت: 19.99

# Boolean به String
print(str(True))   # "True"
```

**float() - تبدیل به عدد اعشاری:**
```python
# Integer به Float
num = float(10)
print(num)  # 10.0

# String به Float
price = float("19.99")
print(price)  # 19.99
```

**مثال عملی:**
```python
# دریافت ورودی و تبدیل
user_input = input("عدد را وارد کنید: ")
number = int(user_input)
double = number * 2
print(f"دو برابر: {double}")

# ترکیب انواع
age = 25
message = "سن شما: " + str(age) + " سال"
print(message)
```

**خروجی:**
```
دو برابر: [عدد * 2]
سن شما: 25 سال
```

**نکات مهم:**
- int() اعشار را حذف می‌کند
- str() هر چیزی را به متن تبدیل می‌کند
- float() همیشه اعشار دارد"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "age = int('25')\nprint(age + 5)",
        "price = float('19.99')\nprint(price * 2)"
    ],
    "expected_outputs": [
        "30",
        "39.98"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "int(19.99) چه مقداری دارد؟",
            "question_type": "text",
            "correct_answer": "19",
            "explanation": "int() اعشار را حذف می‌کند، پس 19.99 می‌شود 19."
        },
        {
            "question_number": 2,
            "question_text": "str(25) + str(10) چه مقداری دارد؟",
            "question_type": "text",
            "correct_answer": "'2510'",
            "explanation": "str() اعداد را به رشته تبدیل می‌کند و + رشته‌ها را به هم می‌چسباند."
        }
    ]
})

LESSONS.append({
    "lesson_number": 9,
    "title": "شرط if و else",
    "content": [
        """🔀 **درس 9: شرط if و else**

شرط‌ها برای تصمیم‌گیری در برنامه استفاده می‌شوند:

**if ساده:**
```python
age = 20
if age >= 18:
    print("بزرگسال هستید")
```

**if و else:**
```python
age = 15
if age >= 18:
    print("بزرگسال هستید")
else:
    print("نوجوان هستید")
```

**if، elif و else:**
```python
score = 85
if score >= 90:
    print("عالی")
elif score >= 70:
    print("خوب")
elif score >= 50:
    print("قابل قبول")
else:
    print("نیاز به تلاش بیشتر")
```

**مثال عملی:**
```python
# بررسی سن
age = int(input("سن خود را وارد کنید: "))
if age >= 18:
    print("شما می‌توانید رای دهید")
    if age >= 65:
        print("شما بازنشسته هستید")
else:
    print("شما هنوز نوجوان هستید")
```

**خروجی (اگر 20 وارد شود):**
```
شما می‌توانید رای دهید
```

**نکات مهم:**
- بعد از if باید : بگذارید
- کد داخل if باید indent (فاصله) داشته باشد
- elif برای چند شرط استفاده می‌شود
- else برای حالت پیش‌فرض است"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "age = 20\nif age >= 18:\n    print('بزرگسال')\nelse:\n    print('نوجوان')",
        "score = 85\nif score >= 90:\n    print('عالی')\nelif score >= 70:\n    print('خوب')"
    ],
    "expected_outputs": [
        "بزرگسال",
        "خوب"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "بعد از if چه علامتی باید بگذاریم؟",
            "question_type": "text",
            "correct_answer": ":",
            "explanation": "بعد از if باید : بگذاریم تا پایتون بداند شرط تمام شده."
        },
        {
            "question_number": 2,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nx = 10\nif x > 5:\n    print('بزرگ')\nelse:\n    print('کوچک')```",
            "question_type": "text",
            "correct_answer": "بزرگ",
            "explanation": "10 بزرگتر از 5 است، پس شرط True می‌شود و 'بزرگ' چاپ می‌شود."
        }
    ]
})

LESSONS.append({
    "lesson_number": 10,
    "title": "Try و Except - مدیریت خطا",
    "content": [
        """⚠️ **درس 10: Try و Except**

گاهی کد ما خطا می‌دهد. با try/except می‌توانیم خطاها را مدیریت کنیم:

**ساختار try/except:**
```python
try:
    # کدی که ممکن است خطا بدهد
    number = int(input("عدد را وارد کنید: "))
    result = 10 / number
    print(f"نتیجه: {result}")
except:
    # اگر خطا داد، این قسمت اجرا می‌شود
    print("خطا! لطفاً عدد معتبر وارد کنید")
```

**انواع خطاها:**
```python
try:
    age = int(input("سن: "))
    print(f"سن شما: {age}")
except ValueError:
    print("خطا: باید عدد وارد کنید")
except ZeroDivisionError:
    print("خطا: تقسیم بر صفر!")
except Exception as e:
    print(f"خطای ناشناخته: {e}")
```

**مثال عملی:**
```python
# دریافت عدد با مدیریت خطا
while True:
    try:
        age = int(input("سن خود را وارد کنید: "))
        if age > 0:
            print(f"سن شما: {age}")
            break
        else:
            print("سن باید مثبت باشد")
    except ValueError:
        print("لطفاً یک عدد معتبر وارد کنید")
```

**خروجی (اگر 'abc' وارد شود):**
```
لطفاً یک عدد معتبر وارد کنید
```

**نکات مهم:**
- try: کدی که ممکن است خطا بدهد
- except: کدی که در صورت خطا اجرا می‌شود
- می‌توانیم نوع خطا را مشخص کنیم
- Exception برای همه خطاها است"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "try:\n    x = int('abc')\nexcept:\n    print('خطا')",
        "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('تقسیم بر صفر')"
    ],
    "expected_outputs": [
        "خطا",
        "تقسیم بر صفر"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "try/except برای چه استفاده می‌شود؟",
            "question_type": "text",
            "correct_answer": "مدیریت خطا",
            "explanation": "try/except برای مدیریت خطاها و جلوگیری از crash برنامه استفاده می‌شود."
        },
        {
            "question_number": 2,
            "question_text": "اگر int('abc') خطا بدهد، چه نوع خطایی است؟",
            "question_type": "text",
            "correct_answer": "ValueError",
            "explanation": "تبدیل 'abc' به int خطای ValueError می‌دهد."
        }
    ]
})

LESSONS.append({
    "lesson_number": 11,
    "title": "حلقه While",
    "content": [
        """🔄 **درس 11: حلقه While**

حلقه while تا زمانی که شرط True باشد، تکرار می‌شود:

**ساختار while:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**خروجی:**
```
0
1
2
3
4
```

**مثال عملی:**
```python
# دریافت ورودی تا زمانی که معتبر باشد
while True:
    age = input("سن خود را وارد کنید (برای خروج 'q' بزنید): ")
    if age == 'q':
        break
    try:
        age_num = int(age)
        if age_num > 0:
            print(f"سن شما: {age_num}")
            break
        else:
            print("سن باید مثبت باشد")
    except ValueError:
        print("لطفاً عدد معتبر وارد کنید")
```

**break و continue:**
```python
# break: خروج از حلقه
count = 0
while count < 10:
    if count == 5:
        break  # حلقه متوقف می‌شود
    print(count)
    count += 1

# continue: رفتن به دور بعد
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # دور بعد شروع می‌شود
    print(count)
```

**نکات مهم:**
- while تا زمانی که شرط True باشد ادامه می‌دهد
- باید شرط را تغییر دهیم وگرنه حلقه بی‌نهایت می‌شود
- break برای خروج از حلقه
- continue برای رد کردن دور فعلی"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "count = 0\nwhile count < 3:\n    print(count)\n    count += 1",
        "x = 0\nwhile x < 5:\n    x += 1\n    if x == 3:\n        continue\n    print(x)"
    ],
    "expected_outputs": [
        "0\n1\n2",
        "1\n2\n4\n5"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "while تا چه زمانی ادامه می‌دهد؟",
            "question_type": "text",
            "correct_answer": "تا زمانی که شرط True باشد",
            "explanation": "while تا زمانی که شرط True باشد، کد را تکرار می‌کند."
        },
        {
            "question_number": 2,
            "question_text": "break چه کاری می‌کند؟",
            "question_type": "text",
            "correct_answer": "خروج از حلقه",
            "explanation": "break حلقه را متوقف می‌کند و از آن خارج می‌شود."
        }
    ]
})

LESSONS.append({
    "lesson_number": 12,
    "title": "حلقه For",
    "content": [
        """🔁 **درس 12: حلقه For**

حلقه for برای تکرار روی یک دنباله استفاده می‌شود:

**for با range():**
```python
# تکرار از 0 تا 4
for i in range(5):
    print(i)
```

**خروجی:**
```
0
1
2
3
4
```

**range() با شروع و پایان:**
```python
# از 1 تا 5
for i in range(1, 6):
    print(i)
```

**range() با گام:**
```python
# از 0 تا 10 با گام 2
for i in range(0, 11, 2):
    print(i)
# خروجی: 0, 2, 4, 6, 8, 10
```

**for روی String:**
```python
name = "علی"
for char in name:
    print(char)
# خروجی: ع، ل، ی
```

**مثال عملی:**
```python
# جمع اعداد از 1 تا 10
total = 0
for i in range(1, 11):
    total += i
print(f"جمع: {total}")  # 55

# چاپ جدول ضرب 5
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")
```

**نکات مهم:**
- for برای تکرار روی دنباله‌ها استفاده می‌شود
- range(5) یعنی 0 تا 4
- range(1, 6) یعنی 1 تا 5
- range(0, 11, 2) یعنی از 0 تا 10 با گام 2"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "for i in range(3):\n    print(i)",
        "total = 0\nfor i in range(1, 6):\n    total += i\nprint(total)"
    ],
    "expected_outputs": [
        "0\n1\n2",
        "15"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "range(5) چه اعدادی تولید می‌کند؟",
            "question_type": "text",
            "correct_answer": "0, 1, 2, 3, 4",
            "explanation": "range(5) از 0 شروع می‌شود و تا 4 ادامه می‌دهد."
        },
        {
            "question_number": 2,
            "question_text": "range(1, 6) چه اعدادی تولید می‌کند؟",
            "question_type": "text",
            "correct_answer": "1, 2, 3, 4, 5",
            "explanation": "range(1, 6) از 1 شروع می‌شود و تا 5 ادامه می‌دهد."
        }
    ]
})

LESSONS.append({
    "lesson_number": 13,
    "title": "تعریف تابع - def",
    "content": [
        """📝 **درس 13: تعریف تابع با def**

تابع یک بلوک کد قابل استفاده مجدد است:

**تعریف تابع ساده:**
```python
def greet():
    print("سلام!")
    print("خوش آمدید")

# فراخوانی تابع
greet()
```

**تابع با پارامتر:**
```python
def greet(name):
    print(f"سلام {name}!")

greet("علی")  # سلام علی!
greet("سارا")  # سلام سارا!
```

**تابع با چند پارامتر:**
```python
def add(a, b):
    result = a + b
    print(f"جمع: {result}")

add(5, 3)  # جمع: 8
```

**مثال عملی:**
```python
# تابع محاسبه مساحت مستطیل
def rectangle_area(width, height):
    area = width * height
    return area

# استفاده از تابع
area1 = rectangle_area(5, 10)
area2 = rectangle_area(3, 7)
print(f"مساحت اول: {area1}")  # 50
print(f"مساحت دوم: {area2}")  # 21
```

**نکات مهم:**
- def برای تعریف تابع استفاده می‌شود
- بعد از def باید : بگذاریم
- پارامترها در پرانتز قرار می‌گیرند
- تابع را با نام آن فراخوانی می‌کنیم"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "def greet(name):\n    print(f'سلام {name}')\ngreet('علی')",
        "def add(a, b):\n    return a + b\nresult = add(5, 3)\nprint(result)"
    ],
    "expected_outputs": [
        "سلام علی",
        "8"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای تعریف تابع چه کلمه کلیدی استفاده می‌شود؟",
            "question_type": "text",
            "correct_answer": "def",
            "explanation": "def کلمه کلیدی برای تعریف تابع در پایتون است."
        },
        {
            "question_number": 2,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\ndef multiply(x, y):\n    return x * y\nprint(multiply(3, 4))```",
            "question_type": "text",
            "correct_answer": "12",
            "explanation": "تابع multiply دو عدد را ضرب می‌کند: 3 * 4 = 12."
        }
    ]
})

LESSONS.append({
    "lesson_number": 14,
    "title": "Return در توابع",
    "content": [
        """↩️ **درس 14: Return در توابع**

return برای برگرداندن مقدار از تابع استفاده می‌شود:

**تابع بدون return:**
```python
def greet(name):
    print(f"سلام {name}!")

result = greet("علی")
print(result)  # None
```

**تابع با return:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

**return چند مقدار:**
```python
def calculate(a, b):
    sum_result = a + b
    product = a * b
    return sum_result, product

sum_val, prod_val = calculate(5, 3)
print(f"جمع: {sum_val}, ضرب: {prod_val}")
```

**return زودرس:**
```python
def check_age(age):
    if age < 0:
        return "سن نامعتبر"
    if age < 18:
        return "نوجوان"
    return "بزرگسال"

print(check_age(20))  # بزرگسال
print(check_age(15))  # نوجوان
```

**مثال عملی:**
```python
# تابع محاسبه میانگین
def average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

scores = [85, 90, 78, 92]
avg = average(scores)
print(f"میانگین: {avg}")
```

**نکات مهم:**
- return مقدار را برمی‌گرداند
- می‌توانیم چند مقدار برگردانیم
- return فوراً تابع را تمام می‌کند
- اگر return نباشد، تابع None برمی‌گرداند"""
    ],
    "lesson_type": "lesson",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "def multiply(x, y):\n    return x * y\nprint(multiply(4, 5))",
        "def get_info():\n    return 'علی', 25\nname, age = get_info()\nprint(f'{name}: {age}')"
    ],
    "expected_outputs": [
        "20",
        "علی: 25"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "return چه کاری می‌کند؟",
            "question_type": "text",
            "correct_answer": "مقدار را از تابع برمی‌گرداند",
            "explanation": "return مقدار را از تابع برمی‌گرداند و تابع را تمام می‌کند."
        },
        {
            "question_number": 2,
            "question_text": "اگر تابع return نداشته باشد، چه برمی‌گرداند؟",
            "question_type": "text",
            "correct_answer": "None",
            "explanation": "اگر تابع return نداشته باشد، به طور پیش‌فرض None برمی‌گرداند."
        }
    ]
})

# ==================== PROJECT 2 ====================

LESSONS.append({
    "lesson_number": 15,
    "title": "پروژه ترکیبی 2: بازی حدس عدد",
    "content": [
        """🎮 **پروژه 2: بازی حدس عدد**

بیایید یک بازی حدس عدد بسازیم:
1. برنامه یک عدد تصادفی انتخاب می‌کند
2. کاربر باید آن را حدس بزند
3. برنامه می‌گوید بزرگتر یا کوچکتر است

**کد کامل:**
```python
import random

def guess_number_game():
    # انتخاب عدد تصادفی بین 1 تا 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("بازی حدس عدد!")
    print("یک عدد بین 1 تا 100 انتخاب شده است.")
    
    while True:
        try:
            guess = int(input("حدس خود را وارد کنید: "))
            attempts += 1
            
            if guess < secret_number:
                print("بزرگتر!")
            elif guess > secret_number:
                print("کوچکتر!")
            else:
                print(f"🎉 درست حدس زدید! در {attempts} تلاش")
                break
        except ValueError:
            print("لطفاً عدد معتبر وارد کنید")

# اجرای بازی
guess_number_game()
```

**چالش:**
- محدودیت تعداد تلاش اضافه کنید
- پیام‌های تشویقی اضافه کنید
- امتیازدهی بر اساس تعداد تلاش"""
    ],
    "lesson_type": "project",
    "section": "functions",
    "is_free": True,
    "code_examples": [
        "import random\nsecret = random.randint(1, 10)\nguess = int(input('حدس: '))\nif guess == secret:\n    print('درست!')\nelse:\n    print('غلط!')"
    ],
    "expected_outputs": [
        "[بسته به حدس کاربر]"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "random.randint(1, 100) چه کاری می‌کند؟",
            "question_type": "text",
            "correct_answer": "یک عدد تصادفی بین 1 تا 100 برمی‌گرداند",
            "explanation": "randint یک عدد تصادفی در بازه مشخص شده برمی‌گرداند."
        }
    ]
})

# ==================== DATA STRUCTURES LESSONS ====================

LESSONS.append({
    "lesson_number": 16,
    "title": "لیست (List) - بخش 1: مقدمه و روش‌های پایه",
    "content": [
        """📋 **درس 16: لیست (List)**

لیست یک ساختار داده برای ذخیره چند مقدار است:

**ایجاد لیست:**
```python
# لیست خالی
my_list = []

# لیست با مقادیر
numbers = [1, 2, 3, 4, 5]
names = ["علی", "سارا", "رضا"]
mixed = [1, "علی", 3.14, True]
```

**دسترسی به عناصر:**
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # 10 (اولین عنصر)
print(numbers[2])  # 30 (سومین عنصر)
print(numbers[-1])  # 50 (آخرین عنصر)
```

**تغییر عناصر:**
```python
numbers = [1, 2, 3]
numbers[0] = 10
print(numbers)  # [10, 2, 3]
```

**مثال عملی:**
```python
# لیست نمرات
scores = [85, 90, 78, 92, 88]
print(f"اولین نمره: {scores[0]}")
print(f"آخرین نمره: {scores[-1]}")

# تغییر نمره
scores[2] = 85
print(f"نمرات جدید: {scores}")
```

**خروجی:**
```
اولین نمره: 85
آخرین نمره: 88
نمرات جدید: [85, 90, 85, 92, 88]
```

**نکات مهم:**
- لیست‌ها با [] ساخته می‌شوند
- اندیس از 0 شروع می‌شود
- می‌توانند انواع مختلف داده داشته باشند
- قابل تغییر هستند (mutable)"""
    ],
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "numbers = [1, 2, 3, 4, 5]\nprint(numbers[0])\nprint(numbers[-1])",
        "names = ['علی', 'سارا']\nnames[0] = 'رضا'\nprint(names)"
    ],
    "expected_outputs": [
        "1\n5",
        "['رضا', 'سارا']"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "numbers[0] به کدام عنصر دسترسی دارد؟",
            "question_type": "text",
            "correct_answer": "اولین عنصر",
            "explanation": "اندیس 0 به اولین عنصر لیست اشاره می‌کند."
        },
        {
            "question_number": 2,
            "question_text": "numbers[-1] به کدام عنصر دسترسی دارد؟",
            "question_type": "text",
            "correct_answer": "آخرین عنصر",
            "explanation": "اندیس منفی از انتها شمارش می‌کند، -1 آخرین عنصر است."
        }
    ]
})

LESSONS.append({
    "lesson_number": 17,
    "title": "لیست - بخش 2: متدهای append، insert، remove",
    "content": [
        """🔧 **درس 17: متدهای لیست**

**append() - اضافه کردن به انتها:**
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
```

**insert() - اضافه کردن در موقعیت خاص:**
```python
numbers = [1, 2, 3]
numbers.insert(1, 10)  # در موقعیت 1، عدد 10 را اضافه کن
print(numbers)  # [1, 10, 2, 3]
```

**remove() - حذف مقدار:**
```python
numbers = [1, 2, 3, 2]
numbers.remove(2)  # اولین 2 را حذف می‌کند
print(numbers)  # [1, 3, 2]
```

**pop() - حذف و برگرداندن:**
```python
numbers = [1, 2, 3]
last = numbers.pop()  # آخرین عنصر را حذف و برمی‌گرداند
print(last)  # 3
print(numbers)  # [1, 2]
```

**مثال عملی:**
```python
# لیست خرید
shopping = []
shopping.append("نان")
shopping.append("شیر")
shopping.insert(1, "تخم مرغ")
print(f"لیست: {shopping}")

shopping.remove("شیر")
print(f"بعد از حذف: {shopping}")
```

**خروجی:**
```
لیست: ['نان', 'تخم مرغ', 'شیر']
بعد از حذف: ['نان', 'تخم مرغ']
```

**نکات مهم:**
- append() به انتها اضافه می‌کند
- insert() در موقعیت خاص اضافه می‌کند
- remove() مقدار را حذف می‌کند
- pop() عنصر را حذف و برمی‌گرداند"""
    ],
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "numbers = [1, 2, 3]\nnumbers.append(4)\nprint(numbers)",
        "numbers = [1, 2, 3]\nnumbers.insert(1, 10)\nprint(numbers)"
    ],
    "expected_outputs": [
        "[1, 2, 3, 4]",
        "[1, 10, 2, 3]"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "append() چه کاری می‌کند؟",
            "question_type": "text",
            "correct_answer": "مقدار را به انتهای لیست اضافه می‌کند",
            "explanation": "append() یک عنصر را به انتهای لیست اضافه می‌کند."
        },
        {
            "question_number": 2,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nnumbers = [1, 2, 3]\nnumbers.insert(0, 10)\nprint(numbers)```",
            "question_type": "text",
            "correct_answer": "[10, 1, 2, 3]",
            "explanation": "insert(0, 10) عدد 10 را در ابتدای لیست اضافه می‌کند."
        }
    ]
})

LESSONS.append({
    "lesson_number": 18,
    "title": "لیست - بخش 3: لیست‌های تو در تو و map/filter/zip",
    "content": [
        """🔗 **درس 18: لیست‌های پیشرفته**

**لیست‌های تو در تو (Nested Lists):**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # 2 (ردیف اول، ستون دوم)
```

**map() - اعمال تابع روی همه عناصر:**
```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8]
```

**filter() - فیلتر کردن:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]
```

**zip() - ترکیب لیست‌ها:**
```python
names = ["علی", "سارا"]
ages = [25, 30]
combined = list(zip(names, ages))
print(combined)  # [('علی', 25), ('سارا', 30)]
```

**مثال عملی:**
```python
# تبدیل درجه به فارنهایت
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(f"فارنهایت: {fahrenheit}")

# فیلتر اعداد مثبت
numbers = [-5, 2, -1, 8, -3, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(f"مثبت‌ها: {positive}")
```

**خروجی:**
```
فارنهایت: [32.0, 50.0, 68.0, 86.0]
مثبت‌ها: [2, 8, 10]
```

**نکات مهم:**
- لیست‌های تو در تو برای ماتریس استفاده می‌شوند
- map() تابع را روی همه عناصر اعمال می‌کند
- filter() عناصری که شرط دارند را برمی‌گرداند
- zip() لیست‌ها را جفت می‌کند"""
    ],
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "matrix = [[1, 2], [3, 4]]\nprint(matrix[0][1])",
        "numbers = [1, 2, 3]\ndoubled = list(map(lambda x: x*2, numbers))\nprint(doubled)"
    ],
    "expected_outputs": [
        "2",
        "[2, 4, 6]"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "map() چه کاری می‌کند؟",
            "question_type": "text",
            "correct_answer": "تابع را روی همه عناصر لیست اعمال می‌کند",
            "explanation": "map() یک تابع را روی همه عناصر یک لیست اعمال می‌کند."
        },
        {
            "question_number": 2,
            "question_text": "filter() چه کاری می‌کند؟",
            "question_type": "text",
            "correct_answer": "عناصری که شرط دارند را برمی‌گرداند",
            "explanation": "filter() فقط عناصری را که شرط را برآورده می‌کنند برمی‌گرداند."
        }
    ]
})

LESSONS.append({
    "lesson_number": 19,
    "title": "Tuple - ساختار و کاربرد",
    "content": [
        """📌 **درس 19: Tuple**

Tuple شبیه لیست است اما قابل تغییر نیست (immutable):

**ایجاد Tuple:**
```python
# با پرانتز
my_tuple = (1, 2, 3)

# بدون پرانتز (کاما مهم است)
my_tuple = 1, 2, 3

# Tuple تک عنصری (باید کاما بگذاریم)
single = (5,)  # نه (5)
```

**دسترسی به عناصر:**
```python
coordinates = (10, 20)
x = coordinates[0]  # 10
y = coordinates[1]  # 20
```

**Tuple قابل تغییر نیست:**
```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ خطا می‌دهد!
```

**Tuple تو در تو:**
```python
nested = ((1, 2), (3, 4))
print(nested[0][1])  # 2
```

**مثال عملی:**
```python
# مختصات نقطه
point = (5, 10)
print(f"X: {point[0]}, Y: {point[1]}")

# بازگشت چند مقدار از تابع
def get_name_age():
    return "علی", 25

name, age = get_name_age()
print(f"{name}: {age}")
```

**خروجی:**
```
X: 5, Y: 10
علی: 25
```

**نکات مهم:**
- Tuple با () ساخته می‌شود
- قابل تغییر نیست (immutable)
- برای داده‌های ثابت مناسب است
- می‌تواند چند مقدار از تابع برگرداند"""
    ],
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "point = (10, 20)\nprint(point[0])",
        "def get_info():\n    return 'علی', 25\nname, age = get_info()\nprint(name)"
    ],
    "expected_outputs": [
        "10",
        "علی"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "Tuple قابل تغییر است؟",
            "question_type": "multiple_choice",
            "options": ["بله", "خیر", "گاهی", "بستگی دارد"],
            "correct_answer": "خیر",
            "explanation": "Tuple قابل تغییر نیست (immutable)، برخلاف لیست."
        },
        {
            "question_number": 2,
            "question_text": "تفاوت اصلی Tuple و List چیست؟",
            "question_type": "text",
            "correct_answer": "Tuple قابل تغییر نیست، List قابل تغییر است",
            "explanation": "Tuple immutable است و نمی‌توان عناصر آن را تغییر داد، اما List mutable است."
        }
    ]
})

LESSONS.append({
    "lesson_number": 20,
    "title": "Dictionary - ساختار و کاربرد",
    "content": [
        """📖 **درس 20: Dictionary**

Dictionary برای ذخیره داده‌ها به صورت کلید-مقدار استفاده می‌شود:

**ایجاد Dictionary:**
```python
# خالی
my_dict = {}

# با مقادیر
student = {
    "name": "علی",
    "age": 25,
    "city": "تهران"
}
```

**دسترسی به مقادیر:**
```python
student = {"name": "علی", "age": 25}
print(student["name"])  # علی
print(student.get("age"))  # 25
print(student.get("phone", "ندارد"))  # ندارد (مقدار پیش‌فرض)
```

**تغییر و اضافه کردن:**
```python
student = {"name": "علی"}
student["age"] = 25  # تغییر یا اضافه
student["city"] = "تهران"
print(student)  # {'name': 'علی', 'age': 25, 'city': 'تهران'}
```

**حذف:**
```python
student = {"name": "علی", "age": 25}
del student["age"]
# یا
student.pop("name")
```

**مثال عملی:**
```python
# اطلاعات دانشجو
student = {
    "name": "سارا",
    "age": 20,
    "scores": [85, 90, 88]
}

print(f"نام: {student['name']}")
print(f"میانگین: {sum(student['scores']) / len(student['scores'])}")
```

**خروجی:**
```
نام: سارا
میانگین: 87.66666666666667
```

**نکات مهم:**
- Dictionary با {} ساخته می‌شود
- کلید-مقدار ذخیره می‌کند
- کلیدها باید یکتا باشند
- برای داده‌های ساختاریافته مناسب است"""
    ],
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "student = {'name': 'علی', 'age': 25}\nprint(student['name'])",
        "student = {'name': 'علی'}\nstudent['age'] = 25\nprint(student)"
    ],
    "expected_outputs": [
        "علی",
        "{'name': 'علی', 'age': 25}"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "Dictionary با چه علامتی ساخته می‌شود؟",
            "question_type": "text",
            "correct_answer": "{}",
            "explanation": "Dictionary با {} ساخته می‌شود و شامل جفت‌های کلید-مقدار است."
        },
        {
            "question_number": 2,
            "question_text": "کد زیر چه خروجی می‌دهد؟\n```python\nd = {'a': 1, 'b': 2}\nprint(d.get('c', 0))```",
            "question_type": "text",
            "correct_answer": "0",
            "explanation": "get() اگر کلید وجود نداشته باشد، مقدار پیش‌فرض (0) را برمی‌گرداند."
        }
    ]
})

LESSONS.append({
    "lesson_number": 21,
    "title": "Dictionary - تو در تو و Set",
    "content": [
        """🔗 **درس 21: Dictionary تو در تو و Set**

**Dictionary تو در تو:**
```python
students = {
    "علی": {
        "age": 25,
        "scores": [85, 90]
    },
    "سارا": {
        "age": 20,
        "scores": [92, 88]
    }
}

print(students["علی"]["age"])  # 25
print(students["سارا"]["scores"][0])  # 92
```

**Set - مجموعه بدون تکرار:**
```python
# ایجاد Set
my_set = {1, 2, 3, 3, 4}  # تکرار حذف می‌شود
print(my_set)  # {1, 2, 3, 4}

# اضافه کردن
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

# حذف
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}
```

**عملیات Set:**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# اجتماع (union)
union = set1 | set2  # {1, 2, 3, 4, 5}

# اشتراک (intersection)
intersection = set1 & set2  # {3}

# تفاضل (difference)
difference = set1 - set2  # {1, 2}
```

**مثال عملی:**
```python
# حذف تکرارها از لیست
numbers = [1, 2, 2, 3, 3, 4]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4]

# بررسی عضویت
fruits = {"سیب", "موز", "پرتقال"}
print("سیب" in fruits)  # True
```

**نکات مهم:**
- Dictionary می‌تواند تو در تو باشد
- Set تکرار ندارد
- Set برای عملیات مجموعه‌ای مناسب است
- Set با {} ساخته می‌شود اما خالی نیست"""
    ],
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "students = {'علی': {'age': 25}}\nprint(students['علی']['age'])",
        "my_set = {1, 2, 2, 3}\nprint(my_set)"
    ],
    "expected_outputs": [
        "25",
        "{1, 2, 3}"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "Set چه ویژگی دارد؟",
            "question_type": "text",
            "correct_answer": "تکرار ندارد",
            "explanation": "Set به طور خودکار تکرارها را حذف می‌کند."
        },
        {
            "question_number": 2,
            "question_text": "برای حذف تکرار از لیست چه باید کرد؟",
            "question_type": "text",
            "correct_answer": "تبدیل به Set و برگرداندن به لیست",
            "explanation": "list(set(numbers)) تکرارها را حذف می‌کند."
        }
    ]
})

# ==================== PROJECT 3 ====================

LESSONS.append({
    "lesson_number": 22,
    "title": "پروژه ترکیبی 3: مدیریت لیست دانشجویان",
    "content": [
        """🎯 **پروژه 3: مدیریت لیست دانشجویان**

بیایید یک سیستم مدیریت دانشجویان بسازیم:
1. اضافه کردن دانشجو
2. نمایش لیست
3. جستجو
4. حذف

**کد کامل:**
```python
students = []

def add_student():
    name = input("نام دانشجو: ")
    age = int(input("سن: "))
    score = float(input("نمره: "))
    student = {
        "name": name,
        "age": age,
        "score": score
    }
    students.append(student)
    print("دانشجو اضافه شد!")

def show_students():
    if not students:
        print("لیست خالی است")
        return
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} - سن: {student['age']} - نمره: {student['score']}")

def search_student():
    name = input("نام برای جستجو: ")
    found = [s for s in students if name.lower() in s['name'].lower()]
    if found:
        for student in found:
            print(f"{student['name']} - نمره: {student['score']}")
    else:
        print("یافت نشد")

# استفاده
add_student()
add_student()
show_students()
search_student()
```

**چالش:**
- محاسبه میانگین نمرات
- مرتب‌سازی بر اساس نمره
- ذخیره در فایل"""
    ],
    "lesson_type": "project",
    "section": "data_structures",
    "is_free": True,
    "code_examples": [
        "students = [{'name': 'علی', 'score': 85}]\nfor s in students:\n    print(s['name'])"
    ],
    "expected_outputs": [
        "علی"
    ],
    "questions": [
        {
            "question_number": 1,
            "question_text": "چرا از Dictionary برای دانشجو استفاده کردیم؟",
            "question_type": "text",
            "correct_answer": "برای ذخیره اطلاعات ساختاریافته",
            "explanation": "Dictionary برای داده‌های ساختاریافته با کلید-مقدار مناسب است."
        }
    ]
})

# Continue with more lessons...

def get_all_lessons():
    """Return all lessons"""
    return LESSONS

def get_lesson_by_number(lesson_number: int) -> Dict:
    """Get a specific lesson by number"""
    for lesson in LESSONS:
        if lesson["lesson_number"] == lesson_number:
            return lesson
    return None

def get_free_lessons():
    """Get all free lessons"""
    return [lesson for lesson in LESSONS if lesson["is_free"]]

def get_lessons_by_section(section: str):
    """Get lessons by section"""
    return [lesson for lesson in LESSONS if lesson["section"] == section]

