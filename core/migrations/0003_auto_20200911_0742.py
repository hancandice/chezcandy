# Generated by Django 2.2.8 on 2020-09-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200911_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='contents',
        ),
        migrations.AddField(
            model_name='item',
            name='contents_long',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='contents_short',
            field=models.TextField(blank=True, null=True),
        ),
    ]
