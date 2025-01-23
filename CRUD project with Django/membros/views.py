from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Membro

class MembroListView(ListView):
    model = Membro
    template_name = 'membros/membro_list.html'

class MembroDetailView(DetailView):
    model = Membro
    template_name = 'membros/membro_detail.html'

class MembroCreateView(CreateView):
    model = Membro
    fields = ['nome', 'idade', 'bairro', 'numero_celular', 'estado_civil']
    template_name = 'membros/membro_form.html'
    success_url = reverse_lazy('membro_list')

class MembroUpdateView(UpdateView):
    model = Membro
    fields = ['nome', 'idade', 'bairro', 'numero_celular', 'estado_civil']
    template_name = 'membros/membro_form.html'
    success_url = reverse_lazy('membro_list')

class MembroDeleteView(DeleteView):
    model = Membro
    template_name = 'membros/membro_confirm_delete.html'
    success_url = reverse_lazy('membro_list')
