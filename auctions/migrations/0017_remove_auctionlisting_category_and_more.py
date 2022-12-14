# Generated by Django 4.1.1 on 2022-10-08 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0016_rename_bid_amount_bid_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="category",
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Categories",
                to="auctions.categories",
            ),
        ),
    ]
