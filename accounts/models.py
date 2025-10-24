import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Remove these lines - use default Django authentication
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email if self.email else self.username