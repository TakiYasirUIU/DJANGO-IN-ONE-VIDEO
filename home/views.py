from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable1" :"Harry is great",
        "variable2" :"Rohan is great"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")
def services(request):
    return HttpResponse("this is servicespage")
def contract(request):
    return HttpResponse("this is contractpage")


