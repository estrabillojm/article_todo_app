from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

def account_login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'accounts/accounts_index.html', {'form': form, 'active4':'active'})
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
        else:
            err_msg = "Username and Password did not matched"
        return render(request, 'accounts/accounts_index.html', {'form': form, 'active4':'active', 'errmsg':err_msg})

def account_signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/accounts_signup.html', {'form': form, 'active5':'active'})
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
        return render(request, 'accounts/accounts_signup.html', {'form': form, 'active5':'active'})

def account_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
