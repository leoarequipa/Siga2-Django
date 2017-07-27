"""siga2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from core.views import home
from core.views import form
from core.views import ListaAlunos as listagem, ListaDetalhe as aluno, LoginView as login, logout, profile

#arquivo responsável por fazer o match de tudo que está após a barra do endereço url.
#ex: o ~mvmf do cin.ufpe.br/~mvmf

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^form/$', form, name='form'),
    url(r'^listagem/$', listagem.as_view(), name='listagem'),
    url(r'^aluno/(?P<pk>\d+)$', aluno.as_view(), name='aluno'),
    url(r'^login$', login.as_view(), name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^profile$', profile, name='profile'),
]
