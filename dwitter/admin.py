from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Dweet, Profile

class ProfileInline(admin.StackedInline):
    model = Profile

class userAdmin(admin.ModelAdmin):
    model = User
    
    fields = ["username"]
    inlines = [ProfileInline]
    
admin.site.unregister(User)
admin.site.register(User, userAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)

# admin.site.register(Profile)