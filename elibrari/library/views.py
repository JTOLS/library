from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from library.forms import LoginUserForm, RegisterUserForm


def index(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('reader'))
    else:
        form = LoginUserForm()
    return render(request, 'library/index.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('reader'))
    else:
        form = RegisterUserForm()
    return render(request, 'library/registration.html', {'form': form})

def reader(request):
    return render(request, 'library/reader.html')