# Generated by Django 5.0.1 on 2024-01-10 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_listings_highest_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='highest_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winning_bid', to='auctions.bids'),
        ),
    ]
