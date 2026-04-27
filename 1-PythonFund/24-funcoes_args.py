"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos
queremos ter numa função.
- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário
"""

# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n# sum_total = sum_total + n
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7,8)
sum(7, 10 , 9 , 8, 7, 6 , 5)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
        
print("###Curso###")
presentation(name="Python", category="Backend", Level="Iniciante")
presentation(name="Visão Computacional com Python", category="IA", Level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", Level="Intermediário")


