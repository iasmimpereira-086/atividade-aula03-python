n1 = int(input("Digite um número positivo: "))
n2 = int(input("Digite um número negativo: "))
print("1 - Média ponderada")
print("2 - Quadrado da soma")
print("3 - Cubo do menor número")
opcao = int(input("Escolha uma opção: "))

if opcao > 0 and opcao <2 :
    resultado = (n1 * 2 + n2 * 3) / 5
    print("Resultado: ", resultado)
elif opcao > 1 and opcao < 4:
    if n1 < n2:
        resultado = n1 * n1 * n1
    else:
        resultado = n2 * n2 * n2
    print("Resultado: ", resultado)
else:
    print("Opção inválida")