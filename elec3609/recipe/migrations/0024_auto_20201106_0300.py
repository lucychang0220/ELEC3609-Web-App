# Generated by Django 3.1.2 on 2020-11-05 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0023_post_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picture',
            new_name='post_img',
        ),
    ]
