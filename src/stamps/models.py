from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, blank=True, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse_lazy("stamps:category", args=[self.slug])

    def get_groups(self):
        groups = Group.objects.filter(category=self)
        return groups

    def __str__(self):
        return self.name


def categry_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)


pre_save.connect(categry_pre_save_receiver, sender=Category)


class Group(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="groups")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "group"
        verbose_name_plural = "groups"

    def get_absolute_url(self):
        return reverse_lazy("stamps:group", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


def group_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)


pre_save.connect(group_pre_save_receiver, sender=Group)


class ProductManager(models.Manager):
    def all(self):
        qs = self.get_queryset().all()
        qs = qs.filter(availible=True)
        return qs


class Product(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, blank=True, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="products")
    availible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    class Meta:
        ordering = ('name',)
        verbose_name = "product"
        verbose_name_plural = "products"

    def get_absolute_url(self):
        return reverse_lazy("stamps:product", args=[self.group.category.slug, self.group.slug, self.slug])

    def __str__(self):
        return self.name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
