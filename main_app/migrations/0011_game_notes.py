# Generated by Django 4.1.2 on 2022-11-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_game_max_player_alter_game_min_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='notes',
            field=models.TextField(blank=True, max_length=250, verbose_name='Private notes (e.g., strategy, etc.)'),
        ),
    ]
