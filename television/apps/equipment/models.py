from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('available', 'Доступно'),
        ('reserved', 'Забронировано'),
        ('broken', 'Сломано'),
    ])
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
