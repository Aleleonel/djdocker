from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url

from .forms import EstoqueForm, EstoqueItensForm
from .models import (Estoque, EstoqueEntrada, EstoqueItens, EstoqueSaida,
                     Produto)


def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = EstoqueEntrada.objects.all()
    context = {
        'object_list': objects
    }
    return render(request, template_name, context)


def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = EstoqueEntrada.objects.get(pk=pk)
    context = {
        'object': obj
    }
    return render(request, template_name, context)


def dar_baixa_estoque(form):
    # Pega os produtos a partir da instancia do formulario (estoque)
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
    print("Estoque aualizado com sucesso")


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()
    item_estoque_form = inlineformset_factory(
        EstoqueEntrada,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_form(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            dar_baixa_estoque(form)
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_form(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def estoque_saida_list(request):
    template_name = 'estoque_saida_list.html'
    objects = EstoqueSaida.objects.all()
    context = {
        'object_list': objects
    }
    return render(request, template_name, context)


def estoque_saida_detail(request, pk):
    template_name = 'estoque_saida_detail.html'
    obj = EstoqueSaida.objects.get(pk=pk)
    context = {
        'object': obj
    }
    return render(request, template_name, context)


def estoque_saida_add(request):
    template_name = 'estoque_saida_form.html'
    estoque_form = Estoque()
    item_estoque_form = inlineformset_factory(
        EstoqueSaida,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_form(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            dar_baixa_estoque(form)
            url = 'estoque:estoque_saida_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_form(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)
