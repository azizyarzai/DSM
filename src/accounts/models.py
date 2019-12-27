from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles", blank=True)
    address = models.TextField(max_length=2000, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    blocked = models.BooleanField(default=False)

    class Meta:
        ordering = ('user',)
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def get_absolute_url(self):
        return reverse_lazy("accounts:profile", kwargs={"slug": self.user.username})

    def __str__(self):
        return self.user.username
