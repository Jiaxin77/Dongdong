# Generated by Django 2.2.7 on 2019-11-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191119_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='icon',
            field=models.ImageField(null=True, upload_to='head'),
        ),
    ]
