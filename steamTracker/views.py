from django.shortcuts import render
from steamTracker.utils import Utils

# Create your views here.

def test(request):
    Utils.log(request)
    return render(request, 'steamTracker/test.html')
