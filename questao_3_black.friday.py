valor = int(input("Digite o valor total da venda: "))
print("1 - Á vista (15% de desconto)")
print("2 - Cartão de Débito(10% de desconto)")
print("3 - Cartão de Crédito(5% de Desconto)")

opcao = int(input("Digite a opção da forma de pagamento: "))

if opcao > 0 and opcao < 2:
    desconto = valor * 15 / 100
    final = valor - desconto
    print("valor final", final)
elif opcao > 1 and opcao < 3:
    desconto = valor * 10 / 100
    final = valor - desconto
    print("valor final", final)
elif opcao > 2 and opcao < 4:
    desconto = valor * 5 / 100
    final = valor - desconto
    print("valor final:", final)
else:
    print("opção inválida, tente novamente")