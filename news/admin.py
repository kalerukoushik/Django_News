from django.contrib import admin
from .models import Reporter, Article

# Register your models here.
admin.site.register(Article)
admin.site.register(Reporter)
