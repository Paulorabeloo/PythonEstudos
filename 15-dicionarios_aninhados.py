import pprint

#dicionario pai
gamesDict = {
    #dicionarios filhos / 3 dicionarios dentro de um dicionario
    "resident evil 4":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre":["ação", "aventura"]
    },
    "mario odyssey":{
        "yearLaunch": 2017,
        "classification":10.0,
        "genre":["aventura", "3d"]
    },
    "donkey kong country":{
        "yearLaunch": 1995,
        "classification": 9.5,
        "genre":["aventura", "plataforma"]
    }
}

print(gamesDict)

#melhor legibilidade
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)


# 1 - Buscar informação dentro de um dicionario aninhado
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionar novo item
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])

# 3 - Excluir um dicionário
del gamesDict["resident evil 4"]
pp.pprint(gamesDict)