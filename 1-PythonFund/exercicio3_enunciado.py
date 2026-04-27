"""
Exercício 3:
* Cálculo da Distância:
-> Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,35 para viagens mais longas

*Aumento salário funcionário:
-> Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$  1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%.
"""

distancia = float(input("Digite a distância que deseja percorrer em km\n"))

if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.35 * distancia
print(f"Preço da viagem: {preco:.2f}")

print("---------------------")

salario = float(input("Digite o salário do funcionário para calcular o valor do aumento\n"))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f"Aumento: {aumento}")