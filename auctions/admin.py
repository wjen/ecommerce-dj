from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Listing, Bid, Comment

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "creator", "title", "timestamp", "price", "category", "active", "winner")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "bidder", "timestamp", "bid_price")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "commenter", "timestamp", "comment")


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ("watchlist",)
    fieldsets = UserAdmin.fieldsets + (
        ("Watchlist", {'fields': ('watchlist',)}),
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
