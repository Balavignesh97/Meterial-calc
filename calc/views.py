from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def hexa(request):
    if request.method=="POST":
        value1=int(request.POST.get('w'))
        value2=int(request.POST.get('l'))
        value3=float(request.POST.get('list'))
        res=(value1 * value1)*value2*value3
    else:
        res=0
    return render(request,"hexa.html",{"res":res})

def round(request):
    if request.method=="POST":
        v1=int(request.POST.get('dia'))
        v2=int(request.POST.get('len'))
        v3=float(request.POST.get('list'))
        res1=res=(v1 * v1)*v2*v3
    else:
        res1=0
    return render(request,"round.html",{"res1":res1})

def square(request):
    if request.method=="POST":
        v1=int(request.POST.get('width'))
        v2=int(request.POST.get('len'))
        v3=float(request.POST.get('list'))
        res2=res=(v1 * v1)*v2*v3
    else:
        res2=0
    return render(request,"square.html",{"res2":res2})

def tube(request):
    if request.method=="POST":
        v1=int(request.POST.get('dia'))
        v2=int(request.POST.get('wt'))
        v3=int(request.POST.get('len'))
        v4=float(request.POST.get('list'))
        res3=(v1-v2)*v2*v3*v4
    else:
        res3=0
    return render(request,"pipe.html",{"res3":res3})

def flat(request):
    if request.method=="POST":
        v1=int(request.POST.get('width'))
        v2=int(request.POST.get('thicknes'))
        v3=int(request.POST.get('len'))
        v4=float(request.POST.get('list'))
        res4=v1*v2*v3*v4
    else:
        res4=0
    return render(request,"flat.html",{"res4":res4})
    

    

