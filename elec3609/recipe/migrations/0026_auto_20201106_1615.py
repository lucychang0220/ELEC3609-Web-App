# Generated by Django 3.1.2 on 2020-11-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0025_auto_20201106_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]
