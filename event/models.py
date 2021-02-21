from django.db import models
from django.contrib import admin

# Create your models here.

class event(models.Model):
    email = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    year=models.IntegerField()

class eventAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'year')