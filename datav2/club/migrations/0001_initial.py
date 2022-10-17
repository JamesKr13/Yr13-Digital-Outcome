# Generated by Django 4.1.1 on 2022-09-15 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("photo", models.ImageField(upload_to="pics")),
            ],
        ),
        migrations.CreateModel(
            name="Meeting_Days",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                        ],
                        default="Monday",
                        max_length=10,
                    ),
                ),
                ("time", models.CharField(default="2", max_length=10)),
                (
                    "period_name",
                    models.CharField(
                        choices=[("L", "Lunch"), ("M", "Morning Tea")],
                        default="Lunch",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("first_text_field", models.CharField(default="", max_length=300)),
                ("second_text_field", models.CharField(default="", max_length=300)),
                (
                    "day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="club.meeting_days",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.image"
                    ),
                ),
            ],
        ),
    ]