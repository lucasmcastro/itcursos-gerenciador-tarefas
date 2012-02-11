from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('gt.gtarefas.views',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tarefas'),
    url(r'^tarefas/$', 'tarefas'),
    url(r'^tarefas_abertas/$', 'tarefas_abertas'),
    url(r'^criar_tarefa/$', 'criar_tarefa'),
    url(r'^editar_tarefa/(?P<id>\d+)$', 'editar_tarefa'),
	url(r'^remover_tarefa/(?P<id>\d+)$', 'remover_tarefa'),
	
)