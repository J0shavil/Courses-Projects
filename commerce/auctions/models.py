from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

class Listings(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    starting_bid = models.FloatField(null=False, blank=False)
    class Category(models.IntegerChoices):
        Fashion = 1
        Toys = 2
        Electronics = 3
        Home = 4
        Books = 5
        Videogames = 6
    category = models.IntegerField(null=True, choices=Category.choices)
    image = models.URLField(null=True)
    date = models.DateField(auto_now_add=True)
    highest_bid =models.ForeignKey('Bids', on_delete=models.SET_NULL, null=True, related_name="winning_bid")
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Listings" 

    def __str__(self):
        return f"Username: {self.user.username}     Listing:{ self.title} "
    
    

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    listing  = models.ForeignKey(Listings, on_delete = models.CASCADE)  
    bid_amount = models.FloatField(null=False, blank=False)
    winner_status = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Bids" 

    def __str__(self):
        return f"Username:{self.user.username} || Listing:{ self.listing.title} || Bid amount:{self.bid_amount}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="watchlists")
    listings = models.ManyToManyField(Listings, related_name="watchlists")
    

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    listing  = models.ForeignKey(Listings, on_delete = models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    #handle the adding of an extra plural char in the admin
    class Meta:
        verbose_name_plural = "Comments" 

    def __str__(self):
        return f"Username: { self.user.username} || Listing: {self.listing.title} || Comment: {self.comment} " 