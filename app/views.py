from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.


def fr(request):
    return HttpResponse('its normal string return ')

class cr(View):
    def  get(self,request):
        return HttpResponse('its normal class based view')

def funpage(request):
    return render(request, 'funpage.html')

class classpage(View):
    def get(self, request):
        return render(request, 'classpage.html')
    

def studformpage(request):
    sf=StudForm()
    d={'sf':sf}
    if request.method=="POST":
        sfo=StudForm(request.POST)
        if sfo.is_valid():
            sfo.save()
            return HttpResponse('data inserted successfully')
    return render(request, 'studformpage.html',d)

class clsStudForm(View):
    def get(self,request):
        sf=StudForm()
        d={'sf': sf}
        return render(request,'clsStudForm.html',d)
    def post(self,request):
        sf=StudForm(request.POST)
        if sf.is_valid():
            sf.save()
            return HttpResponse('data inserted successfully')
