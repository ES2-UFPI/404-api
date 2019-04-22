from django.db import models

class Cliente(models.Model):

    class Meta:
        dt_table: 'Cliente'

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    celular = models.CharField(max_length=14)

class Portal(models.Model):

    class Meta:
        dt_table: 'Portal'

    universidade = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    area_conhecimento = models.CharField(max_length=100)
    nome_do_curso = models.CharField(max_length=255)
    nome_do_coordenador = models.CharField(max_length=255)
    nome_do_chefe_departamento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    endereco = models.CharField(max_length=255)
    telefone_1 = models.CharField(max_length=14)
    telefone_2 = models.CharField(max_length=14)
    telefone_3 = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
