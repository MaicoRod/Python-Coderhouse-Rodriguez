from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm

@login_required
def mensajes(request):
    """Vista principal de mensajes"""
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    
    no_leidos = mensajes_recibidos.filter(leido=False).count()
    
    return render(request, 'mensajeria/mensajes.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados,
        'no_leidos': no_leidos,
    })


@login_required
def enviar_mensaje(request):
    """Vista para enviar un mensaje"""
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado correctamente')
            return redirect('mensajes')
    else:
        form = MensajeForm()
    
    return render(request, 'mensajeria/enviar_mensaje.html', {'form': form})


@login_required
def ver_mensaje(request, pk):
    """Vista para ver un mensaje específico"""
    mensaje = get_object_or_404(Mensaje, pk=pk)
    
    if mensaje.destinatario != request.user and mensaje.remitente != request.user:
        messages.error(request, 'No tienes permiso para ver este mensaje')
        return redirect('mensajes')
    
    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    
    return render(request, 'mensajeria/ver_mensaje.html', {'mensaje': mensaje})


@login_required
def eliminar_mensaje(request, pk):
    """Vista para eliminar un mensaje"""
    mensaje = get_object_or_404(Mensaje, pk=pk)
    
    if mensaje.destinatario == request.user or mensaje.remitente == request.user:
        mensaje.delete()
        messages.success(request, 'Mensaje eliminado')
    else:
        messages.error(request, 'No tienes permiso para eliminar este mensaje')
    
    return redirect('mensajes')