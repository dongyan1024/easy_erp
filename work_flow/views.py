from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Ele_Overview, Detial
from .forms import OverviewForm, WorkStepForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def overview(request):
    elements = Ele_Overview.objects.order_by('-date_add')
    context = {'elements': elements}
    return render(request, 'work_flow/overview.html', context)

@login_required
def detials(request, E_O_id):
    E_O = Ele_Overview.objects.get(id=E_O_id)
    work_steps = E_O.detial_set.order_by('-date_add')
    context = {'E_O': E_O, 'work_steps': work_steps}
    return render(request, 'work_flow/detials.html', context)

@login_required
def new_element(request):
    if request.method != 'POST':
        form = OverviewForm()
    else:
        form = OverviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('work_flow:overview'))
    context = {'form': form}
    return render(request, 'work_flow/new_element.html', context)


@login_required
def new_step(request, element_id):
    element = Ele_Overview.objects.get(id=element_id)
    if request.method != 'POST':
        form = WorkStepForm()
    else:
        form = WorkStepForm(data=request.POST)
        if form.is_valid():
            new_step = form.save(commit=False)
            new_step.type = element
            new_step.save()
            return HttpResponseRedirect(reverse('work_flow:detials', args=[element_id]))
    context = {'element': element, 'form': form}
    return render(request, 'work_flow/new_step.html', context)

@login_required
def edit_working(request, element_id):
    element = Ele_Overview.objects.get(id=element_id)
    if request.method != 'POST':
        form = OverviewForm(instance=element)
    else:
        form = OverviewForm(instance=element, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('work_flow:overview'))

    context = {'element': element, 'form': form}
    return render(request, 'work_flow/edit_working.html', context)

@login_required
def edit_step(request, step_id):
    step = Detial.objects.get(id=step_id)
    id = step.type.id
    if request.method != 'POST':
        form = WorkStepForm(instance=step)
    else:
        form = WorkStepForm(instance=step, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('work_flow:detials', args=[id]))

    context = {'step': step, 'form': form}
    return render(request, 'work_flow/edit_step.html', context)
