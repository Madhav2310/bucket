# Generated by Django 2.2.13 on 2020-07-31 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketuser',
            name='bio',
            field=models.TextField(blank=True, max_length=100, verbose_name='Bio'),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.BucketUser')),
            ],
        ),
        migrations.AddField(
            model_name='bucketuser',
            name='content_bookmark',
            field=models.ManyToManyField(related_name='content_bookmarked_by', through='users.Bookmark', to='subjects.Content'),
        ),
    ]
