# Generated by Django 4.2 on 2024-04-08 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_author_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
    ]