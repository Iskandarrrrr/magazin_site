# Generated by Django 4.2.11 on 2024-04-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Image'),
        ),
    ]
