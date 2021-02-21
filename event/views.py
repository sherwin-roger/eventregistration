from django.shortcuts import render
from .models import event,eventAdmin
# Create your views here.
def home(request):
    context={}
    return render(request, 'event/home.html', context) 

def events(request):
    context={}
    return render(request, 'event/event.html', context)

def form(request):
    context={}
    if request.method == "POST":
        e1=event()
        e1.email=request.POST.get("email")
        e1.name=request.POST.get("name")
        e1.year=request.POST.get("year")

        if len(event.objects.all()) > 15:
            return render(request, 'event/failed.html', context)
        else:
            e1.save()
            return render(request, 'event/success.html', context)
    return render(request, 'event/form.html', context) 

def success(request):
    context={}
    return render(request, 'event/success.html', context) 

def failed(request):
    context={}
    return render(request, 'event/failed.html', context)

def eventAdmin(request):
    context={}
    result=event.objects.all()
    context["answers"]=result
    return render(request,'event/eventAdmin.html',context)