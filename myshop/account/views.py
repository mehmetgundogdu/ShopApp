from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import LoginForm, UserRegistrationForm, UserEditForm, UserPasswordEditForm
from django.http import HttpResponse, HttpResponseRedirect

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user_login = request.user
                    return render(request,
                          'account/login_done.html',
                          {'user_login': user_login})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required(login_url='/account/login/')
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'account/edit.html', {'user_form': user_form})

@login_required(login_url='/account/login/')
def password_edit(request):
    if request.method == 'POST':
        password_edit_form = UserPasswordEditForm(instance=request.user,
                                 data=request.POST)

        if password_edit_form.is_valid():
            new_password = password_edit_form.cleaned_data['password']
            u = User.objects.get(username=request.user.username)
            u.set_password(new_password)
            u.save()
            logout(request)
            return HttpResponseRedirect('/account/login/')
        else:
            messages.error(request, 'Error changing your password')
    else:
        password_edit_form = UserPasswordEditForm(instance=request.user)
    return render(request, 'account/password_edit.html', {'password_edit_form': password_edit_form})


@login_required(login_url='/account/login/')
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'user': user})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/shop/')
