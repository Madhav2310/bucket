# Generated by Django 2.2.13 on 2020-07-14 06:27

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True, verbose_name='Slug')),
                ('type', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('documentary', 'Documentary'), ('website', 'Website'), ('youtube_channel', 'Youtube Channel'), ('social_media', 'Social Media'), ('other', 'Other')], default='other', max_length=150, verbose_name='Type')),
                ('creator', models.CharField(blank=True, max_length=255, verbose_name='Creator')),
                ('image', models.ImageField(blank=True, null=True, upload_to='content_images', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('content_url', models.URLField(blank=True, default='', null=True, verbose_name='URL')),
                ('bookmarked_by', models.ManyToManyField(blank=True, related_name='content_bookmark', to='users.BucketUser', verbose_name='Bookmarked By')),
                ('subject', models.ManyToManyField(blank=True, related_name='content', to='subjects.Subject')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]