# -*- coding: utf-8 -*-
"""
محتوای 15 درس پایتون تا ساخت ربات تلگرام
همه درس‌ها رایگان هستند
"""

import json
from typing import Dict, List

LESSONS = []

# ==================== بخش 1: مبانی پایتون ====================

# درس 1: مقدمه و نصب پایتون
LESSONS.append({
    "lesson_number": 1,
    "title": "مقدمه و نصب پایتون",
    "content": json.dumps([
        """🎓 **درس 1: مقدمه و نصب پایتون**

سلام! به دوره آموزش پایتون خوش آمدید! 🎉

**پایتون چیست؟**
پایتون یک زبان برنامه‌نویسی قدرتمند و ساده است که:
- ✅ خواندن و نوشتن آن آسان است
- ✅ برای مبتدیان عالی است
- ✅ در بسیاری از زمینه‌ها استفاده می‌شود (وب، داده، هوش مصنوعی، ربات)
- ✅ جامعه بزرگ و پشتیبانی عالی دارد

**چرا پایتون؟**
- ساده و قابل فهم
- همه کاره (می‌توانید هر چیزی بسازید)
- کتابخانه‌های زیاد
- مناسب برای ساخت ربات تلگرام""",
        
        """📦 **نصب پایتون**

**مرحله 1: دانلود**
1. به سایت python.org بروید
2. آخرین نسخه Python 3.11 یا بالاتر را دانلود کنید
3. هنگام نصب، حتماً گزینه "Add Python to PATH" را تیک بزنید

**مرحله 2: بررسی نصب**
در Command Prompt یا Terminal بنویسید:
```
python --version
```

باید چیزی شبیه `Python 3.11.x` نمایش داده شود.

**مرحله 3: اولین برنامه**
یک فایل با نام `hello.py` بسازید و بنویسید:
```python
print("سلام دنیا!")
```

سپس اجرا کنید:
```
python hello.py
```

باید "سلام دنیا!" را ببینید! 🎉"""
    ]),
    "lesson_type": "lesson",
    "section": "basics",
    "is_free": True,
    "code_examples": json.dumps([
        "# اولین برنامه\nprint('سلام دنیا!')\nprint('خوش آمدید به پایتون!')"
    ]),
    "expected_outputs": json.dumps([
        "سلام دنیا!\nخوش آمدید به پایتون!"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "پایتون چیست؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["یک زبان برنامه‌نویسی", "یک نرم‌افزار", "یک کتابخانه", "یک سیستم عامل"]),
            "correct_answer": "یک زبان برنامه‌نویسی",
            "explanation": "پایتون یک زبان برنامه‌نویسی سطح بالا و تفسیری است."
        },
        {
            "question_number": 2,
            "question_text": "برای اجرای فایل Python از چه دستوری استفاده می‌کنیم؟",
            "question_type": "text",
            "correct_answer": "python",
            "explanation": "از دستور python برای اجرای فایل‌های Python استفاده می‌شود."
        }
    ]
})

# درس 2: متغیرها و انواع داده
LESSONS.append({
    "lesson_number": 2,
    "title": "متغیرها و انواع داده",
    "content": json.dumps([
        """📚 **درس 2: متغیرها و انواع داده**

**متغیر چیست؟**
متغیر یک نام است که برای ذخیره داده استفاده می‌شود.
مثل یک جعبه که می‌توانید چیزهایی در آن بگذارید!

**انواع داده در پایتون:**
1. **int** (عدد صحیح): 5, 10, -3
2. **float** (عدد اعشاری): 3.14, 2.5
3. **str** (رشته): "سلام", 'دنیا'
4. **bool** (درست/غلط): True, False""",
        
        """💡 **مثال‌های عملی:**

```python
# عدد صحیح
age = 25
print(age)  # خروجی: 25

# عدد اعشاری
price = 99.99
print(price)  # خروجی: 99.99

# رشته
name = "علی"
print(name)  # خروجی: علی

# درست/غلط
is_student = True
print(is_student)  # خروجی: True
```

**ورودی و خروجی:**
```python
# دریافت ورودی از کاربر
name = input("نام خود را وارد کنید: ")
print(f"سلام {name}!")
```"""
    ]),
    "lesson_type": "lesson",
    "section": "basics",
    "is_free": True,
    "code_examples": json.dumps([
        "# تعریف متغیرها\nname = 'علی'\nage = 25\nheight = 175.5\nis_student = True\n\nprint(f'نام: {name}')\nprint(f'سن: {age}')\nprint(f'قد: {height}')\nprint(f'دانشجو: {is_student}')"
    ]),
    "expected_outputs": json.dumps([
        "نام: علی\nسن: 25\nقد: 175.5\nدانشجو: True"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام نوع داده برای ذخیره نام استفاده می‌شود؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["int", "str", "float", "bool"]),
            "correct_answer": "str",
            "explanation": "str (string) برای ذخیره متن استفاده می‌شود."
        }
    ]
})

