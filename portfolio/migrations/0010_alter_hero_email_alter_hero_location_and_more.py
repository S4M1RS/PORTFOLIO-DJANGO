# Generated by Django 4.2.4 on 2023-08-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_hero_email_hero_location_hero_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='hero',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hero',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
