from django.contrib import admin
from notes.models import OrdemServico

class ListNotes(admin.ModelAdmin):
  list_display = ("id", "cliente", "data_inicio", "data_conclusao", "status")
  list_filter = ("status", "cliente", "data_inicio", "data_conclusao")
  search_fields = ("cliente__nome", "descricao")

admin.site.register(OrdemServico, ListNotes)