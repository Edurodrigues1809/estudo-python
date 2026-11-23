# Aula 5 - Elif
nota = float(input("Digite sua nota: "))
if nota >= 90:
    print("Nota A+")
elif nota >= 80:      # Para verificar essa condição 
    print("Nota B")   # a de cima precisa ser falsa
elif nota >= 60:
    print("Nota C")
elif nota >= 40:
    print("Nota D")
else:
    print("Nota F")


idade = int(input("Digite sua idade: "))
carteira = False
if idade > 17:
    print("Você tem idade para dirigir.")
    if carteira:
        print("E está habilitado para dirigir.")
    else:
        print("Porém, não possui carteira.")
else:
    print("Você não tem idade para dirigir")

