from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)

class Trail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ("Iniciante", "Iniciante"),
            ("Intermediário", "Intermediário"),
            ("Avançado", "Avançado")
        ]
    )
    duration = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Exercise(models.Model):
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    achieved_at = models.DateTimeField(auto_now_add=True)
