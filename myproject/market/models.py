from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name=_('Category'),
                                 related_name='FKcategpry')
    author = models.ManyToManyField('Author', verbose_name=_('Author'),  related_name='FKAuthor')
    name = models.CharField(max_length=255, verbose_name=_('Book Name'))
    page_count = models.IntegerField(verbose_name=_('List Count'))
    price = models.FloatField(null=True, blank=True, verbose_name=_("Price"))
    image = models.ImageField(upload_to='mediafiles/', null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("books")
        verbose_name = _("book")


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name=_('Category'))

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,

    class Meta:
        verbose_name_plural = _('Categoryes')
        verbose_name = _('Category')
    

class Author(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name=_('Author'))

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,

    class Meta:
        verbose_name_plural = _('Authors')
        verbose_name = _('Author')
