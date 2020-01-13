from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your models here.


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ADDRESS_TYPE_CHOICES = (
    ('Home', 'Home'),
    ('Work', 'Work'),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profiles", blank=True, null=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    blocked = models.BooleanField(default=False)

    class Meta:
        ordering = ('user',)
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def get_absolute_url(self):
        return reverse_lazy("accounts:profile", kwargs={"slug": self.user.username})

    def __str__(self):
        return self.user.username


class Address(models.Model):
    address_type = models.CharField(max_length=4, choices=ADDRESS_TYPE_CHOICES)
    address = models.TextField(max_length=2000)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.PositiveIntegerField()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        ordering = ('address',)
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return str(self.address)
