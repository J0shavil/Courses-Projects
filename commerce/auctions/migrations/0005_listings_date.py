# Generated by Django 5.0.1 on 2024-01-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_latest_bid_bids_bid_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='date',
            field=models.DateField(auto_now_add=True, default='2014-01-09'),
            preserve_default=False,
        ),
    ]
