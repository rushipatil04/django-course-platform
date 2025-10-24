from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from courses.views import home, course_list, course_detail, course_content
from accounts.views import register, profile, my_courses, my_purchases, custom_login  # Add custom_login
from purchases.views import purchase_course
from purchases.admin_views import admin_dashboard, approve_purchase, reject_purchase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    # Authentication
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),  # Use custom_login instead
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Rest of your URLs remain the same...
    path('profile/', profile, name='profile'),
    path('my-courses/', my_courses, name='my_courses'),
    path('my-purchases/', my_purchases, name='my_purchases'),
    path('courses/', course_list, name='course_list'),
    path('course/<slug:slug>/', course_detail, name='course_detail'),
    path('course/<slug:slug>/content/', course_content, name='course_content'),
    path('course/<slug:slug>/purchase/', purchase_course, name='purchase_course'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/purchase/<int:pk>/approve/', approve_purchase, name='approve_purchase'),
    path('admin/purchase/<int:pk>/reject/', reject_purchase, name='reject_purchase'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)