# درس 3: عملگرها و عبارات
LESSONS.append({
    "lesson_number": 3,
    "title": "عملگرها و عبارات",
    "content": json.dumps([
        """🔢 **درس 3: عملگرها و عبارات**

**عملگرهای ریاضی:**
- `+` جمع
- `-` تفریق
- `*` ضرب
- `/` تقسیم
- `//` تقسیم صحیح
- `%` باقیمانده
- `**` توان

**عملگرهای مقایسه:**
- `==` برابر است؟
- `!=` برابر نیست؟
- `<` کوچکتر
- `>` بزرگتر
- `<=` کوچکتر یا مساوی
- `>=` بزرگتر یا مساوی

**عملگرهای منطقی:**
- `and` و
- `or` یا
- `not` نه""",
        
        """💡 **مثال‌ها:**

```python
# ریاضی
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000

# مقایسه
print(5 > 3)   # True
print(5 == 3)  # False
print(5 != 3)  # True

# منطقی
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```"""
    ]),
    "lesson_type": "lesson",
    "section": "basics",
    "is_free": True,
    "code_examples": json.dumps([
        "# عملگرها\na = 10\nb = 3\nprint(f'جمع: {a + b}')\nprint(f'ضرب: {a * b}')\nprint(f'باقیمانده: {a % b}')\nprint(f'توان: {a ** b}')"
    ]),
    "expected_outputs": json.dumps([
        "جمع: 13\nضرب: 30\nباقیمانده: 1\nتوان: 1000"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "نتیجه 10 // 3 چیست؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["3.33", "3", "4", "1"]),
            "correct_answer": "3",
            "explanation": "// تقسیم صحیح است که فقط قسمت صحیح را برمی‌گرداند."
        }
    ]
})

# درس 4: ساختارهای کنترلی
LESSONS.append({
    "lesson_number": 4,
    "title": "ساختارهای کنترلی",
    "content": json.dumps([
        """🎯 **درس 4: ساختارهای کنترلی**

**دستور if/elif/else:**
برای تصمیم‌گیری در برنامه استفاده می‌شود.

```python
age = 18
if age >= 18:
    print("بزرگسال")
else:
    print("نوجوان")
```

**حلقه for:**
برای تکرار روی یک لیست یا محدوده.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

**حلقه while:**
تا زمانی که شرط درست باشد، تکرار می‌شود.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```""",
        
        """💡 **مثال‌های پیشرفته:**

```python
# if/elif/else
score = 85
if score >= 90:
    print("عالی")
elif score >= 70:
    print("خوب")
else:
    print("نیاز به تلاش بیشتر")

# for با لیست
names = ["علی", "مریم", "رضا"]
for name in names:
    print(f"سلام {name}")

# while با شرط
password = ""
while password != "1234":
    password = input("رمز را وارد کنید: ")
print("ورود موفق!")
```"""
    ]),
    "lesson_type": "lesson",
    "section": "basics",
    "is_free": True,
    "code_examples": json.dumps([
        "# if/else\nage = 20\nif age >= 18:\n    print('بزرگسال')\nelse:\n    print('نوجوان')\n\n# for\nfor i in range(1, 6):\n    print(f'عدد: {i}')"
    ]),
    "expected_outputs": json.dumps([
        "بزرگسال\nعدد: 1\nعدد: 2\nعدد: 3\nعدد: 4\nعدد: 5"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام دستور برای تکرار استفاده می‌شود؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["if", "for", "print", "input"]),
            "correct_answer": "for",
            "explanation": "for برای تکرار روی یک لیست یا محدوده استفاده می‌شود."
        }
    ]
})

