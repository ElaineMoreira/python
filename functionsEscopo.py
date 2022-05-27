# trabalhando com funcoes
# testado no terminal
def imc (peso, altura):
  return peso / (altura/100) ** 2

imc(55, 152)

# trabalhando com escopo
# testado no terminal
# se printar ainda dara 10, e nao 11 caso o x = 10
 def incrementa (x):
   x = x + 1
   return x
