from django.shortcuts import render

# Create your views here.
def index(request):
    item_list = {
        1: 'knife',
        2: 'knife',
        3: 'knife',
        4: 'knife',
        5: 'knife',
        6: 'knife',
    }
    context = {'item_list': item_list}
    return render(request, 'home/index.html', context)
