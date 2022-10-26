from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("auction", views.auction, name="auction"),
    path("auction", views.auction, name="auction"),
    path("auction1/<int:id>", views.listing, name="auction1"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addwatchlist/<int:id>", views.addwatchlist, name="addwatchlist"),
    path("delwatchlist/<int:id>", views.delwatchlist, name="delwatchlist"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("close/<int:id>", views.close, name="close"),
    path("comments/<int:id>", views.comments, name="comments"),
    path("categories", views.categories, name="categories"),
    path("category/<str:title>", views.category, name="category"),
]
