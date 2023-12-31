# Generated by Django 4.2.2 on 2023-06-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='counted_views',
        ),
        migrations.AddField(
            model_name='post',
            name='client_url',
            field=models.CharField(default='#', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
