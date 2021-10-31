from django.contrib import admin

from users.models import CustomUser
# from django.contrib.auth
# Register your models here.
admin.site.register(CustomUser)