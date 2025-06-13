from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPES = (
        ('TEA', 'Чай'),
        ('COFFEE', 'Кава'),
        ('ACCESSORY', 'Аксесуар'),
        ('OTHER', 'Інше'),
    )

    name = models.CharField(max_length=200, verbose_name="Назва продукту")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name="Категорія")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    description = models.TextField(blank=True, verbose_name="Детальний опис")
    stock_quantity = models.IntegerField(default=0, verbose_name="Кількість на складі")
    is_available = models.BooleanField(default=True, verbose_name="Доступний")
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='OTHER', verbose_name="Тип товару")

    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        unique_together = ('name', 'category')
        ordering = ['-added_date']

    def __str__(self):
        return f"{self.name} ({self.category.name if self.category else 'Без категорії'})"