# درس 5: توابع
LESSONS.append({
    "lesson_number": 5,
    "title": "توابع",
    "content": json.dumps([
        """⚙️ **درس 5: توابع**

**تابع چیست؟**
تابع یک بلوک کد است که می‌تواند چندین بار استفاده شود.

**تعریف تابع:**
```python
def greet(name):
    return f"سلام {name}!"

print(greet("علی"))  # خروجی: سلام علی!
```

**پارامترها:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

**مقدار پیش‌فرض:**
```python
def greet(name="کاربر"):
    return f"سلام {name}!"

print(greet())      # سلام کاربر!
print(greet("علی")) # سلام علی!
```""",
        
        """💡 **مثال‌های عملی:**

```python
# تابع ساده
def square(x):
    return x * x

print(square(5))  # 25

# تابع با چند پارامتر
def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b

print(calculate("add", 5, 3))  # 8
```"""
    ]),
    "lesson_type": "lesson",
    "section": "basics",
    "is_free": True,
    "code_examples": json.dumps([
        "# تعریف تابع\ndef greet(name):\n    return f'سلام {name}!'\n\nprint(greet('علی'))\n\n# تابع با چند پارامتر\ndef add(a, b):\n    return a + b\n\nprint(add(5, 3))"
    ]),
    "expected_outputs": json.dumps([
        "سلام علی!\n8"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "کدام کلمه کلیدی برای تعریف تابع استفاده می‌شود؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["def", "function", "func", "define"]),
            "correct_answer": "def",
            "explanation": "def کلمه کلیدی برای تعریف تابع در پایتون است."
        }
    ]
})

# ==================== بخش 2: ساختارهای داده ====================

# درس 6: لیست‌ها
LESSONS.append({
    "lesson_number": 6,
    "title": "لیست‌ها (Lists)",
    "content": json.dumps([
        """📋 **درس 6: لیست‌ها**

**لیست چیست؟**
لیست یک مجموعه مرتب از داده‌هاست.

```python
fruits = ["سیب", "موز", "پرتقال"]
print(fruits[0])  # سیب
```

**متدهای لیست:**
- `append()` - اضافه کردن
- `remove()` - حذف
- `pop()` - حذف و برگرداندن
- `sort()` - مرتب کردن
- `len()` - طول لیست""",
        
        """💡 **مثال‌ها:**

```python
# ساخت لیست
numbers = [1, 2, 3, 4, 5]

# اضافه کردن
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# حذف
numbers.remove(3)
print(numbers)  # [1, 2, 4, 5, 6]

# حلقه روی لیست
for num in numbers:
    print(num)
```"""
    ]),
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": json.dumps([
        "# لیست\nfruits = ['سیب', 'موز', 'پرتقال']\nfruits.append('انگور')\nprint(fruits)\nprint(f'تعداد: {len(fruits)}')"
    ]),
    "expected_outputs": json.dumps([
        "['سیب', 'موز', 'پرتقال', 'انگور']\nتعداد: 4"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای اضافه کردن به لیست از چه متدی استفاده می‌کنیم؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["add", "append", "insert", "push"]),
            "correct_answer": "append",
            "explanation": "append() برای اضافه کردن عنصر به انتهای لیست استفاده می‌شود."
        }
    ]
})

