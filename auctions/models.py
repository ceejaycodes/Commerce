from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models
from traitlets import default
from django.utils import timezone


class User(AbstractUser):
        def __str__(self):
            return f"{self.username}"
        
class Categories(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.name}"
    
    

class Bid(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0, blank=True, null=True)
    bid_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name='buyers',blank=True) 
    
    def __str__(self):
        return f"{self.bid_by} bid {self.price}"
    
        
        
class AuctionListing(models.Model):
    item = models.CharField(max_length=75, blank=True) 
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='current_bid')
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, max_length=200)
    active = models.BooleanField(default=True)
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='creator')
    watchers = models.ManyToManyField(User,related_name='watchlist', blank=True, null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='winners', blank=True, null=True)
    time_listed = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.item} starting price is {self.bid.price}"


    


class Comment(models.Model):
    comment = models.TextField(help_text="Please Leave A Review", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='authors')
    item =  models.ForeignKey(AuctionListing, on_delete=models.PROTECT, related_name = 'products')
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.comment} by {self.author}"
    

    
    
    

