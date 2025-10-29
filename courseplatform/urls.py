from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from courses.views import home, course_list, course_detail, course_content
from accounts.views import register, profile, my_courses, my_purchases, custom_login
from purchases.views import purchase_course
from purchases.admin_views import admin_dashboard, approve_purchase, reject_purchase

urlpatterns = [
    # Home
    path('', home, name='home'),
    
    # Authentication
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # User Dashboard
    path('profile/', profile, name='profile'),
    path('my-courses/', my_courses, name='my_courses'),
    path('my-purchases/', my_purchases, name='my_purchases'),
    
    # Courses
    path('courses/', course_list, name='course_list'),
    path('course/<slug:slug>/', course_detail, name='course_detail'),
    path('course/<slug:slug>/content/', course_content, name='course_content'),
    path('course/<slug:slug>/purchase/', purchase_course, name='purchase_course'),
    
    # Custom Admin Dashboard (moved before Django admin to avoid conflicts)
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('purchase/<int:pk>/approve/', approve_purchase, name='approve_purchase'),  # Changed URL
    path('purchase/<int:pk>/reject/', reject_purchase, name='reject_purchase'),    # Changed URL
    
    # Django Admin (must be last to avoid catching custom URLs)
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)