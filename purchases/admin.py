from django.contrib import admin
from .models import PurchaseRequest

@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'status', 'transaction_id', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email', 'course__title', 'transaction_id')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Request Information', {
            'fields': ('user', 'course', 'screenshot')
        }),
        ('Payment Details', {
            'fields': ('transaction_id', 'notes')
        }),
        ('Admin Review', {
            'fields': ('status', 'admin_comments')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )