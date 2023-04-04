from django.shortcuts import render
from .models import Item

# Create your views here.

def item_detail_view(request):
    obj = Item.objects.all()
    context = {
        'obj': obj
    }
    return render(request, "mari_efficiency\mari_efficiency.html", context)