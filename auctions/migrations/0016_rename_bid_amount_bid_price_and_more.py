# Generated by Django 4.1.1 on 2022-10-07 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0015_auctionlisting_watchers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bid",
            old_name="bid_amount",
            new_name="price",
        ),
        migrations.RemoveField(
            model_name="auctionlisting",
            name="price",
        ),
        migrations.RemoveField(
            model_name="bid",
            name="bid_time",
        ),
        migrations.RemoveField(
            model_name="bid",
            name="item",
        ),
        migrations.RemoveField(
            model_name="bid",
            name="listed_by",
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="bid",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="current_bid",
                to="auctions.bid",
            ),
            preserve_default=False,
        ),
    ]
