from django.db import models
from django.conf import settings
from apps.equipment.models import Equipment

class Defect(models.Model):
    STATUS_CHOICES = [
        ('reported', 'Сообщено'),
        ('in_progress', 'В работе'),
        ('resolved', 'Решено'),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Деффект {self.equipment.name} - {self.get_status_display()}"