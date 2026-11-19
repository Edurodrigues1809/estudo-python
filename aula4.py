# Aula 4 - Condicionais
# if e else
idade = int(input("Qual é a sua idade? "))
if idade > 17:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

senha = "1234"
tentativa = input("Digite sua senha: ")
if tentativa == senha:
    print("Acesso liberado")
    print("Seja bem vindo")
if tentativa != senha:
    print("Acesso negado")

print(type(True)) # bool

