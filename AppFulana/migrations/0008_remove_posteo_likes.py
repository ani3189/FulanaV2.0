# Generated by Django 4.0.4 on 2022-05-27 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFulana', '0007_alter_posteo_bodyposteo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='likes',
        ),
    ]
