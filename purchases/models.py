from django.db import models
from accounts.models import User
from courses.models import Course

class PurchaseRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_requests')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchase_requests')
    screenshot = models.ImageField(upload_to='payment_screenshots/')
    transaction_id = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    admin_comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.course.title} - {self.status}"