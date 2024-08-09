from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.user.username} - {self.role.name if self.role else 'No Role'}"

    def save(self, *args, **kwargs):
        if self.role is None:
            self.role, created = Role.objects.get_or_create(name='No Role')
        super().save(*args, **kwargs)
