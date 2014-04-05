from django.shortcuts import render

# Create your views here.

class SteamTracker(models.Model):
    firstName = models.CharField(max_length=120, null=True, blank=True)
    lastName = models.CharField(max_length=120, null=True, blank=True)
    email = models.Email()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
