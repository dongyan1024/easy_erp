from django.shortcuts import render
from .models import Inventory, Element
from .forms import TypeForm, ElementForm
from django.http import  HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from haystack.forms import SearchForm
# Create your views here.
def index(request):
    return render(request, 'inventory_manage/index.html')

@login_required
def inventory(request):
    types = Inventory.objects.order_by('date_add')
    context = {'types': types}
    return render(request, 'inventory_manage/type.html', context)

@login_required
def element(request, type_id):
    type = Inventory.objects.get(id=type_id)
    elements = type.element_set.order_by('-date_add')
    context = {'type': type, 'elements': elements}
    return render(request, 'inventory_manage/element.html', context)

@login_required
def new_type(request):
    if request.method != 'POST':
        form = TypeForm()
    else:
        form = TypeForm(request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            new_type.owner = request.user
            new_type.save()
        return HttpResponseRedirect(reverse('inventory_manage:type'))

    context = {'form': form}
    return render(request, 'inventory_manage/new_type.html', context)

@login_required
def new_element(request, type_id):
    type = Inventory.objects.get(id=type_id)

    if request.method != 'POST':
        form = ElementForm
    else:
        form = ElementForm(data=request.POST)
        if form.is_valid():
            new_element = form.save(commit=False)
            new_element.type = type
            new_element.save()
        return HttpResponseRedirect(reverse('inventory_manage:element', args=[type_id]))
    context = {'type': type, 'form': form}
    return render(request, 'inventory_manage/new_element.html', context)

@login_required
def edit_element(request, element_id):
    element = Element.objects.get(id=element_id)
    type = element.type

    if request.method != 'POST':
        form = ElementForm(instance=element)
    else:
        form = ElementForm(instance=element, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inventory_manage:element', args=[type.id]))

    context = {'element': element, 'type': type, 'form': form}
    return render(request,'inventory_manage/edit_element.html', context)


