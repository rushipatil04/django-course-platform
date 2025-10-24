from django.contrib import admin
from .models import Category, Course, Content, Enrollment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured', 'category')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ContentInline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at', 'completed')
    list_filter = ('completed', 'enrolled_at')