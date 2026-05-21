print("""Calculadora de Números Reais
      1. Soma
      2. Subtração
      3. Divisão
      4. multiplicação""")
print("*"*30)
opcao = int(input("Escolha a opção desejada: "))
if(opcao ==1 or opcao ==2 or opcao ==3 or opcao ==4):
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
if opcao ==1:
    print(f"O resultado da soma é:{n1} + {n2}= {n1 + n2}")
elif opcao ==2:
    print(f"O resultado da subtração é:{n1} - {n2} = {n1 - n2}")
elif opcao ==3:
    print(f"O resultado da divisão é:{n1} / {n2} = {n1 / n2:.2f}")
elif opcao ==4:
    if n2 !=0:
        print(f"O resultado da multiplicação é:{n1} * {n2} = {n1 * n2}")
    else:
        print("Erro. Divisão por zero!!!")
else:
    print("Operação inválida! Tente novamente")