# Generated by Django 4.1.2 on 2022-10-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_port',
            field=models.SmallIntegerField(default=22, verbose_name='主机port'),
        ),
    ]
