# Generated by Django 3.1.1 on 2020-10-23 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_merge_20201022_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
