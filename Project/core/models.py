from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Computer(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y', blank=True, verbose_name='Картинка товара',
                              default='../static/images/comp_default.jpg')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:computer_detail', args=[self.id, self.slug])


class Order(models.Model):
    user = models.ForeignKey(User, related_name='user_cart', blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Computer, on_delete=models.CASCADE, blank=False)
    count = models.IntegerField(validators=[MinValueValidator(0)], default=0)
