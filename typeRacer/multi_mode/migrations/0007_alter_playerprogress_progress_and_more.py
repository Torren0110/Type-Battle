# Generated by Django 4.1.7 on 2023-07-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_mode', '0006_alter_lobby_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprogress',
            name='progress',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playerprogress',
            name='wpm',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
