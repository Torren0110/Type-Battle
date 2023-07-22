# Generated by Django 4.1.7 on 2023-07-21 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_mode', '0007_alter_playerprogress_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='playerCount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5, message='There can only be 5 player at max in a lobby.')]),
        ),
    ]
