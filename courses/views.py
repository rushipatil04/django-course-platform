from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Course, Category, Content, Enrollment

def home(request):
    print("HOME VIEW CALLED!")  # Add this line for debugging
    featured_courses = Course.objects.filter(is_published=True, is_featured=True)[:3]
    free_courses = Course.objects.filter(is_published=True, price=0)[:3]
    paid_courses = Course.objects.filter(is_published=True, price__gt=0)[:3]
    
    context = {
        'featured_courses': featured_courses,
        'free_courses': free_courses,
        'paid_courses': paid_courses,
    }
    print(f"Context: {context}")  # Add this line too
    return render(request, 'home.html', context)

def course_list(request):
    courses = Course.objects.filter(is_published=True)
    
    # Filter by type
    course_type = request.GET.get('type')
    if course_type == 'free':
        courses = courses.filter(price=0)
    elif course_type == 'paid':
        courses = courses.filter(price__gt=0)
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        courses = courses.filter(category__slug=category_slug)
    
    # Search
    search_query = request.GET.get('q')
    if search_query:
        courses = courses.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )
    
    categories = Category.objects.all()
    
    context = {
        'courses': courses,
        'categories': categories,
        'current_category': category_slug,
        'course_type': course_type,
        'search_query': search_query,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    contents = course.contents.all()
    is_enrolled = False
    has_pending_purchase = False
    
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
        has_pending_purchase = course.purchase_requests.filter(
            user=request.user, 
            status='pending'
        ).exists()
    
    context = {
        'course': course,
        'contents': contents,
        'is_enrolled': is_enrolled,
        'has_pending_purchase': has_pending_purchase,
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
def course_content(request, slug):
    course = get_object_or_404(Course, slug=slug)
    
    # Check if user has access
    if course.is_free:
        # Auto-enroll in free course
        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user,
            course=course
        )
    else:
        # Check if user is enrolled
        enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
        if not enrollment:
            messages.error(request, 'You need to purchase this course to access its content.')
            return redirect('course_detail', slug=course.slug)
    
    contents = course.contents.all()
    
    context = {
        'course': course,
        'contents': contents,
        'enrollment': enrollment,
    }
    return render(request, 'courses/course_content.html', context)