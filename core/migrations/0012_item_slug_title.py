# Generated by Django 2.2.8 on 2020-09-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200913_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]