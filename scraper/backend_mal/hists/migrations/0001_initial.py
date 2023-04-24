# Generated by Django 4.1.7 on 2023-04-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimeMembersHist",
            fields=[
                ("d_date", models.DateField(primary_key=True, serialize=False)),
                ("members", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "anime_members_hist",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AnimeScoreHist",
            fields=[
                ("d_date", models.DateField(primary_key=True, serialize=False)),
                ("score", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "anime_score_hist",
                "managed": False,
            },
        ),
    ]
