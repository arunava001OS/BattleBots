from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'battlebots/index.html',{})

def index1(request):
    return render(request,'battlebots/index1.html',{})

def login(request):
    return render(request,'battlebots/login.html',{})

def play(request):
    return render(request,'battlebots/play.html',{})

def index2(request):
    return render(request,'battlebots/index2.html',{})

def leaderboard(request):
    return render(request,'battlebots/leaderboard.html',{})
def interface(request):
    return render(request,'battlebots/interface.html',{})


