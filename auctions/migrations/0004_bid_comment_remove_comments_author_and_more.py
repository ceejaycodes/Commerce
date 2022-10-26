# Generated by Django 4.1.1 on 2022-09-26 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_comments_bids"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bid",
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
                ("bids", models.IntegerField()),
                ("bid_time", models.DateTimeField(auto_now=True)),
                (
                    "bid_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("comment", models.TextField(help_text="Please Leave A Review")),
                ("time", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authors",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="comments",
            name="author",
        ),
        migrations.RemoveField(
            model_name="comments",
            name="item",
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="time_listed",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="auctionlisting",
            name="item",
            field=models.CharField(help_text="Product Name", max_length=75),
        ),
        migrations.DeleteModel(
            name="Bids",
        ),
        migrations.DeleteModel(
            name="Comments",
        ),
        migrations.AddField(
            model_name="comment",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="auctions.auctionlisting",
            ),
        ),
        migrations.AddField(
            model_name="bid",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="auctions.auctionlisting",
            ),
        ),
        migrations.AddField(
            model_name="bid",
            name="listed_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sellers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
