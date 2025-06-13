from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_available', 'type', 'added_date')
    list_filter = ('is_available', 'type', 'category', 'added_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'added_date'
    raw_id_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'type', 'description')
        }),
        ('Наявність та кількість', {
            'fields': ('stock_quantity', 'is_available'),
            'classes': ('collapse',),
        }),
    )
