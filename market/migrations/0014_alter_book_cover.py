# Generated by Django 4.2 on 2024-04-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_rename_products_category_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('hard', 'Hard cover'), ('soft', 'Soft cover'), ('special', 'Special cover')], max_length=30, verbose_name='cover'),
        ),
    ]
