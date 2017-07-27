from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import MatriculaModelForm, LoginForm
from .models import Aluno, Curso, Disciplina

# Create your views here.

def home(request):
	return render(request, 'core/index.html', locals())
	
def form(request):

	msg = ''

	if request.method == 'POST':

		form = MatriculaModelForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'Cadastro efetuado com sucesso'
		else:
			msg = 'Ocorreu um erro'

	form = MatriculaModelForm()
	return render(request, 'core/form.html', {
					'form':			form,
					'msg':			msg
					})

class ListaAlunos(ListView):
	template_name='core/listagem.html'
	model = Aluno

class ListaDetalhe(DetailView):
	template_name='core/aluno.html'
	model = Aluno

def logout(request):
	auth_logout(request)
	return redirect('/')

@login_required
def profile(request):
	return render(request, 'core/profile.html', {'user':request.user})

class LoginView(View):
	template_name='core/login.html'
	def get(self, request):
		form =LoginForm()
		return render(request, 'core/login.html', {'form':form})
	
	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('email')
			password = form.cleaned_data.get('senha')
			user=authenticate(request, username=username, password=password)
			if user is not None:
				auth_login(request, user)
				return redirect('/profile')

			else:
				msg ='Email ou Senha Incorreto'
				return render(request, 'core/login.html', {'form':form, 'msg':msg})


'''def another(request):
	return render(request, 'core/another.html', locals())

{
		'nome': 		'Mateus',
		'periodo': 		'2',
		'curso': 		'Engenharia da Computação',
		'code':[		'C',
						'Pascal',
						'HTML',
						'CSS',
						'JavaScript'],
		'hobbies':[		'Tecnologia',
						'Matemática',
			 			'Vôlei',
			  			'Viajar',
		   				'Cultura japonesa'],
		'curriculum':[	'ENSINO MÉDIO - 2012 (COLÉGIO MÓDULO, SALVADOR, BA)',
						'FCE - FIRST CERTIFICATE IN ENGLISH - 2010',
						'TOEFL ITP - 2015']
	})'''