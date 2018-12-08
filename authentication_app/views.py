from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('memories:list', kwargs={'username': username}))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'authentication_app/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('memories:list', kwargs={'username': username}))
    return render(request, 'authentication_app/login.html')

def logout_view(request):
    logout(request);
    return redirect(reverse('memories:main'))
