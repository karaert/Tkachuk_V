from django.db import models

class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=50, unique=True)
    description = models.TextField('Опис', blank=True)
    is_active = models.BooleanField('Активна', default=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Назва товару', max_length=100, db_index=True)
    description = models.TextField('Опис', blank=True)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія', related_name='products')
    stock = models.PositiveIntegerField('Кількість на складі', default=0)
    is_available = models.BooleanField('Доступний', default=True)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField('Дата оновлення', auto_now=True)
    sku = models.CharField('Артикул', max_length=30, unique=True, default='SKU0000')
    image_url = models.URLField('Посилання на зображення', blank=True, null=True)
    
    def __str__(self):
        return self.name