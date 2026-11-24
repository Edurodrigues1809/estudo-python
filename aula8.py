# Aula 8 - Coleções (Listas e Tuplas)

# Listas [ 1, 2 , 4.5, eduardo]
frutas = ["acerola", "uva","maçã", "banana"] 
print(frutas[1]) # retorna o valor pelo index
frutas.append("laranja") # adiciona itens na lista
frutas.remove("maçã") # remove itens na lista

frutas[1] = "manga" # substituindo a partir do index
frutas.pop(3) # remove num index específico
frutas.insert(2,"guaraná") # insere um valor num index específico
print(frutas)


print(frutas.index("acerola")) # retorna o index do elemento desejado
frutas.clear() # limpa todos os elementos da lista
frutas.sort() # deixa a lista em ordem alfabetica

frutas2 = frutas.copy() # se não colocar o .copy() as listas ficam a mesma

# Tuplas ("eduardo", 2, 4, 7.2) # Imutáveis
cores = ("vermelho", "amarelo", "verde")
# não suporta alterações como append ou insert
# usado para dias da semana meses nomes proprios
# dados que não variam