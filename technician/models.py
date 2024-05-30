from django.db import models

class Tecnico(models.Model):
  nome = models.CharField(max_length=255, null=False, blank=False)
  especialidade = models.CharField(max_length=255, null=False, blank=False)
  
  def __str__(self):
    return self.nome