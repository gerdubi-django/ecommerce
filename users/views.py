from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('product_list')
    return render(request, 'users/login.html', {'form': form})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('product_list')
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('product_list')
