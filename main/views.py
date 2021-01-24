from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def index(request):    
    return render(request , "index.html")

def cap(request):
    handle_uploaded_file(request.FILES['img'] )
    return HttpResponse("hey")
