from django.contrib import admin
from django.contrib.auth.models import Group

from apps.models import User, Product, Category

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.unregister(Group)
