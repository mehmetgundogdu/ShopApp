from django.contrib import admin
from .models import Category, Brand, BrandModel, Product, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Brand, BrandAdmin)

class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(BrandModel, BrandModelAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'price', 'stock', 'avaiable']
    list_filter = ['avaiable', 'created', 'updated']
    list_editable = ['price', 'stock', 'avaiable']
admin.site.register(Product, ProductAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = ['created_on', 'text']
    list_filter = ['created_on']
    list_editable = ['text']

    
admin.site.register(Comment, CommentAdmin)


