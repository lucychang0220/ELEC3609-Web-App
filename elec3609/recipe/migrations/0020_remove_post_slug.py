# Generated by Django 3.1.1 on 2020-10-30 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0019_merge_20201030_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]