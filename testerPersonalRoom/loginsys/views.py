# -*- coding: utf-8 -*-
from django.http import request
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    # просто массив ошибок который используется собственно в форме
    # если юзер ввел некорректное имя(такого юзера нет в бд) то сюда запишется ошибка "Пользователь не найден",

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
        args['form'] = UserCreationForm()
        if request.POST:
            newuser_form = UserCreationForm(request.POST)
            if newuser_form.is_valid():
                newuser_form.save()
                newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
                auth.login(request, newuser)
                return redirect('/')
            else:
                args['form'] = newuser_form
        return render(request, 'loginsys/register.html', args)
