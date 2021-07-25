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


def about_view(request,*args,**kwargs):
    my_context = {
        "my_text": "si que si,hola ",
        "my_number": 123,
        "my_list": [123,456,789]
    }
    return render(request=request,
                  template_name="about.html",
                  context=my_context)