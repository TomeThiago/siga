from django.contrib import admin
from technician.models import Tecnico

class ListTechnicians(admin.ModelAdmin):
  list_display = ("id", "nome", "especialidade")

admin.site.register(Tecnico, ListTechnicians)