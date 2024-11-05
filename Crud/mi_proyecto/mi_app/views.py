
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

# Crear (Create)
def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/producto_form.html', {'form': form})

# Leer (Read)
def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'mi_app/producto_lista.html', {'productos': productos})

# Actualizar (Update)
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'mi_app/producto_form.html', {'form': form})

# Eliminar (Delete)
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_lista')
    return render(request, 'mi_app/producto_eliminar.html', {'producto': producto})
