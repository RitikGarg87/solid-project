from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class Myuseradmin(admin.ModelAdmin):
    list_display = ['id','fullname','phone']