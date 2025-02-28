from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('operator', 'Оператор'),
        ('technician', 'Техник'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",  
        blank=True
    )