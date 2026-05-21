soma = 0
quantidade = 0
maior = 0
numero = int(input("Digite um número positivo (negativo para parar): "))

while numero >=0:
    soma = soma + numero
    quantidade = quantidade + 1
    if quantidade == 1 or numero > maior:
        maior = numeronumero = int(input(" Digite um número positivo (negativo para parar): "))

media = soma / quantidade
print(f"soma: {soma}")
print(f"Média: {media}")
print("Maior número: ")