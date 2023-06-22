# importar no python
from random import randint

pantheon_of_arton = [
    {'nome': 'Wynna', 'dominio': 'Magia'},
    {'nome': 'Nimb', 'dominio': 'Sorte'},
    {'nome': 'Ahadarak', 'dominio': 'Tormenta'},
  ]
print(pantheon_of_arton)

# rolagem de dados entre 1 e 20
# vai me mostrar numeros aleatorios
dice_roll = randint(1, 20)
print(dice_roll)

# fazendo uma condicional em python
if dice_roll == 1:
  print("Vish... Deu ruim!"),
elif 2 <= dice_roll <= 15:
  print("Ahadarak... porque me atormentas!")
elif 16 <= dice_roll <= 19:
  print("Nimb, obrigado pela sorte")  
else:
  print("Agora ninguem me seguraaaa!")