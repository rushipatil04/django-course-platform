from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import PurchaseRequest
from courses.models import Course, Enrollment
from accounts.models import User

@staff_member_required
def admin_dashboard(request):
    pending_purchases = PurchaseRequest.objects.filter(status='pending').order_by('-created_at')
    recent_purchases = PurchaseRequest.objects.all().order_by('-created_at')[:10]
    
    stats = {
        'total_users': User.objects.count(),
        'total_courses': Course.objects.count(),
        'pending_purchases': pending_purchases.count(),
        'total_enrollments': Enrollment.objects.count(),
    }
    
    context = {
        'pending_purchases': pending_purchases,
        'recent_purchases': recent_purchases,
        'stats': stats,
    }
    return render(request, 'admin/dashboard.html', context)

@staff_member_required
def approve_purchase(request, pk):
    purchase = get_object_or_404(PurchaseRequest, pk=pk)
    
    if request.method == 'POST':
        purchase.status = 'approved'
        purchase.admin_comments = request.POST.get('comments', '')
        purchase.save()
        
        # Create enrollment
        Enrollment.objects.get_or_create(
            user=purchase.user,
            course=purchase.course
        )
        
        messages.success(request, f'Purchase approved for {purchase.user.email}')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/approve_purchase.html', {'purchase': purchase})

@staff_member_required
def reject_purchase(request, pk):
    purchase = get_object_or_404(PurchaseRequest, pk=pk)
    
    if request.method == 'POST':
        purchase.status = 'rejected'
        purchase.admin_comments = request.POST.get('comments', '')
        purchase.save()
        
        messages.warning(request, f'Purchase rejected for {purchase.user.email}')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/reject_purchase.html', {'purchase': purchase})