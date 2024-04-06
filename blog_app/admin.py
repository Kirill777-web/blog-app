from django.contrib import admin

# Register your models here.
from .models import Blog, Entry
admin.site.register(Blog)
admin.site.register(Entry)
