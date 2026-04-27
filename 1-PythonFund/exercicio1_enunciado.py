"""
Exercício 1:
*Antecessor e sucessor de um número:
-> Escreva um programa em python que leia um número e represente o número antecessor e
sucessor desse número que foi lido, utilizando operadores de atribuição.

Ex 2:
* Média de 4 notas:
-> Escreva um programa em Python que leia quatro números e calcule a média entre esses
números
"""

num = int(input("Digite um número: "))
numAntecessor = num -1
numSucessor = num + 1

print(f"Número antecessor: ", numAntecessor)
print(f"Numéro sucessor: ", numSucessor)


print("----------EX2------------")
print("\n")

num1 = float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

media = (num1 + num2 + num3 + num4) / 4
print(f"A média dos números {num1} + {num2} + {num3} + {num4} é: ", media)



