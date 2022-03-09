from django.db import models
from django.urls import reverse

class Computer(models.Model):
    comp_name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.comp_name
    
    # def get_absolute_url(self):
    #     return reverse('result', kwargs={'result_slug': self.slug})
    
    class Meta:
        verbose_name = 'Компьютеры'
        verbose_name_plural = 'Компьютеры'
        ordering = ['comp_name', 'price']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['id']
