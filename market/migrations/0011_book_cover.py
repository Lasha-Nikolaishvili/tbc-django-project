# Generated by Django 4.2 on 2024-04-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('hard', 'Hard'), ('soft', 'Soft'), ('special', 'Special')], default='hard', max_length=30, verbose_name='cover'),
            preserve_default=False,
        ),
    ]