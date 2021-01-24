from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
from capgen import *

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def index(request):    
    return render(request , "index.html")

def cap(request):
    """handle_uploaded_file(request.FILES["file"])
    model = load_mymodel()
    idx_to_word, word_to_idx, vocab_size = load_vocab()
    resnet = load_resnet()
    caption = predict_caption("name.jpg", word_to_idx, idx_to_word, model, resnet)
    os.remove("name.jpg")
    return caption
    """
    return "hey"
