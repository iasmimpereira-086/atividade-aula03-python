while True:
    valor = float(input("Digite o valor da compra(ou 0 para sair): "))
    print('-'* 50)

    if valor == 0:
        print("Encerrando o programa. Até logo!")
        break

    opcao = int(input(f"""[1] Á vista - 15% de desconto
[2] Cartão de débito - 10% de desconto
[3] Cartão de crédito - 5% de desconto
[0] Sair
Selecione a opção que deseja: """))
    print('-' * 50)

    if opcao == 0:
        print("Encerrando o programa. Até logoo!!")
        break
    elif opcao == 1:
        print(f"Desconto: R${valor * 0.15:.2f} | Valor final: {valor * 0.85:.2f}")
    elif opcao == 2:
        print(f"Desconto: R${valor * 0.10:.2f} | Valor final {valor * 0.90:.2f}")
    elif opcao == 3:
        print(f"Desconto: R${valor * 0.05:.2f} | Valor final { valor * 0.95:.2f}")
    else:
        print("Opção inválida! Tente novamente!")
    
    print('-' * 50)