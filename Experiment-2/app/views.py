from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<i>Hello All.</i>")

def about(request):
    return render(request, 'fwad.html', {'name': 'Bob', 'age': 20})