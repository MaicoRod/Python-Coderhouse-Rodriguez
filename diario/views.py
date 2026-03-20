from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from .models import EntradaGratitud, Emocion, Categoria
from .forms import EntradaGratitudForm, EmocionForm, CategoriaForm


def inicio(request):
    """Vista de inicio con búsqueda integrada"""
    entradas_recientes = EntradaGratitud.objects.all()[:3]
    total_entradas = EntradaGratitud.objects.count()
    total_emociones = Emocion.objects.count()
    total_categorias = Categoria.objects.count()
    
    resultados = []
    busqueda = request.GET.get('buscar', '')
    if busqueda:
        resultados = EntradaGratitud.objects.filter(
            Q(titulo__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(emocion__nombre__icontains=busqueda) |
            Q(categoria__nombre__icontains=busqueda)
        )
    
    return render(request, 'diario/index.html', {
        'entradas_recientes': entradas_recientes,
        'total_entradas': total_entradas,
        'total_emociones': total_emociones,
        'total_categorias': total_categorias,
        'resultados': resultados,
    })


def about(request):
    """Vista de Acerca de mí"""
    return render(request, 'diario/about.html')


class EntradaListView(ListView):
    model = EntradaGratitud
    template_name = 'diario/entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 6


class EntradaDetailView(DetailView):
    model = EntradaGratitud
    template_name = 'diario/entrada_detail.html'
    context_object_name = 'entrada'


class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = EntradaGratitud
    form_class = EntradaGratitudForm
    template_name = 'diario/entrada_form.html'
    success_url = reverse_lazy('entrada_list')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, 'Entrada creada correctamente')
        return super().form_valid(form)


class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    model = EntradaGratitud
    form_class = EntradaGratitudForm
    template_name = 'diario/entrada_form.html'
    success_url = reverse_lazy('entrada_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Entrada actualizada correctamente')
        return super().form_valid(form)


class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    model = EntradaGratitud
    template_name = 'diario/entrada_confirm_delete.html'
    success_url = reverse_lazy('entrada_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Entrada eliminada correctamente')
        return super().delete(request, *args, **kwargs)


@login_required
def emociones(request):
    if request.method == 'POST':
        form = EmocionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emoción creada correctamente')
    else:
        form = EmocionForm()
    
    emociones_lista = Emocion.objects.all()
    return render(request, 'diario/emociones.html', {
        'form': form,
        'emociones': emociones_lista,
    })


@login_required
def categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente')
    else:
        form = CategoriaForm()
    
    categorias_lista = Categoria.objects.all()
    return render(request, 'diario/categorias.html', {
        'form': form,
        'categorias': categorias_lista,
    })