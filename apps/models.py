from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, PositiveIntegerField, TextField, ImageField, \
    DateTimeField, BooleanField
from django.forms import DecimalField


class User(AbstractUser):
    phone_number = CharField(max_length=11, blank=True)


class Category(Model):
    name = CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=120)
    price = PositiveIntegerField()
    count = PositiveIntegerField()
    description = TextField()
    image = ImageField(upload_to='products/')
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_archived = BooleanField(default=False)

    def __str__(self):
        return self.name



