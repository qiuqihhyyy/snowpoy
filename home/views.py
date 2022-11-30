from django.shortcuts import render

def mainhome(requests):
    return render(requests, 'home.html')
