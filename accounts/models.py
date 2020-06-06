from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models.signals import post_save
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
    image = models.ImageField(
        upload_to="media/profiles", blank=True, null=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    blocked = models.BooleanField(default=False)

    class Meta:
        db_table = 'profile'
        ordering = ('user',)
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def get_absolute_url(self):
        return reverse_lazy("accounts:profile", kwargs={"slug": self.user.username})

    def __str__(self):
        return self.user.username


# When a user is created a profile will be created for him
def post_save_user_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_created_receiver, sender=User)


class Address(models.Model):
    address_type = models.CharField(max_length=5, choices=ADDRESS_TYPE_CHOICES)
    address = models.TextField(max_length=2000)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.PositiveIntegerField()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        db_table = 'address'
        ordering = ('address',)
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return str(self.address)
