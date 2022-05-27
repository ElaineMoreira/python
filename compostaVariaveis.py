# listas (como se fosse arrays)
great_chess_players = ['Magnus carlsen', 'Fabiano Caruana']
print(great_chess_players)
# acessa pelo index
print(great_chess_players[0])
print(great_chess_players[1])
# adicionar novo nome na lista
great_chess_players.append('Elaine Moreira')
print(great_chess_players)
# remove nome da lista
great_chess_players.remove('Elaine Moreira')
print(great_chess_players)
# criando uma outra lista
more_chess_players = ['Hikaku Nakamura', 'Viswanathan', 'Alireza Firouzja']
print(more_chess_players)
# usando "extend"
great_chess_players.extend(more_chess_players)
print(great_chess_players)
# pode passar atraves da lista "great_chess_players([])"

# tupla
world_Champion = ('Magnus carlsen', 1)
print(world_Champion[0]) # pode acessar pelos indices
print(world_Champion[1]) # pode acessar pelos indices

print(great_chess_players)

# fazendo ranking
great_chess_players_ranking = [world_Champion]
print(great_chess_players_ranking)

# incluindo na tupla do ranking
great_chess_players_ranking.append(('Fabiano karuana', 2))
print(great_chess_players_ranking)

# incluindo mais jogadores com extend
great_chess_players_ranking.extend(
  [
    (great_chess_players[2], 18), 
    (great_chess_players[3], 15),
    (great_chess_players[4], 21)
  ]
)
print(great_chess_players_ranking)

# uso do dicionario
jogador = { 'nome': 'Elaine', 'cidade': 'Belo Horizonte' }
print(jogador)
# tupla
jogador = ['Elaine', 'Belo Horizonte']
print(jogador[0])

# criando conjuntos de pessoas que trabalha na trybe
admin_user = {'Alberto', 'Gabi'}
data_squad = {'Gabi', 'Nakano', 'Lucca'}
print(admin_user)
print(data_squad)
# quem do data_squad tem privilegios de admin_user?
intersection = admin_user.intersection(data_squad)
print(intersection)

# todas as pessoas que tem cadastro
all_users = {'Alberto', 'Gabi', 'Leticia Bora', 'Lucca', 'Nakano', 'Mateus Goyas'}
print(all_users)
# qual dessas pessoas nao tem acesso ao admin?
diference = all_users.difference(admin_user)
print(diference)
# quero que todos tenham privilegios de admin
union = admin_user.union(diference)
print(union)
print(admin_user)
