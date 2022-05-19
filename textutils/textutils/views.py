# I HAVE CREATED THIS FILE - VARUN
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request,'index2.html')

def analyze2(request):
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    caps = request.POST.get('caps','off')
    nlr = request.POST.get('nlr','off')
    esr = request.POST.get('esr','off')
    temp = text
    print (removepunc)
    if removepunc == "on":
        result = ''
        punctuations = '''!@#$%^&*()_:;,'"./{[]}<>+'''
        for i in text:
            if i not in punctuations:
                result += i
        text = result
        params = {'given':temp,'result':result}
       

    if( caps == "on" ):
        result = ''
        for i in text:
            result += i.upper()
        text = result
        params = {'given':temp,'result':result}
        

    if( nlr == "on"):
        result = ''
        for i in text:
            if (i != "\n" and i != "\r"):
                result += i
        text = result
        params = {'given':temp,'result':result}
        

    if( esr == "on"):
        result = ''
        for i,c in enumerate(text):
            if not(text[i]==" " and text[i+1]==" "):
                result += c 
        text = result
        params = {'given':temp,'result':result}

    if (removepunc=="off" and caps=="off" and nlr=="off" and esr=="off"):
        result = "No Changes"
        params = {'given':temp,'result':result}
        return render(request,'analyze2.html',params)
    else:
        return render(request,'analyze2.html',params)