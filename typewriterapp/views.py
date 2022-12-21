from django.shortcuts import render

def home(request):
    return render(request,'typewriterapp/homepage.html')