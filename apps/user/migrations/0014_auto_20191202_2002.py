# Generated by Django 2.2.7 on 2019-12-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20191202_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreman',
            name='Bank',
            field=models.CharField(max_length=100, null=True, verbose_name='银行'),
        ),
        migrations.AddField(
            model_name='foreman',
            name='BankNumber',
            field=models.CharField(max_length=1000, null=True, verbose_name='银行卡号'),
        ),
    ]
