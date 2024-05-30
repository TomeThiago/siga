from django.db import models

class Suporte(models.Model):
  descricao = models.TextField(null=False, blank=False)