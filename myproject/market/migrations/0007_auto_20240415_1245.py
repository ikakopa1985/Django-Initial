# Generated by Django 3.2.10 on 2024-04-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='FKAuthor', to='market.Author', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Book Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=''),
        ),
    ]
