# Generated by Django 4.0.4 on 2022-05-26 04:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFulana', '0006_remove_posteo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='bodyPosteo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
