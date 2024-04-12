from django.db import models

# Create your models here.


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name="  კატეგორია", related_name='FKcategpry')
    author = models.ManyToManyField('Author', verbose_name=' კატეგორია',  related_name='FKAuthor')
    name = models.CharField(max_length=255, verbose_name=' წიგნის დასახელება')
    page_count = models.IntegerField(verbose_name=' ფურცლების რაოდენობა')
    price = models.FloatField(null=True, blank=True, verbose_name=" ფასი")
    image = models.ImageField(upload_to='mediafiles/', null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=" შექმნის თარიღი")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " წიგნები"
        verbose_name = " წიგნი"


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="  კატეგორია")

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,

    class Meta:
        verbose_name_plural = " კატეგორიები"
        verbose_name = " კატეგორია"
    

class Author(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="  ავტორი")

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,

    class Meta:
        verbose_name_plural = " ავტორები"
        verbose_name = " ავტორი"

