from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Sitter
from .forms import SitterForm

# Sitter views

def sitter_list(request):
    sitters = Sitter.objects.all()
    return render(request, 'core/sitter_list.html', {'sitters': sitters})

def sitter_detail(request, pk):
    sitter = get_object_or_404(Sitter, pk=pk)
    return render(request, 'core/sitter_detail.html', {'sitter': sitter})

def sitter_create(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitter_list')
    else:
        form = SitterForm()
    return render(request, 'core/sitter_form.html', {'form': form})

def sitter_update(request, pk):
    sitter = get_object_or_404(Sitter, pk=pk)
    if request.method == 'POST':
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sitter_list')
    else:
        form = SitterForm(instance=sitter)
    return render(request, 'core/sitter_form.html', {'form': form})

def sitter_delete(request, pk):
    sitter = get_object_or_404(Sitter, pk=pk)
    if request.method == 'POST':
        sitter.delete()
        return redirect('sitter_list')
    return render(request, 'core/sitter_confirm_delete.html', {'sitter': sitter})

# Baby views

# Similar to Sitter views, create views for Baby, BabyDeparture, Payment, ProcuredItem, and ResoldDoll.
