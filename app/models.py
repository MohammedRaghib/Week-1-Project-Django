from django.db import models
from django.utils import timezone

class foods(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return f'Food name: {self.name},\nCalories: {self.calorie}'