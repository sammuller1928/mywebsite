from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'sammullerApp/home.html')

def Music(request):
    return render(request,'sammullerApp/music.html')
