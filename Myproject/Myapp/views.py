from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def Homepage(request):
    context={}
    return render(request,"Homepage.html",context)


def Loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        psw = request.POST.get('password')
        print(username)
    context={}
    return render(request,"loginpage.html",context)

def Registrationpage(request):
    form= UserCreationForm()
    if request.method == 'POSt':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"regist.html",context)
