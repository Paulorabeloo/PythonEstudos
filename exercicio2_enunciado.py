"""
Exercicio2:
* Substituindo caractere repetido;
-> Escreva um programa Python para obter uma string de uma determinada string em
que todas as ocorrências de seu primeiro caractere foram alteradas para '$',
exceto o próprio primeiro caractere
ex: fifa 23 -> fi$a 23

*Troca de cacteres:
-> Escreva um programa python para obter uma única string de duas strings fornecidas
separadas por um espaço e troque os dois primeiros caracteres de cada string.
ex: abc xvz -> xvc abz
"""

gameName = "Fifa 23"
print(gameName + " -> " + gameName.replace("f", "$"))

line = "="
print(line * 25 + "\nEx2 :")

gameName = "abc xvz"
gameName.split(" ")
gameName.replace("c", "z")
gameName.replace("z", "c")
print(gameName)