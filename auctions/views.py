from unicodedata import name
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from sqlalchemy import false
from .forms import Auctionform, Bidform, Commentform


from .models import User, AuctionListing, Bid, Comment, Categories

@login_required(redirect_field_name='login')
def index(request):
    auctionmodel = AuctionListing.objects.filter(active=True)
    return render(request, "auctions/index.html",{"model":  auctionmodel})


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

@login_required(redirect_field_name='login')
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


        
@login_required()
def auction(request):
  
    form = Auctionform(request.POST)
      # create bid instance
    if request.method == 'POST': 
        try:    
            starting_bid = Bid(price = request.POST['bid'], bid_by = request.user)
            starting_bid.save()
            if form.is_valid():
                m = form.save(commit=False)
                m.listed_by = request.user
                m.bid = starting_bid
                m.save()
                newmodel = AuctionListing.objects.all()    
                return render(request, "auctions/index.html",{"model":newmodel})
        except ValidationError:
            return render(request,"auctions/error.html",{"message":"Bad Request"})
        else:
            return render(request,"auctions/error.html",{"message":"Bad Request"})
    else:
        return render(request, "auctions/auction.html",{"form":form})
    
    
@login_required(redirect_field_name='login')   
def listing(request, id):
    model = AuctionListing.objects.get(pk=id)
    try:
        commentmod = Comment.objects.filter(item=model.id)
    except:
        commentmod = None
    bidform = Bidform(request.POST)
    highestbidder = model.bid.bid_by
    price = model.bid.price
    user = request.user
    watching = False
    active = model.active
    creator = model.listed_by
    comform = Commentform(request.POST)
    watchl = model.watchers.all()
    for w in watchl:
        if user == w:
            watching = True
    return render(request, "auctions/auctioned.html", {
        "model": model, 
        "watching":watching,
        "price":price,
        "bidform":bidform,
        "creator": creator,
        "user": user,
        "highestbidder": highestbidder,
        "active": active,
        "commentform":comform,
        "comment": commentmod
        })

@login_required(redirect_field_name='login')
def watchlist(request):
    # get current user
    id = request.user.id 
    
    user = User.objects.get(id=id) # get all the objects for the current user
    
    watch = user.watchlist.all() # use related name to bring all items associted to current user
    
    return render(request, "auctions/watchlist.html", {"watch":watch})


@login_required(redirect_field_name='login')
def addwatchlist(request,id):
    model = AuctionListing.objects.get(pk=id)
    user_id = request.user.id
    current = User.objects.get(pk= user_id)
    model.watchers.add(current)
    return HttpResponseRedirect(reverse("auction1", args=(id,)))
        
@login_required(redirect_field_name='login')
def delwatchlist(request,id):
    model = AuctionListing.objects.get(pk=id)
    user_id = request.user.id
    current = User.objects.get(pk = user_id)
    model.watchers.remove(current)
    return HttpResponseRedirect(reverse("auction1", args=(id,)))


#function for adding a new bid
@login_required(redirect_field_name='login')
def bid(request,id):
    model = AuctionListing.objects.get(pk=id)
    comform = Commentform(request.POST)
    try:
        commentmod = Comment.objects.filter(item=model.id)
    except:
        commentmod = None
    watching = False
    user = request.user
    bidform = Bidform(request.POST)
    creator = model.listed_by
    watchl = model.watchers.all()
    for w in watchl:
        if user == w:
            watching = True
    if request.method == 'POST':
        newbid = Bidform(request.POST)
        n = newbid.save(commit=False)
        price = model.bid.price
        bidform = Bidform(request.POST)
        creator = model.listed_by
        user = request.user
        comform = Commentform(request.POST)
        highestbidder = model.bid.bid_by
        active = model.active
        if n.price < model.bid.price:
            return render(request, "auctions/auctioned.html", {
        "model": model, 
        "watching":watching,
        "price":price,
        "bidform":bidform,
        "creator": creator,
        "user": user,
        "highestbidder": highestbidder,
        "active": active,
        "failmessage": "Please Bid Above currrent Auction Price!",
        "commentform":comform,
        "comment":commentmod
        })
        else:
            n.bid_by = request.user
            n.save()
            model.bid = n
            model.save()
            message = "bid Successful!"
            return render(request, "auctions/auctioned.html", {
        "model": model, 
        "watching":watching,
        "price":price,
        "bidform":bidform,
        "creator": creator,
        "user": user,
        "highestbidder": highestbidder,
        "active": active,
        "message": message,
        "commentform":comform,
        "comment":commentmod
        })
            
            
# function to close listing
@login_required(redirect_field_name='login')     
def close(request,id):
    model = AuctionListing.objects.get(pk=id)
    model.active = False
    model.save()
    return HttpResponseRedirect(reverse("auction1", args=(id,)))

# function to add comments
@login_required(redirect_field_name='login') 
def comments(request,id):
    model = AuctionListing.objects.get(pk=id)
    price = model.bid.price
    bidform = Bidform(request.POST)
    creator = model.listed_by
    highestbidder = model.bid.bid_by
    active = model.active
    user = request.user
    watching = False
    watchl = model.watchers.all()
    for w in watchl:
        if user == w:
            watching = True
    if request.method == 'POST':
        comform = Commentform(request.POST)
        c = comform.save(commit=False)
        c.author = request.user
        c.item = model
        c.save()
        message = "Comment Added!"
        commentmod = Comment.objects.filter(item=model.id)
        return render(request, "auctions/auctioned.html", {
        "model": model, 
        "watching":watching,
        "price":price,
        "bidform":bidform,
        "creator": creator,
        "user": user,
        "highestbidder": highestbidder,
        "active": active,
        "message": message,
        "commentform":comform,
        "comment":commentmod
        })

# function to view categories        
@login_required(redirect_field_name='login') 
def categories(request):
    model = Categories.objects.all()
    return render(request, "auctions/categories.html", {"model":model})

# fucntion to view category page
@login_required(redirect_field_name='login') 
def category(request,title):
    newmodel = Categories.objects.get(name=title)
    model = newmodel.categories.filter(active=True)
    return render(request, "auctions/category.html", {"model":model, "title":title})
    
    
            
        
        
        
        
        
    
    
    

    
    

    
    
    
    