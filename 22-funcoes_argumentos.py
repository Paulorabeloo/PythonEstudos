# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, Lname):
    print(f"Nome completo: {fname} {Lname}")
    
full_name("Rodrigo", "Macedo")

# 2 - Crie uma função que some dois números via parâmetros
def sum(a, b):
    return a + b

print(sum(10, 40))

# 3 - Argumentos default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
    
address()
address("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtdRaintg):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRaintg):
        note = float(input("Digite a nota para o jogo\n"))
        sum += note #sum = sum + note
        print(f"Média de availiaçãpo do jogo {game_name} é: {sum / qtdRaintg}")
rating = int(input("Digite quantas avaliações deseja fazer no jogoz\n"))
rating_game(2)