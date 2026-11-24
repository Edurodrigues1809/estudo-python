# Exercicios - Match Case
# 1) Crie um menu com 3 opções:
# Pizza, Sushi, Salada
# O usuário digita um número. O programa o prato escolhido.
print("Menu: ")
print("1 - Pizza")
print("2 - Sushi") 
print("3 - Salada")
Comida = int(input("Escolha entre 1,2 e 3: "))
match Comida:
    case 1:
        print("Você escolheu pizza.")
    case 2:
        print("Você escolheu sushi.")
    case 3:
        print("Você escolheu salada.")
    case _:
        print("Opção inválida")

# 2) Peça para o usuário digitar um meio de transporte.
# Mostre uma mensagem conforme a entrada:
# "carro" -> "Veículo terrestre"
# "bicicleta" -> "Transporte sustentável"
# "avião" -> "Transporte aéreo"
# Caso contrário: "Transporte desconhecido"
veiculo = str(input("Escolha um meio de transporte: "))
match veiculo:
    case "carro":
        print("Veiculo terrestre")
    case "bicicleta":
        print("Veiculo sustentavel")
    case "aviao":
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")