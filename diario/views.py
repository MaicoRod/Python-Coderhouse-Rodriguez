from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Emocion, Categoria, EntradaGratitud
from .forms import EmocionForm, CategoriaForm, EntradaGratitudForm, BusquedaForm

def inicio(request):

    entradas_recientes = EntradaGratitud.objects.all()[:3]
    total_entradas = EntradaGratitud.objects.count()
    total_emociones = Emocion.objects.count()
    total_categorias = Categoria.objects.count()

    resultados = []
    busqueda = request.GET.get('buscar', '')
    if busqueda:
        resultados = EntradaGratitud.objects.filter(
            titulo__icontains=busqueda
        ) | EntradaGratitud.objects.filter(
            descripcion__icontains=busqueda
        ) | EntradaGratitud.objects.filter(
            emocion__nombre__icontains=busqueda
        ) | EntradaGratitud.objects.filter(
            categoria__nombre__icontains=busqueda
        )

    return render(request, 'diario/index.html', { 
        'entradas_recientes': entradas_recientes,
        'total_entradas': total_entradas,
        'total_emociones': total_emociones,
        'total_categorias': total_categorias,
        'resultados': resultados,
    })

def entradas(request):

    if request.method == 'POST':
        form = EntradaGratitudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrada guardada correctamente')
            return redirect('entradas') 
    else:
        form = EntradaGratitudForm()

    entradas_lista = EntradaGratitud.objects.all()

    return render(request, 'diario/entradas.html',{
        'form': form,
        'entradas': entradas_lista,
    })

def emociones(request):
    if request.method == 'POST':
        form = EmocionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Emoción registrada correctamente')
            return redirect('emociones')
    else:
        form = EmocionForm()

    
    emociones_lista = Emocion.objects.all()
    return render(request, 'diario/emociones.html', {
        'form': form,
        'emociones': emociones_lista,
    })

def categorias(request):

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria creada correctamente')
            return redirect('categorias')
    else:
        form = CategoriaForm()

    categorias_lista = Categoria.objects.all()

    return render(request,'diario/categorias.html', {
        'form': form,
        'categorias': categorias_lista,
    })




