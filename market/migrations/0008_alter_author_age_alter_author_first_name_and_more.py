# Generated by Django 4.2 on 2024-04-10 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_remove_book_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='nationality',
            field=models.CharField(max_length=100, verbose_name='nationality'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.author', verbose_name='author name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('horror', 'Horror'), ('mystery', 'Mystery'), ('science fiction', 'Science Fiction'), ('historical fiction', 'Historical Fiction'), ('romance', 'Romance'), ('fantasy', 'Fantasy'), ('autobiography', 'Autobiography'), ('adventure', 'Adventure'), ('history', 'History')], max_length=30, verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=150, verbose_name='book name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(verbose_name='page count'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
    ]
