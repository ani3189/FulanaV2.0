# Generated by Django 4.0.4 on 2022-05-26 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFulana', '0005_posteo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='slug',
        ),
    ]