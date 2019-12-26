from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=2000, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    blocked = models.BooleanField(default=False)

    class Meta:
        ordering = ('user',)
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username
