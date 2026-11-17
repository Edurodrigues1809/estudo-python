# Sessão de exercícios

#  Crie um código onde é solicitado para o usuário inserir dois valores:
#  o ano atual e o ano de nascimento. O sistema deve calcular quantos anos
#  ele tem de acordo com essas informações e exibir no console.
ano_atual = int(input("Digite o ano em que estamos: "))
nascimento = int(input("Digite o ano em que você nasceu: "))
idade = ano_atual - nascimento
print(f"Se você nasceu em {nascimento} e estamos em {ano_atual}, você tem {idade} anos.")

# Crie um código onde o usuário deve inserir dois números e exiba a soma,
# subtração, multiplicação e divisão deles.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"Soma = {soma}")
print(f"Subtração = {subtracao}")
print(f"Multiplicação = {multiplicacao}")
print(f"Divisão = {divisao}")

# Crie um código onde o usuário deve digitar 3 notas
# escolares e calcular a média delas.
nota1 = int(input("Digite a 1ª nota: "))
nota2 = int(input("Digite a 2ª nota: "))
nota3 = int(input("Digite a 3ª nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media}")