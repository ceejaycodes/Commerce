# Generated by Django 4.1.1 on 2022-09-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0006_alter_auctionlisting_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="auctionlisting",
            name="item",
            field=models.CharField(max_length=75),
        ),
    ]