# درس 7: دیکشنری‌ها
LESSONS.append({
    "lesson_number": 7,
    "title": "دیکشنری‌ها (Dictionaries)",
    "content": json.dumps([
        """📖 **درس 7: دیکشنری‌ها**

**دیکشنری چیست؟**
دیکشنری یک مجموعه از جفت‌های کلید-مقدار است.

```python
student = {
    "name": "علی",
    "age": 20,
    "grade": "A"
}
print(student["name"])  # علی
```

**عملیات:**
- دسترسی: `dict["key"]`
- اضافه/به‌روزرسانی: `dict["key"] = value`
- حذف: `del dict["key"]`""",
        
        """💡 **مثال‌ها:**

```python
# ساخت دیکشنری
person = {
    "name": "علی",
    "age": 25,
    "city": "تهران"
}

# دسترسی
print(person["name"])  # علی

# به‌روزرسانی
person["age"] = 26

# حلقه روی دیکشنری
for key, value in person.items():
    print(f"{key}: {value}")
```"""
    ]),
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": json.dumps([
        "# دیکشنری\nstudent = {'name': 'علی', 'age': 20, 'grade': 'A'}\nprint(student['name'])\nstudent['age'] = 21\nprint(student)"
    ]),
    "expected_outputs": json.dumps([
        "علی\n{'name': 'علی', 'age': 21, 'grade': 'A'}"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "دیکشنری از چه ساختاری استفاده می‌کند؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["کلید-مقدار", "فقط مقدار", "فقط کلید", "ایندکس"]),
            "correct_answer": "کلید-مقدار",
            "explanation": "دیکشنری از ساختار کلید-مقدار استفاده می‌کند."
        }
    ]
})

# درس 8: تاپل‌ها و ست‌ها
LESSONS.append({
    "lesson_number": 8,
    "title": "تاپل‌ها و ست‌ها",
    "content": json.dumps([
        """🔗 **درس 8: تاپل‌ها و ست‌ها**

**تاپل چیست؟**
تاپل مثل لیست است اما قابل تغییر نیست (immutable).

```python
point = (10, 20)
print(point[0])  # 10
```

**ست چیست؟**
ست یک مجموعه بدون ترتیب و بدون تکرار.

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}
```

**تفاوت‌ها:**
- لیست: قابل تغییر، ترتیب دارد
- تاپل: غیرقابل تغییر، ترتیب دارد
- ست: قابل تغییر، ترتیب ندارد، بدون تکرار""",
        
        """💡 **مثال‌ها:**

```python
# تاپل
coordinates = (10, 20)
x, y = coordinates
print(f"x: {x}, y: {y}")

# ست
unique_numbers = {1, 2, 3, 3, 4, 4}
print(unique_numbers)  # {1, 2, 3, 4}

# عملیات روی ست
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}
```"""
    ]),
    "lesson_type": "lesson",
    "section": "data_structures",
    "is_free": True,
    "code_examples": json.dumps([
        "# تاپل\npoint = (10, 20)\nprint(f'x: {point[0]}, y: {point[1]}')\n\n# ست\nnumbers = {1, 2, 3, 3, 4}\nprint(numbers)"
    ]),
    "expected_outputs": json.dumps([
        "x: 10, y: 20\n{1, 2, 3, 4}"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "تفاوت اصلی تاپل با لیست چیست؟",
            "question_type": "text",
            "correct_answer": "غیرقابل تغییر",
            "explanation": "تاپل غیرقابل تغییر (immutable) است اما لیست قابل تغییر است."
        }
    ]
})

# ==================== بخش 3: پیشرفته ====================

# درس 9: فایل‌ها و مدیریت خطا
LESSONS.append({
    "lesson_number": 9,
    "title": "فایل‌ها و مدیریت خطا",
    "content": json.dumps([
        """📁 **درس 9: فایل‌ها و مدیریت خطا**

**خواندن از فایل:**
```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

**نوشتن در فایل:**
```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("سلام دنیا!")
```

**مدیریت خطا:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("خطا: تقسیم بر صفر!")
```""",
        
        """💡 **مثال‌های عملی:**

```python
# نوشتن در فایل
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("این یک تست است")

# خواندن از فایل
try:
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("فایل یافت نشد!")
```"""
    ]),
    "lesson_type": "lesson",
    "section": "advanced",
    "is_free": True,
    "code_examples": json.dumps([
        "# نوشتن در فایل\nwith open('test.txt', 'w', encoding='utf-8') as f:\n    f.write('سلام')\n\n# خواندن\nwith open('test.txt', 'r', encoding='utf-8') as f:\n    print(f.read())"
    ]),
    "expected_outputs": json.dumps([
        "سلام"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای مدیریت خطا از چه دستوری استفاده می‌کنیم؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["if", "try/except", "for", "while"]),
            "correct_answer": "try/except",
            "explanation": "try/except برای مدیریت خطا استفاده می‌شود."
        }
    ]
})

