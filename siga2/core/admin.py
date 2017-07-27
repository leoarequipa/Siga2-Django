from __future__ import unicode_literals

from django.contrib import admin
from .models import Curso, Aluno, Disciplina

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Disciplina)