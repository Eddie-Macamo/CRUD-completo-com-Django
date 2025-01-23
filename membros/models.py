from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    bairro = models.CharField(max_length=30)
    numero_celular = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=20)

    def __str__(self):
        return self.nome  # Isso irá mostrar o nome do membro nas listagens
