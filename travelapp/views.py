from django.shortcuts import render
from django.contrib.auth.models import User
from travelapp.models import Place
from django.shortcuts import render


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, 'index.html',{'result': obj})
# Create your views here.




# Create your views here.
