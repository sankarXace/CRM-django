from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else :
            messages.success(request, "There was an error in loggin in, Please try again...")
            return redirect('home')
    else :
        return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered!")
            return redirect('home') 
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request ,pk):
    if request.user.is_authenticated:
        # Lookup the record
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page....")
        return redirect('home')    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_item = Record.objects.get(id=pk)
        delete_item.delete()
        messages.success(request, "Records Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You need to be logged in to be able to do that operation...")
        return redirect('home')
