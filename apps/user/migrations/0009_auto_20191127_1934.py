# Generated by Django 2.2.7 on 2019-11-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20191126_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmers',
            name='type',
            field=models.CharField(default='未设置', max_length=2000, verbose_name='工种'),
        ),
    ]
