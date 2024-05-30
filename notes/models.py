from django.db import models
from costumers.models import Cliente

class OrdemServico(models.Model):
  PENDENTE = 'Pendente'
  EM_ANDAMENTO = 'Em andamento'
  FECHADO = 'Fechado'
    
  STATUS_CHOICES = [
    (PENDENTE, 'Pendente'),
    (EM_ANDAMENTO, 'Em andamento'),
    (FECHADO, 'Fechado'),
  ]
    
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='notes')
  descricao = models.TextField()
  data_inicio = models.DateField(auto_now_add=True)
  data_conclusao = models.DateField(null=True, blank=True)
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default=PENDENTE,
  )
  
  def __str__(self):
    return f"{self.descricao} - {self.cliente.nome} - {self.status}"