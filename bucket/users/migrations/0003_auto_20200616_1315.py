# Generated by Django 2.2.13 on 2020-06-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200606_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketuser',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Bio'),
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
