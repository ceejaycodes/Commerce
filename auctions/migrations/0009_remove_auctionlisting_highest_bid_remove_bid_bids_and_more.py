# Generated by Django 4.1.1 on 2022-09-29 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0008_remove_categories_items_auctionlisting_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="highest_bid",
        ),
        migrations.RemoveField(
            model_name="bid",
            name="bids",
        ),
        migrations.AddField(
            model_name="bid",
            name="bid_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name="auctionlisting",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.CreateModel(
            name="Watchlist",
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
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="watchitems",
                        to="auctions.auctionlisting",
                    ),
                ),
                (
                    "watchers",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="watchers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]