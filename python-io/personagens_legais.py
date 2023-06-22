# characters_file = open("meus-persongens-favoritos.txt", mode="w")

# characters_file.write("Tio Patinhas\n")
# characters_file.write("Neo\n")
# characters_file.write("Homem Aranha\n")

# print("Batman", file=characters_file)

# more_characters = ["Hulk\n", "Thor\n"]

# characters_file.writelines(more_characters)

# characters_file.close()

############ JSON ############

# import json

# with open("superheroes.json") as superheroes_file:
#   superheroes_list = json.load(superheroes_file)
#   for superheroe in superheroes_list:
#     print(superheroe["after_ego"])

############ CSV ############

# import csv

# with open("dc-wikia-data.csv") as superheroes_file:
#   superheroes_list = csv.DictReader(superheroes_file)
#   for superheroe in superheroes_list:
#     print(superheroe["name"])
#     print(superheroe)

## cabecalho impresso ##

import csv

with open("dc-wikia-data.csv") as superheroes_file:
  header, *superheroes_list = csv.reader(superheroes_file)
  print(header)