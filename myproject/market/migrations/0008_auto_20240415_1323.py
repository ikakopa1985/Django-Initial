# Generated by Django 3.2.10 on 2024-04-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20240415_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='FKAuthor', to='market.Author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(verbose_name='List Count'),
        ),
    ]
