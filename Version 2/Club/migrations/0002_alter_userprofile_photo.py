# Generated by Django 4.1.1 on 2022-11-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Club", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="pics"),
        ),
    ]
