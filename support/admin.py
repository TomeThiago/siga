from django.contrib import admin
from support.models import Suporte

class ListReports(admin.ModelAdmin):
  list_display = ("id", "descricao")
  
admin.site.register(Suporte, ListReports)