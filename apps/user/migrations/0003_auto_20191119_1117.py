# Generated by Django 2.2.7 on 2019-11-19 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0002_remove_needs_matchresult'),
        ('user', '0002_auto_20191118_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmers',
            name='completedNeed',
        ),
        migrations.RemoveField(
            model_name='farmers',
            name='ingNeed',
        ),
        migrations.CreateModel(
            name='FarmersGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='组号')),
                ('type', models.IntegerField(choices=[(-1, '未设置'), (1, '木工'), (2, '泥瓦工')], default=-1, verbose_name='工种')),
                ('memberNumber', models.IntegerField(default=1, verbose_name='组内人数')),
                ('leader', models.CharField(max_length=1000, null=True, verbose_name='组长')),
                ('ingNeed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needs.Needs', verbose_name='进行中需求')),
            ],
        ),
        migrations.AddField(
            model_name='farmers',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.FarmersGroup'),
            preserve_default=False,
        ),
    ]
