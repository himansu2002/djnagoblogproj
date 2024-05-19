from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserCreationForm ,profileupdateform ,userUpdateform
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! {username} able to log in')
            return redirect('blog/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form}) 

@login_required

def profile(request):
    
    
    return render(request, 'users/profile.html',)

def profile_update(request):
    context = {'u_form':userUpdateform(instance=request.user), 'p_form':profileupdateform(instance=request.user.profile)}   
    if request.method == 'POST':
        u_form = userUpdateform(request.POST, instance=request.user)
        p_form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:   
        u_form = userUpdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    
    return render(request, 'users/profile_update.html',context)