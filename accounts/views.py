from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistroForm, EditarPerfilForm
from .models import Perfil

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Cuenta creada correctamente')
            return redirect('inicio')
    else:
        form = RegistroForm()
    
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('inicio')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('inicio')


@login_required
def profile(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'perfil': perfil})


@login_required
def edit_profile(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            
            form.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('profile')
    else:
        form = EditarPerfilForm(instance=perfil)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(old_password):
            messages.error(request, 'Contraseña actual incorrecta')
        elif new_password != confirm_password:
            messages.error(request, 'Las contraseñas nuevas no coinciden')
        elif len(new_password) < 4:
            messages.error(request, 'La contraseña debe tener al menos 4 caracteres')
        else:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Contraseña cambiada correctamente')
            return redirect('profile')
    
    return render(request, 'accounts/change_password.html')