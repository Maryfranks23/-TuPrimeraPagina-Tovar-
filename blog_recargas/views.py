from django.shortcuts import render, redirect
from .forms import RecargaForm, ClienteForm, EmpresaRecargaForm, BusquedaRecargaForm
from .models import Recarga

def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaRecargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_empresa')
    else:
        form = EmpresaRecargaForm()
    return render(request, 'blog_recargas/crear_empresa.html', {'form': form, 'titulo': 'Crear Empresa'})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_cliente')
    else:
        form = ClienteForm()
    return render(request, 'blog_recargas/crear_cliente.html', {'form': form, 'titulo': 'Crear Cliente'})

def crear_recarga(request):
    if request.method == 'POST':
        form = RecargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_recarga')
    else:
        form = RecargaForm()
    return render(request, 'blog_recargas/crear_recarga.html', {'form': form, 'titulo': 'Crear Recarga'})

def buscar_recarga(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaRecargaForm(request.POST)
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            resultados = Recarga.objects.filter(telefono__icontains=telefono)
    else:
        form = BusquedaRecargaForm()
    return render(request, 'blog_recargas/buscar_recarga.html', {'form': form, 'resultados': resultados, 'titulo': 'Buscar Recarga'})