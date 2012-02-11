from django.shortcuts import render_to_response, redirect
from django.template import Context, loader 
from gt.gtarefas.models import Task
from gt.gtarefas.forms import TaskForm
from django.contrib.auth.decorators import login_required

def load_default_dict(request):
    default_dict = {}
    default_dict['user'] = request.user
    return default_dict


def tarefas(request):
	return_dict = load_default_dict(request)
	return_dict['lista_tarefas'] = Task.objects.all()
	return render_to_response('tarefas.html', return_dict)

def tarefas_abertas(request):
	return_dict = load_default_dict(request)
	return_dict['lista_tarefas'] = Task.open_tasks()
	return render_to_response('tarefas.html', return_dict)
	
@login_required
def criar_tarefa(request):
	return_dict = load_default_dict(request)
	if request.POST:
		return_dict['form'] = TaskForm(request.POST)
		if return_dict['form'].is_valid():
			return_dict['form'].save()
			return redirect('/')
		else:
			return render_to_response('criar_tarefa.html', return_dict)
	else:
		return_dict['form'] = TaskForm()
		return render_to_response('criar_tarefa.html', return_dict)

@login_required
def editar_tarefa(request,id):
	return_dict = load_default_dict(request)
	return_dict['task'] = Task.objects.get(pk=id)
	if request.POST:
		return_dict['form'] = TaskForm(request.POST, instance=return_dict['task'])
		if return_dict['form'].is_valid():
			return_dict['form'].save()
			return redirect('/')
		else:
			return render_to_response('editar_tarefa.html', return_dict)
	else:
		
		return_dict['form'] = TaskForm(instance=return_dict['task'])
		return  render_to_response('editar_tarefa.html', return_dict )

@login_required	
def remover_tarefa(request, id):
	if request.POST:
		
		return_dict = load_default_dict(request)
		return_dict['task'] = Task.objects.get(pk=id)
		return_dict['task'].delete()
		return redirect('/') 
	else:
		return redirect('/')