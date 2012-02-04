from django.forms import ModelForm
from gt.gtarefas.models import Task
class TaskForm(ModelForm):
	class Meta:
		model = Task