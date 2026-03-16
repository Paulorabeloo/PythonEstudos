gamesList = ["Resident Evil 4", "Star Wars Jedi Survivor", "The legend of Zelda", "Red Dead 2", "Mario Odyssey"] #Apenas string
print(gamesList)

# 1 - Tamanho da Lista
print(len(gamesList))

# 2 - Recuperar um item da Lista pelo indice
print(gamesList.index("Mario Odyssey"))

# 3 - Adicionar item ao final da lista
gamesList.append("GTA V")
print(gamesList)

# 4 - Ordenar a lista
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gamesList.copy()
gameReset.remove("Star Wars Jedi Survivor") #remove da lista
print(gameReset)

#6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)