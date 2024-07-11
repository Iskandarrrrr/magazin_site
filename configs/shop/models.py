from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Category')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Name of product')

    content = models.TextField(verbose_name='Content')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update date time')
    publish = models.BooleanField(default=True, verbose_name='Public')
    view = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    price = models.FloatField(default=0, verbose_name='Price')
    video = models.CharField(max_length=500, verbose_name='Link video', blank=True, null=True)

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'https://yandex.ru/images/search?pos=9&from=tabbar&img_url=https%3A%2F%2Fagro96.ru%2FuploadedFiles%2Feshopimages%2Fbig%2Fut000000965.jpg&text=no+photo&rpt=simage&lr=10335'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
