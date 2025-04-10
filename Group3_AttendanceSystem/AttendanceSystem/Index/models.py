from django.db import models
from django.contrib.auth.models import User

# Add the missing Class model here
class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    year = models.IntegerField(default=2025)

    def __str__(self):
        return self.name

# If you have other models, keep them below
