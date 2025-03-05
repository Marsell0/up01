from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступно'),
        ('booked', 'Забронировано'),
        ('maintenance', 'На ремонте'),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
