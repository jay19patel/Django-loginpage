from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def Homepage(request):
    context={}
    return render(request,"Homepage.html",context)

def Loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        userdata=auth.authenticate(request,username=username,password=password1)
        if userdata is not None:
            auth.login(request,userdata)
            return redirect('Homepage')
        else:
            messages.error(request,"sorry data not found")

    context={}
    return render(request,"loginpage.html",context)

def Logout(request):
    auth.logout(request)
    return redirect('Loginpage')

def Registrationpage(request):
    if request.method=='POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        city = request.POST.get('city')

        if (password1!= password2):
            messages.error(request, " Passwords do not match")
            return redirect('Registrationpage')
        else:
            myuser = User.objects.create_user(username, email, password1)
            myuser.save()
            messages.success(request, " Your iCoder has been successfully created")
            return redirect('Loginpage')
    context={}
    return render(request,"regist.html",context)

# @login_required()
def Test(request):
    context={}
    return render(request,"test.html",context)
