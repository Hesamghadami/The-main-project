# Generated by Django 4.2.2 on 2023-06-21 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custumuser',
            name='id_code',
        ),
    ]
