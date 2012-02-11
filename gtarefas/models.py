# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(u"Nome", max_length=50)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    name = models.CharField(u"Nome", max_length=200)
    gender = models.CharField(u"Gênero", max_length=2, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    title = models.CharField(u"Título", max_length=200)
    description = models.TextField(u"Descrição")
    status = models.ForeignKey(Status)
    responsible = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


    def closed(self):
        if self.status == 'closed':
		    return True
        else:
		    return False

    @classmethod	
    def open_tasks(self):
	    return Task.objects.exclude(status="closed")

    @classmethod	
    def user_tasks(self, responsible_name):
        resp = Person.objects.get(name=responsible_name)
        return Task.objects.filter(responsible=resp)
	

		