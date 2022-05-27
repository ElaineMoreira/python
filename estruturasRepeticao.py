pantheon_of_arton = [
    {'nome': 'Wynna', 'dominio': 'Magia'},
    {'nome': 'Nimb', 'dominio': 'Sorte'},
    {'nome': 'Ahadarak', 'dominio': 'Tormenta'},
  ]
print(pantheon_of_arton)

# fazer lista de dominios
domains = []

for god in pantheon_of_arton:
  domains.append(god['dominio'])

print(domains)

# vamos fitrar a lista, uero excluir o dominio da tormenta

domains = [god 
  for god in pantheon_of_arton
  if god['dominio'] != 'Tormenta']
print(domains)

# vamos filtrar so a tormenta

domains = [god
  for god in pantheon_of_arton
  if god['dominio'] == 'Tormenta']
print(domains)