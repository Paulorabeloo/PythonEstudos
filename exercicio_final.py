teams = {}
done = False

#Função para listar times
def print_teams():
    print("Times Listado:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

while not done:
    # Opções no programa
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remove um time")
    print("3. Listar times")
    print("4. Adicionar jogadores em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input("> ")
    if choice == "1":
        team_name = input("Digite o nome do time\n")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado.")
    elif choice == "2":
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            del teams[team_name]
            print("Time removido")
        else:
            print("Número do time inválido")
    elif choice == "3":
        print_teams()
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        done = True
    else:
        print("Opção inválida")