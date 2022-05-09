# Generated by Django 4.0.4 on 2022-05-07 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPosteo', models.DateField()),
                ('tituloPosteo', models.CharField(max_length=130)),
                ('bodyPosteo', models.TextField()),
                ('autorPosteo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Posteo',
                'verbose_name_plural': 'Posteos',
            },
        ),
    ]