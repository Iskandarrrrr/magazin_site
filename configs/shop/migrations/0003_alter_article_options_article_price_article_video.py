# Generated by Django 4.2.11 on 2024-04-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_article_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Link video'),
        ),
    ]
