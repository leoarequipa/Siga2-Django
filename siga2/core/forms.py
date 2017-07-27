from django import forms
from .models import Curso, Aluno
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

'''class MatriculaForm(forms.Form):
	nome = forms.CharField(max_length=100)
	cpf = forms.CharField(max_length=14)
	score = forms.DecimalField(max_value=10.0, min_value=0.0, max_digits=3, decimal_places=1)
	curso = forms.ModelChoiceField(queryset=Curso.objects.all())#queryset é uma lista de objetos, assim como em model. ela lista os registros no banco de dados
	data_de_nascimento = forms.DateField()

	def save(self):
		data = self.cleaned_data
		novo_aluno = Aluno(**data)
		novo_aluno.save()
		return novo_aluno'''

class MatriculaModelForm(forms.ModelForm):

	email = forms.EmailField()
	senha = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Aluno
		fields = ['nome', 'cpf', 'data_de_nascimento', 'curso', 'email', 'senha']

	def clean(self):
		data = super(MatriculaModelForm, self).clean()

		if User.objects.filter(username=data.get('email')).count() > 0:
			raise ValidationError('Username ja usado', code='invalid_username')

		'''user = User.objects.create_user(data.get('email'), data.get('email'), data.get('senha'))
		data['user']=user'''
		return data

	def save(self, *args, **kwargs):
		user = User.objects.create_user(self.cleaned_data.get('email'), self.cleaned_data.get('email'), self.cleaned_data.get('senha'))
		
		self.instance.user = user
		self.instance.score = 5
		return super(MatriculaModelForm, self).save(self)

class LoginForm(forms.Form):
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())