# درس 10: ماژول‌ها و کتابخانه‌ها
LESSONS.append({
    "lesson_number": 10,
    "title": "ماژول‌ها و کتابخانه‌ها",
    "content": json.dumps([
        """📦 **درس 10: ماژول‌ها و کتابخانه‌ها**

**import کردن:**
```python
import math
print(math.sqrt(16))  # 4.0
```

**نصب کتابخانه:**
```bash
pip install نام_کتابخانه
```

**کتابخانه‌های مفید:**
- `datetime` - کار با تاریخ و زمان
- `random` - اعداد تصادفی
- `json` - کار با JSON
- `requests` - درخواست HTTP""",
        
        """💡 **مثال‌ها:**

```python
# استفاده از ماژول
import random
number = random.randint(1, 10)
print(number)

# import خاص
from datetime import datetime
now = datetime.now()
print(now)

# ساخت ماژول خودمان
# در فایل my_module.py:
def greet(name):
    return f"سلام {name}!"

# استفاده:
import my_module
print(my_module.greet("علی"))
```"""
    ]),
    "lesson_type": "lesson",
    "section": "advanced",
    "is_free": True,
    "code_examples": json.dumps([
        "import random\nimport math\n\nprint(f'عدد تصادفی: {random.randint(1, 10)}')\nprint(f'جذر 16: {math.sqrt(16)}')"
    ]),
    "expected_outputs": json.dumps([
        "عدد تصادفی: [عدد بین 1 تا 10]\nجذر 16: 4.0"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای نصب کتابخانه از چه دستوری استفاده می‌کنیم؟",
            "question_type": "text",
            "correct_answer": "pip install",
            "explanation": "pip install برای نصب کتابخانه‌های Python استفاده می‌شود."
        }
    ]
})

# درس 11: برنامه‌نویسی شی‌گرا
LESSONS.append({
    "lesson_number": 11,
    "title": "برنامه‌نویسی شی‌گرا (مقدماتی)",
    "content": json.dumps([
        """🏗️ **درس 11: برنامه‌نویسی شی‌گرا**

**کلاس چیست؟**
کلاس یک الگو برای ساخت اشیاء است.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"سلام، من {self.name} هستم و {self.age} سال دارم"

person = Person("علی", 25)
print(person.introduce())
```""",
        
        """💡 **مثال پیشرفته:**

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

student = Student("علی", "12345")
student.add_grade(18)
student.add_grade(20)
print(f"میانگین: {student.average()}")  # 19.0
```"""
    ]),
    "lesson_type": "lesson",
    "section": "advanced",
    "is_free": True,
    "code_examples": json.dumps([
        "class Person:\n    def __init__(self, name):\n        self.name = name\n    \n    def greet(self):\n        return f'سلام {self.name}!'\n\nperson = Person('علی')\nprint(person.greet())"
    ]),
    "expected_outputs": json.dumps([
        "سلام علی!"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "متد __init__ چه کاری انجام می‌دهد؟",
            "question_type": "text",
            "correct_answer": "مقداردهی اولیه",
            "explanation": "__init__ متد سازنده است که هنگام ساخت شیء اجرا می‌شود."
        }
    ]
})

# ==================== بخش 4: ساخت ربات تلگرام ====================

# درس 12: مقدمه ربات تلگرام
LESSONS.append({
    "lesson_number": 12,
    "title": "مقدمه ربات تلگرام",
    "content": json.dumps([
        """🤖 **درس 12: مقدمه ربات تلگرام**

**ربات تلگرام چیست؟**
ربات تلگرام یک برنامه خودکار است که در تلگرام کار می‌کند و به پیام‌ها پاسخ می‌دهد.

**مراحل ساخت ربات:**

**1. ساخت ربات در BotFather:**
- به @BotFather در تلگرام بروید
- دستور `/newbot` را بزنید
- نام و username ربات را وارد کنید
- توکن را دریافت و ذخیره کنید""",
        
        """**2. نصب کتابخانه:**
```bash
pip install python-telegram-bot python-dotenv
```

**3. اولین ربات ساده:**
```python
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام!')

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
```

**4. تست:**
- ربات را اجرا کنید
- در تلگرام به ربات بروید
- `/start` بزنید
- باید "سلام!" را ببینید! 🎉"""
    ]),
    "lesson_type": "lesson",
    "section": "telegram_bot",
    "is_free": True,
    "code_examples": json.dumps([
        "from telegram.ext import Application, CommandHandler\nfrom telegram import Update\n\nasync def start(update: Update, context):\n    await update.message.reply_text('سلام!')\n\napp = Application.builder().token('TOKEN').build()\napp.add_handler(CommandHandler('start', start))\napp.run_polling()"
    ]),
    "expected_outputs": json.dumps([
        "ربات اجرا می‌شود و به /start پاسخ می‌دهد"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای ساخت ربات تلگرام باید به کجا برویم؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["@BotFather", "@Telegram", "@Python", "@Bot"]),
            "correct_answer": "@BotFather",
            "explanation": "@BotFather ربات رسمی تلگرام برای ساخت ربات است."
        }
    ]
})

