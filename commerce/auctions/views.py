from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listings, Watchlist, Bids, Comments


def index(request):
    if request.method == "POST":
        if request.POST["category"] == "None":
            all_listings = Listings.objects.all()
            category_list = Listings.Category.choices
            return render(request, "auctions/index.html", {
            "listings":all_listings,
            "category_list": category_list
            })
        category_list = Listings.Category.choices
        chosen_category = request.POST["category"]
        category_filter = Listings.objects.filter(category=chosen_category)
        return render(request, "auctions/index.html", {
        "listings": category_filter,
        "category_list": category_list
        })

        
    else:
        all_listings = Listings.objects.all()
        category_list = Listings.Category.choices

        return render(request, "auctions/index.html", {
        "listings":all_listings,
        "category_list": category_list
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

 # create a new listing  
@login_required
def new_listing(request):
    category_items = Listings.Category.choices
    if request.method == "POST":
        if request.POST["category"] != "None":
            category = request.POST["category"]
        else:
            return render(request, "auctions/newlisting.html", {
            "categories": category_items,
            "message": "Please choose a category for your item."
        })

        if request.POST["title"] == "":
            return render(request, "auctions/newlisting.html", {
            "categories": category_items,
            "message_title": "Please write a title for your item."
        })

        if request.POST["starting_bid"] == "":
            return render(request, "auctions/newlisting.html", {
            "categories": category_items,
            "message_bid": "Please add a starting bid for your item."
        })

        Listings.objects.create(
            user = request.user,
            title = request.POST["title"],
            description = request.POST["description"],
            category = category,
            starting_bid = request.POST["starting_bid"],
            image= request.POST["image"],
        )
        
        return redirect('index')

    else:
        return render(request, "auctions/newlisting.html", {
            "categories": category_items
        })
# retrieve or create a new watchlist    
@login_required
def watchlist(request):
    try:
        if request.method == "POST":
            watchlist, created = Watchlist.objects.get_or_create (
                user = request.user,
            )

            if request.POST["watchlist_id"] is not None:
                listing_id = request.POST["watchlist_id"]
            watchlist.listings.add(listing_id)

            return HttpResponseRedirect(reverse("listingpage", kwargs={'listing_id':listing_id}))
        
        else:
            watchlist, created = Watchlist.objects.get_or_create (
                user = request.user,
            )
            return render(request, "auctions/watchlist.html", {
                "listings": watchlist.listings.all()
            })
    except(TypeError):
        pass

#remove listing from watchclist
def watchlist_remove(request):
    if request.method == "POST":
        watchlist = Watchlist.objects.get(
            user = request.user,
        )
        #if the request is coming from the listing page, render the listing page
        if request.POST.get("pagelisting") is not None:
            listing_id = request.POST["pagelisting"]
            watchlist.listings.remove(listing_id)
            return HttpResponseRedirect(reverse("listingpage", args=[listing_id]))

        #if the request is coming from the watchlist page  
        elif request.POST.get("watchlisting") is not None:
            listing_id = request.POST["watchlisting"]
            watchlist.listings.remove(listing_id)
            return redirect("watchlist")
            

    else:
        return redirect("watchlist")

# information to be shown in each listing
def listing_page(request,listing_id):
    listing = Listings.objects.get(pk=listing_id)
    comments = Comments.objects.filter(listing = listing)
    watchlist = None
    user = request.user

    if request.user.is_authenticated:
        # create watchlist if user still doesn't have one
        watchlist, created = Watchlist.objects.get_or_create (
                user = user,
            )
    else:
        #if there's no user logged in, user is set to none so that the listing is still viewable
        user = None
    try:
        #check if there's already a bid on the auction
        bids = Bids.objects.get(pk=listing.highest_bid.id)
    except(AttributeError):
        bids = None

    return render(request, 'auctions/listingpage.html', {
        "listings": listing,
        "user": user,
        "bids": bids,
        "watchlist":watchlist,
        "comments": comments
    })

#Get the value from user and post a new bid
@login_required
def post_bid(request):
    user = request.user
    if request.method == "POST":
        listing_id = request.POST["listings_id"]
        listing = Listings.objects.get(pk=listing_id)
        starting_bid = float(request.POST["startingbid"])

        try:  
            bid_post = float(request.POST["bid"])
        except(ValueError):
            return render(request, "auctions/listingpage.html", {
                "listings": listing,
                "user": user,
                "message": "Please input a bid."
            })
    
        
        if bid_post <= starting_bid:
            return render(request, "auctions/listingpage.html", {
                "listings": listing,
                "user": user,
                "message": "Bid Must be higher than starting bid."
            })
        #ensure that highest_bid is already set
        if request.POST["highest_bid"] != "":
            highest_bid = float(request.POST["highest_bid"])
            if bid_post <= highest_bid:
                return render(request, "auctions/listingpage.html", {
                    "listings": listing,
                    "user": user,
                    "message": "Bid Must be equal or higher than the highest bid."
                })

        bid = Bids.objects.create(
            user=user,
            listing=listing,
            bid_amount=bid_post                                           
        )
        bid.save()

        if bid_post > starting_bid:
            listing.highest_bid = bid
            listing.save()
            watchlist, created = Watchlist.objects.get_or_create (
                user = request.user,
            )
            watchlist.listings.add(listing_id)

        return HttpResponseRedirect(reverse("listingpage", args=[listing_id]))
    else:
        return render(request, "auctions/listingpage.html", {
                "listings": listing,
                "user": user,
            })

# close auction and assign the winner of the auction
@login_required
def auction_close(request):
    user = request.user
    listing_id = request.POST["listing"]
    listing = Listings.objects.get(pk=listing_id)
    listing.status = False
    try:
        bids = Bids.objects.get(pk=listing.highest_bid.id)
        bids.winner_status = True
        bids.save()
    except(AttributeError):
        pass
    listing.save()
    
    return  render(request, "auctions/listingpage.html", {
                "listings": listing,
                "user": user,
            })

# creating new comments for a specific listing
@login_required
def comment(request):
    user = request.user
    listing = request.POST["listing"]
    listing_instance = Listings.objects.get(pk=listing)
    comments = Comments.objects.filter(listing = listing)
    watchlist = Watchlist.objects.get(user=user)
    if request.POST["comment"] != "":
        comment = request.POST["comment"]
    else:
        return render(request, "auctions/listingpage.html", {
                "listings": listing_instance,
                'comments': comments,
                'comment_message': "Please write your comment before submitting.",
                'watchlist':watchlist
            })
    user = request.user
    
    new_comment = Comments.objects.create(
        user = user,
        listing = listing_instance,
        comment = comment
    )
    
    return render(request, "auctions/listingpage.html", {
                "listings": listing_instance,
                "user": user,
                'comments': comments
            })