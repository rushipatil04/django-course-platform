import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courseplatform.settings')
django.setup()

from courses.models import Category, Course
from accounts.models import User

# Create categories
categories = [
    {'name': 'Programming', 'slug': 'programming'},
    {'name': 'Design', 'slug': 'design'},
    {'name': 'Business', 'slug': 'business'},
]

for cat_data in categories:
    Category.objects.get_or_create(**cat_data)

# Create courses
programming_cat = Category.objects.get(slug='programming')

courses = [
    {
        'title': 'Python for Beginners',
        'slug': 'python-beginners',
        'short_description': 'Learn Python from scratch',
        'full_description': 'Complete Python course for beginners',
        'price': 0,
        'is_published': True,
        'is_featured': True,
        'category': programming_cat
    },
    {
        'title': 'Advanced Django',
        'slug': 'advanced-django',
        'short_description': 'Master Django framework',
        'full_description': 'Deep dive into Django web development',
        'price': 999,
        'is_published': True,
        'is_featured': True,
        'category': programming_cat
    },
    {
        'title': 'JavaScript Essentials',
        'slug': 'javascript-essentials',
        'short_description': 'JavaScript fundamentals',
        'full_description': 'Learn JavaScript programming',
        'price': 499,
        'is_published': True,
        'category': programming_cat
    },
]

for course_data in courses:
    Course.objects.get_or_create(**course_data)

print("Sample data created successfully!")