import qrcode
import io
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.base import ContentFile
from .models import PurchaseRequest
from courses.models import Course, Enrollment

@login_required
def purchase_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    
    # Check if already enrolled
    if Enrollment.objects.filter(user=request.user, course=course).exists():
        messages.info(request, 'You already have access to this course.')
        return redirect('course_content', slug=course.slug)
    
    # Check for pending purchase
    pending_purchase = PurchaseRequest.objects.filter(
        user=request.user,
        course=course,
        status='pending'
    ).first()
    
    if pending_purchase:
        messages.warning(request, 'You have a pending purchase request for this course.')
        return redirect('my_purchases')
    
    if request.method == 'POST':
        screenshot = request.FILES.get('screenshot')
        transaction_id = request.POST.get('transaction_id', '')
        notes = request.POST.get('notes', '')
        
        if screenshot:
            purchase_request = PurchaseRequest.objects.create(
                user=request.user,
                course=course,
                screenshot=screenshot,
                transaction_id=transaction_id,
                notes=notes
            )
            messages.success(request, 'Your purchase request has been submitted. We will review it shortly.')
            return redirect('my_purchases')
        else:
            messages.error(request, 'Please upload a payment screenshot.')
    
    # Generate QR code
    upi_string = f"upi://pay?pa=merchant@upi&pn=CourseHub&am={course.price}&cu=INR&tn=Course:{course.title}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_string)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    context = {
        'course': course,
        'qr_code': img_str,
        'upi_string': upi_string,
    }
    return render(request, 'purchases/purchase.html', context)