from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    #return HttpResponse("<h1> Hello World </h1>")
    return render(request=request,
                  template_name="home.html",
                  context={})

def contact_view(request,*args,**kwargs):
    return render(request=request,
                  template_name="contact.html",
                  context={})