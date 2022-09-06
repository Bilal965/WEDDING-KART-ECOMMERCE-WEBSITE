from django.shortcuts import render
from django.http import HttpResponse

# Create you  r views here.
def index(request):
    return render(request,'index.html')