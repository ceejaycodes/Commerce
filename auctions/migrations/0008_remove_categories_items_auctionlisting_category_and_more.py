# Generated by Django 4.1.1 on 2022-09-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0007_auctionlisting_active_alter_auctionlisting_item"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categories",
            name="items",
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="category",
            field=models.ManyToManyField(
                blank=True, related_name="Categories", to="auctions.categories"
            ),
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="description",
            field=models.TextField(blank=True, help_text="Description"),
        ),
    ]
