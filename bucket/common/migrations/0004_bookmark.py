# Generated by Django 2.2.13 on 2020-07-25 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0001_initial'),
        ('common', '0003_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('plan_to_watch', 'Plan to watch'), ('on_hold', 'On-hold'), ('dropped', 'Dropped'), ('not_interested', 'Not interested')], default='completed', max_length=150, verbose_name='Status')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='public', max_length=150, verbose_name='Visibility')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.BucketUser')),
            ],
        ),
    ]
