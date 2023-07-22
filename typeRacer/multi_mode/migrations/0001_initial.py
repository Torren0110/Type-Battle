# Generated by Django 4.1.7 on 2023-07-21 14:12

from django.db import migrations, models
import django.db.models.deletion
import multi_mode.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('racer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerCount', models.PositiveIntegerField()),
                ('difficulty', models.PositiveIntegerField()),
                ('startTime', models.DateTimeField(default=multi_mode.util.getStartTime)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racer.passage')),
            ],
        ),
    ]
