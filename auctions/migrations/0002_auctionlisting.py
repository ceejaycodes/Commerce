# Generated by Django 4.1.1 on 2022-09-25 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuctionListing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=75)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="uploads")),
                (
                    "listed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owners",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