# درس 13: دستورات و پیام‌ها
LESSONS.append({
    "lesson_number": 13,
    "title": "دستورات و پیام‌ها",
    "content": json.dumps([
        """💬 **درس 13: دستورات و پیام‌ها**

**ساخت دستورات:**
```python
async def help_command(update: Update, context):
    await update.message.reply_text('راهنما...')

app.add_handler(CommandHandler("help", help_command))
```

**مدیریت پیام‌های متنی:**
```python
async def echo(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f"شما گفتید: {text}")

app.add_handler(MessageHandler(filters.TEXT, echo))
```

**Conversation Handler:**
برای مکالمه چند مرحله‌ای استفاده می‌شود.""",
        
        """💡 **مثال: ربات ثبت‌نام**

```python
from telegram.ext import ConversationHandler

WAITING_NAME, WAITING_AGE = range(2)

async def start_registration(update: Update, context):
    await update.message.reply_text('نام خود را وارد کنید:')
    return WAITING_NAME

async def get_name(update: Update, context):
    context.user_data['name'] = update.message.text
    await update.message.reply_text('سن خود را وارد کنید:')
    return WAITING_AGE

async def get_age(update: Update, context):
    age = update.message.text
    name = context.user_data['name']
    await update.message.reply_text(f'ثبت شد: {name}, {age} سال')
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('register', start_registration)],
    states={
        WAITING_NAME: [MessageHandler(filters.TEXT, get_name)],
        WAITING_AGE: [MessageHandler(filters.TEXT, get_age)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
```"""
    ]),
    "lesson_type": "lesson",
    "section": "telegram_bot",
    "is_free": True,
    "code_examples": json.dumps([
        "# دستورات\nasync def help(update, context):\n    await update.message.reply_text('راهنما')\n\n# پیام‌ها\nasync def echo(update, context):\n    await update.message.reply_text(update.message.text)"
    ]),
    "expected_outputs": json.dumps([
        "ربات به دستورات و پیام‌ها پاسخ می‌دهد"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای ساخت دستور از چه Handler استفاده می‌کنیم؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["CommandHandler", "MessageHandler", "CallbackHandler", "QueryHandler"]),
            "correct_answer": "CommandHandler",
            "explanation": "CommandHandler برای مدیریت دستورات (commands) استفاده می‌شود."
        }
    ]
})

