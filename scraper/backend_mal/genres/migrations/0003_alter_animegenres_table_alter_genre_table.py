# Generated by Django 4.1.7 on 2023-03-23 05:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("genres", "0002_alter_animegenres_options_alter_genre_options"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="animegenres",
            table="anime_genres",
        ),
        migrations.AlterModelTable(
            name="genre",
            table="genre",
        ),
    ]