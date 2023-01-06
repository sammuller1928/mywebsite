from django.shortcuts import render

# Create your views here.
class Home(request):
    return render(request,'sammullerApp/home.html')
