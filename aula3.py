# Aula 3 - Entradas
# O código pede um valor e você fornece no terminal
nome = input("Digite o seu nome: ")

# misturar mensagem com variável
print(f"Prazer em te conhecer, {nome}")

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")
resultado = num1 + num2
print(f"A soma de {num1} + {num2} é igual a {resultado}")
# o resultado de 8 e 9 deu 89 pois foi feita uma soma de strings

# Jeito certo =
num1 = int(input("Digite um numero: ")) # declare o tipo da variável
num2 = int(input("Digite outro numero: "))
resultado = num1 + num2
print(f"A soma de {num1} + {num2} é igual a {resultado}")
# o resultado de 8 e 9 deu 17 :)
