# Generated by Django 2.2.13 on 2020-06-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0012_auto_20200625_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=150, unique=True, verbose_name='Slug'),
        ),
    ]
