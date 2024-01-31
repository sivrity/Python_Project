from django.contrib import admin
from project import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Project_Post)
admin.site.register(models.Comment)