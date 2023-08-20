# Generated by Django 4.2.4 on 2023-08-20 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_hero_email_alter_hero_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='hero',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='hero',
        ),
        migrations.AddField(
            model_name='resume',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.hero'),
        ),
        migrations.AddField(
            model_name='skill',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.hero'),
        ),
    ]