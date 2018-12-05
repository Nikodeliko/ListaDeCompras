from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserForm
# Create your views here.

def usuario_add(request):
    context = {}
    if request.method=="POST":
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'usuario/registro.html', context)
    else:
        user_form= UserForm()
        context['user_form'] = user_form
        return render(request, 'usuario/registro.html', context)

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Error en el usuario o contraseña."
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "listas/index.html", context)

@login_required(login_url="/login/")
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
