from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

def home(request):
    #return render(request, 'index.html')
    return render(request, 'index.html',{'name':'Krishna..'})
    #Passing dynamic parameters through views
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']

        myuser = User.objects.create_user(username,email,pwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request,"Your Account has been created")
        return redirect('signin')

    return render(request,"signup.html")
def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pwd=request.POST['pwd']

        user = authenticate(username=username,pwd=pwd)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"index.html",{'fname':fname})

        else:
            messages.error(request,"Bad Creds")
            return redirect('home')


    return render(request,'signin.html')
def signout(request):
    pass


# Create your views here.
# render means merging the static and dynamic content
