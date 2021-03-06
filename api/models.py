import subprocess
from django.db import models


class Portal(models.Model):
  identificador = models.CharField(max_length=255)
  universidade = models.CharField(max_length=255)
  departamento = models.CharField(max_length=255)
  area_conhecimento = models.CharField(max_length=100)
  nome_do_curso = models.CharField(max_length=255)
  nome_do_coordenador = models.CharField(max_length=255)
  nome_do_chefe_departamento = models.CharField(max_length=255)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=2)
  cep = models.CharField(max_length=8)
  bairro = models.CharField(max_length=255)
  rua = models.CharField(max_length=100)
  numero = models.CharField(max_length=5)
  endereco = models.CharField(max_length=255)
  telefone_1 = models.CharField(max_length=14)
  telefone_2 = models.CharField(max_length=14)
  email = models.CharField(max_length=100)
  nome_solicitante = models.CharField(max_length=255)
  cpf_solicitante = models.CharField(max_length=11)
  email_solicitante = models.CharField(max_length=100)
  telefone_solicitante = models.CharField(max_length=14)
  celular_solicitante = models.CharField(max_length=14)

  class Meta:
    dt_table: 'Portal'

  def create_container(self):
    identificador = self.identificador
    subprocess.call(["sudo", "docker", "run", "-p", "8000:8000", "-d", "--name", identificador, "-i", "-t", "django_application_image"])

def clone():
  subprocess.call(["git", "clone", "https://github.com/ES2-UFPI/404-portal.git"])

def delete_portal():
  subprocess.call(["rm", "-rf", "404-portal"])

def docker_image():
  subprocess.call(["sudo", "docker", "build", "-t", "django_application_image", "."])
