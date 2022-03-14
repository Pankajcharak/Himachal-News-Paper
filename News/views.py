from django.shortcuts import render, HttpResponse
def index(request):
    hello1 = request.POST.get('name')
    d="https://epaperwmimg.amarujala.com/"+hello1+"/ch/01/hdimage.jpg"
    q="https://epaperwmimg.amarujala.com/"+hello1+"/ch/02/hdimage.jpg"
    r="https://epaperwmimg.amarujala.com/"+hello1+"/ch/03/hdimage.jpg"
    s="https://epaperwmimg.amarujala.com/"+hello1+"/ch/04/hdimage.jpg"
    t="https://epaperwmimg.amarujala.com/"+hello1+"/ch/05/hdimage.jpg"
    u="https://epaperwmimg.amarujala.com/"+hello1+"/ch/06/hdimage.jpg"
    v="https://epaperwmimg.amarujala.com/"+hello1+"/ch/07/hdimage.jpg"
    w="https://epaperwmimg.amarujala.com/"+hello1+"/ch/08/hdimage.jpg"
    x="https://epaperwmimg.amarujala.com/"+hello1+"/ch/09/hdimage.jpg"
    y="https://epaperwmimg.amarujala.com/"+hello1+"/ch/10/hdimage.jpg"
    z="https://epaperwmimg.amarujala.com/"+hello1+"/ch/11/hdimage.jpg"
    a="https://epaperwmimg.amarujala.com/"+hello1+"/ch/12/hdimage.jpg"
    b="https://epaperwmimg.amarujala.com/"+hello1+"/ch/13/hdimage.jpg"
    c="https://epaperwmimg.amarujala.com/"+hello1+"/ch/14/hdimage.jpg"
    
    context={
        'd' : d,
        'q' : q,
        'r' : r,
        's' : s,
        't' : t,
        'u' : u,
        'v' : v,
        'w' : w,
        'x' : x,
        'y' : y,
        'z' : z,
        'a' : a,
        'b' : b,
        'c' : c
    }
    return render(request,'index.html',context)