# Generated by Django 4.2.4 on 2023-08-17 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('cover_image', models.FileField(upload_to='project-image')),
                ('category', models.CharField(max_length=50)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.hero')),
            ],
        ),
    ]
