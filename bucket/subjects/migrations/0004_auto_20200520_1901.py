# Generated by Django 2.2.11 on 2020-05-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20200520_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='creator',
            field=models.CharField(blank=True, max_length=255, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='content',
            name='link',
            field=models.URLField(blank=True, verbose_name='Link'),
        ),
    ]