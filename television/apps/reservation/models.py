from django.db import models
from apps.users.models import CustomUser
from apps.equipment.models import Equipment

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('approved', 'Подтверждено'),
        ('rejected', 'Отклонено'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)  
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField()  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  

    def __str__(self):
        return f"{self.equipment} ({self.status})"