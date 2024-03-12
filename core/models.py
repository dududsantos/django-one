from django.db import models

class Produto(models.Model):
  nome = models.CharField('Nome', max_length=100)
  preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
  estoque = models.IntegerField('Quantidade em Estoque')

  def __str__(self):
    return self.nome

class Cliente(models.Model):
  nome = models.CharField('Nome', max_length=100)
  sobrenome = models.CharField('Sobrenome', max_length=100)
  email = models.EmailField('E-mail', max_length=100)
  cpf = models.CharField('CPF', max_length=11)
  data_nascimento = models.DateField('Data de Nascimento')
  ativo = models.BooleanField('Ativo', default=True)
  criado = models.DateTimeField('Criado em', auto_now_add=True)
  atualizado = models.DateTimeField('Atualizado em', auto_now=True)

  def __str__(self):
    return f'{self.nome} {self.sobrenome}'