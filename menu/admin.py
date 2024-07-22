from django.contrib import admin
from .models import Menu, Category
# Register your models here.
@admin.register(Menu)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

