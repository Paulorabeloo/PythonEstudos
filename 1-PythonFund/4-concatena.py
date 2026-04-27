name = input("Digite o nome do jogo:\n") #input retorna em string
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n")) #input retorna em string, então é necessário converter para inteiro int(input)
gamePrice = float(input("Digite o preço do jogo:\n")) #input retorna em string, então é necessário converter para float float(input)
planIncluded = input("Está incluso no serviço mensal?\n")

#Concatenando os dados utilizando diferentes formas de exibição
#Alternativa 1
print("###Dados do Jogo###")
print("===================")
print("Nome do jogo:", name)
print("Ano de lançamento:", yearLaunch)
print("Preço do jogo:", gamePrice)
print("Está incluido no plano?", planIncluded)

print("\n")

#Alternativa 2
print("Nome do jogo:", name, "\nAno de Lançamento:", yearLaunch, "\nPreço do jogo:", gamePrice, "\nEstá incluido no plano?", planIncluded)

print("\n")

#Alternativa 3 (f-string) -> melhor alternativa
print(f"Nome do Jogo: {name} \nAno de Lançamento: {yearLaunch} \n Preço do jogo: {gamePrice} \nEstá incluido no plano? {planIncluded}")

print("\n")

#Alternativa 4 (concatenação assim só pode ser feita com string, então é necessário converter os outros tipos para string utilizando str())
print("Nome do jogo: " + name + "\nAno de Lançamento: " + str(yearLaunch) + "\nPreço do jogo: " + str(gamePrice) + "\nEstá incluido no plano? " + planIncluded)