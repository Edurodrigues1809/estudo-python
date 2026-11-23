# Lista de exercicios envolvendo condicionais (if, else e elif)

# Verificador de nota mínima
# 1) Crie um código que pergunte ao usuário qual foi sua nota em um teste.
# Defina uma nota mínima para aprovação (por exemplo, 7). Use a
# estrutura IF para verificar se a nota do usuário é maior ou igual a
# nota mínima. Se for, exiba a mensagem "Passou por média!"

nota = int(input("Digite sua nota: "))
if nota < 0 or nota > 10:
    print("Nota Invalida")
if nota > 6 and nota <= 10:
    print("Passou por média!")
if nota >= 0 and nota < 7:
    print("Reprovado :(")

# 2) Verificação de Diferença
# Crie um código que peça ao usuário para inserir 2 nomes. Depois,
# verifique se os dois nomes são diferentes. Caso sim, exiba "Os nomes
# digitados são diferentes"

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")
if nome1 != nome2:
    print("Os nomes são diferentes")
else:
    print("Os nomes são iguais")

# 3) Elegibilidade para um Evento (Idade mínima)
# Imagine um evento para maiores de 18 anos, crie um código que
# pergunte a idade do usuário. Verifique se a idade do usuário é 
# maior ou igual a 18, caso sim exiba "Evento liberado!"

idade = int(input("Qual a sua idade? "))
if idade >= 18:
    print("Evento liberado!")
else:
    print("Acesso bloqueado")


# Condicionais Else e Elif

# 1) Peça ao usuário uma nota de 0 a 10 para um filme.

nota = int(input("Digite a nota do filme: "))
if nota >= 0 and nota <= 10:
    if nota > 8:
        print("Exelente")
    elif nota > 6:
        print("Bom")
    elif nota > 4:
        print("Regular")
    else:
        print("Ruim")
else:
    print("Nota inválida")

# 2) Seu programa deve verificar se o usuário tem direito ao
# frete grátis. Se o valor da compra for maior ou igual a 100
# e o cliente estar cadastrado no programa de fidelidade

fidelidade = input("Está cadastrado no programa? (sim/não): ").strip().lower()
compra = int(input("Digite o valor da sua compra: "))
if fidelidade == "sim" or fidelidade == "s":
    fidelidade = True
else:
    fidelidade = False
if compra >= 100 and fidelidade:
    print("Frete grátis aplicado")
else:
    print("Frete não disponivel")