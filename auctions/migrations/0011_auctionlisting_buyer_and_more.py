# Generated by Django 4.1.1 on 2022-09-30 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0010_alter_auctionlisting_listed_by_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="buyer",
            field=models.ForeignKey(
                blank=True,
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="winners",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="auctionlisting",
            name="time_listed",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="bid",
            name="bid_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buyers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="bid",
            name="bid_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
