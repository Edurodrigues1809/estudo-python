# Exercicios envolvendo manipulação de strings

# 1) Programa que peça ao usuário para digitar uma palavra
# e mostre a primeira e a ultima letra da palavra
palavra = input("Digite uma palavra: ")
print(f"Primeira letra: {palavra[0]}")
print(f"Última letra: {palavra[-1]}")

# 2) Peça ao usuário uma frase e dois números: ínicio e fim.
# Mostre o fatiamento da frase entre esses índices.
frase = input("Digite uma frase: ")
print("Fatie a frase entre esses 2 numeros [x,y]:")
x = int(input("Digite X: "))
y = int(input("Digite Y: "))
print(frase[x:y])

# 3) Peça ao usuário para escrever uma mensagem. Verifique
# se ela contém a palavra "bomba", e imprima um alerta se sim.
mensagem = input("Digite uma mensagem: ")
if "bomba" in mensagem:
    print("ALERTA: mensagem explodiu")
else:
    print("Tranquilo")

# 4) Dada uma variável [ frase = @prendendo @ progr@m@r ]
# com espaços nas pontas e letras bagunçadas, o programa deve:
# remover os espaços do inicio e do fim, trocar "@" por "a" e
# colocar a primeira letra de cada palavra em maiúsculo.
frase = "   @prendendo @ progr@m@r   "
frase = frase.strip()
frase = frase.replace("@", "a")
frase = frase.title()
print(frase)