# Aula 7 - Manipulação de Strings
fruta = "Melancia"
print(fruta[0]) # fatiamento de strings, retorna a primeira letra
# Funcionam por meio de index, sequência que começa em 0
print(fruta[0:2]) # retorna as 2 primeiras letras
print(fruta[:4])

frase = "eu amo python!"
tamanho = len(frase) # conta a quantidade de caracteres
print(f"A frase: {frase} ; tem {tamanho} caracteres")

frase = "eu amo python!"
contagem = frase.count("o") # conta a quantidade de tal carctere
print(contagem)

frase = "eu amo python!"
print(frase.find("m")) # diz, em index, a posição do elemento

frase = "Eu amo python!"
if "python" in frase:    # encontrar elemento no conjunto
    print("A palavra python está na frase")
else:
    print("A palavra python não está na frase")

print(frase.lower()) # deixa tudo minúsculo
print(frase.upper()) # deixa tudo maiúsculo
print(frase.capitalize()) # deixa a 1ª letra da frase em maiúsculo
print(frase.title()) # deixa a 1ª letra de cada palavra em maiúculo
print(frase.strip()) # remove os espaços vazios
print(frase.replace("Eu","Ele")) # troca um valor por outro
