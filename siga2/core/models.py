from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#mexendo nos models, voce tem que fazer um 'makemigrations' e logo depois um 'migrate'

class Curso(models.Model):
	nome = models.CharField(max_length=255)
	codigo_geral = models.CharField(max_length=30)
	#através do 'python manage.py makemigrations' eu adiciono a migration
	
	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.codigo_geral)
		#quando for para representar esse curso, utilize como propriedade o nome do objeto, e não 'curso object'

class Aluno(models.Model):
	nome = models.CharField(max_length=255)
	cpf = models.CharField(max_length=14)
	score = models.DecimalField(default=0, max_digits=3, decimal_places=1)
	curso = models.ForeignKey(Curso)
	data_de_nascimento = models.DateField()
	user = models.OneToOneField(User)

	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.curso.nome)

class Disciplina(models.Model):
	nome = models.CharField(max_length=255)
	codigo_geral = models.CharField(max_length=10)
	curso = models.ForeignKey(Curso)
	data_de_insercao = models.DateField()
	eh_eletiva = models.BooleanField()

	def __str__(self):
		return '{0} - CURSO: {1}'.format(self.nome, self.curso.nome)