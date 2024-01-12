from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.new_listing, name="newlisting"),
    path("<int:listing_id>", views.listing_page, name="listingpage"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlistremove", views.watchlist_remove, name="watchlistremove"),
    path("postbid/", views.post_bid, name="postbid"),
    path("auctionclose", views.auction_close, name="auctionclose"),
    path("comment", views.comment, name="comment")
]
