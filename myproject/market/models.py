from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name=' წიგნის დასახელება')
    page_count = models.IntegerField(verbose_name=' ფურცლების რაოდენობა')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name="  კატეგორია")
    author_name = models.CharField(max_length=255, verbose_name=' ავტორი')
    price = models.FloatField(null=True, blank=True, verbose_name=" ფასი")
    image = models.ImageField
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=" შექმნის თარიღი")
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="  კატეგორია")
    def __str__(self):
        return self.name