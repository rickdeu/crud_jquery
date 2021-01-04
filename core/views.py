from core.form import *
from core.models import *
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string

 

def home(request):
    alvo=Alvo.objects.all().order_by('-id')
    template_name="core/alvos_list_home.html"
    context={'alvo':alvo}
    return render(request, template_name, context)

def alvos_list(request):
    alvo=Alvo.objects.all().order_by('-id')
    template_name="core/alvos_list.html"
    context={'alvo':alvo}
    return render(request, template_name, context)


def save_alvos_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            alvo=Alvo.objects.all().order_by('-id')
            data['html_alvo_list'] = render_to_string('core/includes/partial_alvo_list_home.html', {
                'alvo': alvo
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def alvo_create(request):
    if request.method == 'POST':
        form = AlvoForm(request.POST)
    else:
        form = AlvoForm()
    return save_alvos_form(request, form, 'core/includes/partial_alvo_create.html')

def alvo_update(request, pk):
    alvo=get_object_or_404(Alvo, pk=pk)
    if request.method=="POST":
        form=AlvoForm(request.POST, instance=alvo)
    else:
        form=AlvoForm(instance=alvo)
    return save_alvos_form(request, form, 'core/includes/partial_alvo_update.html')

def alvo_delete(request, pk):
    alvo=get_object_or_404(Alvo, pk=pk)
    data=dict()
    if request.method=='POST':
        alvo.delete()
        data['form_is_valid']=True
        alvo=Alvo.objects.all().order_by('-id')
        data['html_alvo_list']=render_to_string('core/includes/partial_alvo_list_home.html', {
            'alvo':alvo
        })
    else:
        context={'alvo':alvo}
        data['html_form']=render_to_string('core/includes/partial_alvo_delete.html', context, request=request)
    return JsonResponse(data)
