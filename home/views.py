from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    return render(request,"home.html")

def submit(request):
    global var
    var=str(request.POST["password"])

    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890+=_)(*&^%$#@!~'
    key = 'xznlwebgjhqdyvtkfuompciasr0987654321@#$%^&*()_+=!~'
    secret_message = var
    secret_message = secret_message.lower()
    res=[]
    for c in secret_message:
        # if c.isalpha():
            res.append(key[alphabet.index(c)])
        # else:
            # res.append(c)
    join="".join(res)


    return render(request,"encry.html",{'id':join})

def decrypt(request):

    return render(request,'decrypt.html',{'id':var})
