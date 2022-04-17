from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from produto.forms import ProdutoForm
from .forms import ProdutoForm

from webstore.settings import TEMPLATES
from .models import Produto
import io
import csv


def replace_number(request):
    template_name = 'replace_number.html'
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file = myfile.read().decode('utf-8')
        reader = csv.reader(io.StringIO(file))
        data = [line for line in reader]
        
        numbers = []
        for numero in range(len(data)):           
            numbers.append(data[numero])
        
        context = {
            'data': numbers
        }
        return render(request, template_name, context)    
    return render(request, template_name)

def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)

def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)


class ProdutoCreate(CreateView):
    model=Produto
    template_name='produto_form.html'
    form_class=ProdutoForm

class ProdutoUpdate(UpdateView):
    model=Produto
    template_name='produto_form.html'
    form_class=ProdutoForm

def produto_json(request, pk):
    '''Retorna o produto, id e estoque'''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
