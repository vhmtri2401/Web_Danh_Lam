# Generated by Django 5.0.6 on 2024-05-18 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='image',
        ),
    ]