# درس 14: دکمه‌ها و منو
LESSONS.append({
    "lesson_number": 14,
    "title": "دکمه‌ها و منو",
    "content": json.dumps([
        """🔘 **درس 14: دکمه‌ها و منو**

**Inline Keyboard (دکمه‌های inline):**
```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = [
    [InlineKeyboardButton("گزینه 1", callback_data='option1')],
    [InlineKeyboardButton("گزینه 2", callback_data='option2')]
]
reply_markup = InlineKeyboardMarkup(keyboard)
await update.message.reply_text('انتخاب کنید:', reply_markup=reply_markup)
```

**Reply Keyboard (منوی کیبورد):**
```python
from telegram import ReplyKeyboardMarkup

keyboard = [['گزینه 1', 'گزینه 2']]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
await update.message.reply_text('منو:', reply_markup=reply_markup)
```""",
        
        """💡 **مثال کامل:**

```python
# Inline Keyboard
async def show_menu(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("📚 درس‌ها", callback_data='lessons')],
        [InlineKeyboardButton("📊 پیشرفت", callback_data='progress')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('منوی اصلی:', reply_markup=reply_markup)

# Callback Handler
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'lessons':
        await query.edit_message_text('فهرست درس‌ها...')
    elif query.data == 'progress':
        await query.edit_message_text('پیشرفت شما...')

app.add_handler(CallbackQueryHandler(button_callback))
```"""
    ]),
    "lesson_type": "lesson",
    "section": "telegram_bot",
    "is_free": True,
    "code_examples": json.dumps([
        "from telegram import InlineKeyboardButton, InlineKeyboardMarkup\n\nkeyboard = [[InlineKeyboardButton('کلیک کنید', callback_data='click')]]\nmarkup = InlineKeyboardMarkup(keyboard)\nawait update.message.reply_text('دکمه:', reply_markup=markup)"
    ]),
    "expected_outputs": json.dumps([
        "دکمه inline نمایش داده می‌شود"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای مدیریت کلیک روی دکمه inline از چه Handler استفاده می‌کنیم؟",
            "question_type": "multiple_choice",
            "options": json.dumps(["CallbackQueryHandler", "CommandHandler", "MessageHandler", "ButtonHandler"]),
            "correct_answer": "CallbackQueryHandler",
            "explanation": "CallbackQueryHandler برای مدیریت کلیک روی دکمه‌های inline استفاده می‌شود."
        }
    ]
})

# درس 15: ربات کامل با دیتابیس
LESSONS.append({
    "lesson_number": 15,
    "title": "ربات کامل با دیتابیس",
    "content": json.dumps([
        """🗄️ **درس 15: ربات کامل با دیتابیس**

**اتصال به Supabase:**
```python
from supabase import create_client

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
```

**ذخیره اطلاعات:**
```python
user_data = {
    "telegram_id": user_id,
    "name": name,
    "phone": phone
}
supabase.table("users").insert(user_data).execute()
```

**خواندن اطلاعات:**
```python
result = supabase.table("users").select("*").eq("telegram_id", user_id).execute()
user = result.data[0] if result.data else None
```""",
        
        """💡 **پروژه نهایی: ربات یادگیری**

در این درس یک ربات کامل می‌سازیم که:
- ✅ کاربران را ثبت‌نام می‌کند
- ✅ اطلاعات را در دیتابیس ذخیره می‌کند
- ✅ منوی زیبا دارد
- ✅ پیشرفت کاربر را ردیابی می‌کند

**ساختار کامل:**
```python
# ثبت‌نام
async def register(update: Update, context):
    # دریافت اطلاعات
    # ذخیره در دیتابیس
    # نمایش منو

# نمایش منو
async def show_menu(update: Update, context):
    # ساخت دکمه‌ها
    # نمایش منو

# مدیریت کلیک
async def handle_callback(update: Update, context):
    # پردازش کلیک
    # نمایش محتوا
```

**تبریک! شما حالا یک ربات کامل دارید! 🎉**"""
    ]),
    "lesson_type": "project",
    "section": "telegram_bot",
    "is_free": True,
    "code_examples": json.dumps([
        "from supabase import create_client\n\nsupabase = create_client(URL, KEY)\n\n# ذخیره\nsupabase.table('users').insert({'telegram_id': 123, 'name': 'علی'}).execute()\n\n# خواندن\nresult = supabase.table('users').select('*').eq('telegram_id', 123).execute()"
    ]),
    "expected_outputs": json.dumps([
        "اطلاعات در دیتابیس ذخیره و خوانده می‌شود"
    ]),
    "questions": [
        {
            "question_number": 1,
            "question_text": "برای اتصال به Supabase از چه کتابخانه‌ای استفاده می‌کنیم؟",
            "question_type": "text",
            "correct_answer": "supabase",
            "explanation": "کتابخانه supabase برای اتصال به Supabase استفاده می‌شود."
        }
    ]
})

def get_all_lessons():
    """بازگرداندن همه درس‌ها"""
    return LESSONS

def get_lesson_by_number(lesson_number: int) -> Dict:
    """دریافت درس خاص بر اساس شماره"""
    for lesson in LESSONS:
        if lesson["lesson_number"] == lesson_number:
            return lesson
    return None

def get_lessons_count():
    """تعداد کل درس‌ها"""
    return len(LESSONS)

