from django.contrib import admin

# Register your models here.
from .models import Cat, CatBreed

admin.site.register(Cat)
admin.site.register(CatBreed)