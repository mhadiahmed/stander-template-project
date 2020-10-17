from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import FileUpladForm
# Create your views here.


def home_view(request):
    return render(request,'home.html',{})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:home')
    else:
        form = UserCreationForm()
    return render(request, 'singup.html', {'form': form})


def fileUpload(request):
    if request.method == 'POST':
        form = FileUpladForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('core:home')
    else:
        form = FileUpladForm()
    return render(request,'fileupload.html',{'form':form})