import datetime

class Funcionario():
  aumento = 1.04

  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario
  
  def dados(self):
    return {'nome': self.nome, 'salario': self.salario}

  def aplicar_aumento(self):
    self.salario = self.salario * self.aumento

  @classmethod
  def definir_aumento(cls, valor):
    cls.aumento = valor

  @staticmethod
  def dia_util(dia):
    if dia.weekday() >= 5:
      return False
    return True

fabio = Funcionario('Fabio', 7000)

print(fabio.dados())

# fabio.aplicar_aumento()

# print(fabio.dados())

Funcionario.definir_aumento(1.05)

fabio.aplicar_aumento()

print(fabio.dados())

minha_data = datetime.date(2020, 3, 29)

print(Funcionario.dia_util(minha_data))