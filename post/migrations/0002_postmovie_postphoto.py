# Generated by Django 4.2.7 on 2023-12-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostMovie",
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
                ("title", models.CharField(max_length=20, unique=True)),
                ("video", models.FileField(upload_to="posts/")),
            ],
        ),
        migrations.CreateModel(
            name="PostPhoto",
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
                ("title", models.CharField(max_length=20, unique=True)),
                ("photo", models.ImageField(blank=True, upload_to="post_images/")),
            ],
        ),
    ]
