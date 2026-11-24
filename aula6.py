# Aula 6 - Match Case

opcao = int(input("Escolha uma opção (1 a 3): "))
match opcao:
    case 1:
        print("Opcao um")
    case 2:
        print("Opcao dois")
    case 3:
        print("Opcao tres")
    case _:   # _ = "else" do match case
        print("Opcao invalida")

# Uso do "|" como "or"

nota = int(input("Sua nota: "))
match nota:
    case 10 | 9:
        print("Excelente")
    case 8 | 7:
        print("Muito bom")
    case 6 | 5:
        print("Da pra melhorar...")
    case 4 | 3 | 2 | 1 | 0:
        print("Reprovado")