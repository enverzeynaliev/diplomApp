# -*- coding: utf-8 -*-
from django.http import request
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'loginsys/login.html', args)
    else:
        return render(request, 'loginsys/login.html', args)


def logout():
    auth.logout(request)
    return redirect('')


def register(request):
    args = {}
    # сообщения валидации(встроенные методы валидации)
    args.update(csrf(request))
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
        args['form'] = form
    return render(request, 'loginsys/register.html', args)
