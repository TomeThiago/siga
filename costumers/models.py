from django.db import models

class Cliente(models.Model):
  nome = models.CharField(max_length=255, null=False, blank=False)
  email = models.CharField(max_length=255, null=False, blank=False)
  endereco = models.CharField(max_length=255, null=False, blank=False)
  telefone = models.CharField(max_length=20, null=False, blank=False)
  
  def __str__(self):
    return self.nome
