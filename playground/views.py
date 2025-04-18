from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sey_hello(reqest):
    return HttpResponse("Hello!")

def test_templet(request):
    return render(request,"hello.html",{'name':'ABC'})