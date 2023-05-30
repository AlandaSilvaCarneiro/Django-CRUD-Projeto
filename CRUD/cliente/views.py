from cliente.models import Cliente
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView


class ClienteList(ListView):
    template_name = 'cliente/home.html'
    model = Cliente
    queryset =Cliente.objects.all()


class ClienteCreate(CreateView):
    model = Cliente
    fields = "__all__"
    success_url= reverse_lazy('cliente:list')



class ClienteUpdate(UpdateView):
    model = Cliente
    fields = "__all__"
    success_url= reverse_lazy('cliente:list')
