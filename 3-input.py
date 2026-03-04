# Utilizando o Input(comando de entrada)
# \n quebra de linha

'''
Jogoteca
'''

name = input("Digite o nome do jogo:\n") #input retorna em string
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n")) #input retorna em string, então é necessário converter para inteiro int(input)
gamePrice = float(input("Digite o preço do jogo:\n")) #input retorna em string, então é necessário converter para float float(input)
planIncluded = input("Está incluso no serviço mensal?\n")

print(name)
print(yearLaunch)
print(gamePrice)
print(planIncluded)