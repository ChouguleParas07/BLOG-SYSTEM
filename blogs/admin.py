from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'category', 'author', 'is_featured','status', 'created_at']
    search_fields = ['title', 'category__category_name', 'author__username', 'status', 'id']
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog, blogAdmin)