from django.contrib import admin
from costumers.models import Cliente

class ListCostumers(admin.ModelAdmin):
  list_display = ("id", "nome", "email", "endereco", "telefone")

admin.site.register(Cliente, ListCostumers)
