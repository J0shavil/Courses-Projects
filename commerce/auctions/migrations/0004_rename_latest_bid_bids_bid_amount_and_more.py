# Generated by Django 5.0.1 on 2024-01-09 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_listings_other_category_bids_initial_bid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='latest_bid',
            new_name='bid_amount',
        ),
        migrations.RemoveField(
            model_name='bids',
            name='initial_bid',
        ),
        migrations.AddField(
            model_name='bids',
            name='listing',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctions.listings'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listings', models.ManyToManyField(related_name='watchlists', to='auctions.listings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
