num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Operadores Artiméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2 #resto de uma divisão ex (3 % 2 = 1)
exp = num1 ** num2 #elevado ex (4^2 = 4 * 4)

print(sum)
print(sub)
print(div)
print(mult)
print(f"Resto da divisão de {num1} por {num2} é {mod}")
print(f"Potência do número {num1} por {num2} é {exp}")


# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"Os números {num1} é maior ou igual a {num2}? {bigger_equal}")


#Operadores de Atribuição
# =
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1
