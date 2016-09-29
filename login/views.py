from django.shortcuts import render
from django.core.context_processors import csrf

def index(request):
    c = {}
    c.update(csrf(request))

    return render(request, 'login/index.html',c)
    # return render(request,'login/index.html')
    # return HttpResponse("hiii")


def loginapp(request):
    if request.method=='POST':
        username = request.POST['Username']
        password = request.POST['password']

        if username=='ishan'and password=='abc':
            return render(request, 'login/detail.html')
        else:
            return render(request,'login/index.html')
    else:
        print("invalid")
