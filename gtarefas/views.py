from django.shortcuts import render_to_response, redirect
from django.template import Context, loader 
from gt.gtarefas.models import Task
from gt.gtarefas.forms import TaskForm

# Create your views here.

def tarefas(request):
	return_dict = {}
	return_dict['lista_tarefas'] = Task.objects.all()
	return render_to_response('tarefas.html', return_dict)

def tarefas_abertas(request):
	return_dict = {}
	return_dict['lista_tarefas'] = Task.open_tasks()
	return render_to_response('tarefas.html', return_dict)
	
def criar_tarefa(request):
	return_dict = {}
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

def editar_tarefa(request,id):
	return_dict = {}
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
		
def remover_tarefa(request, id):
	if request.POST:
		
		return_dict = {}
		return_dict['task'] = Task.objects.get(pk=id)
		return_dict['task'].delete()
		return redirect('/') 
	else:
		return redirect('/')