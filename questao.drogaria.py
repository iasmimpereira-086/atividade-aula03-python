print("""----------------------------------------------
        nome        |            preço
    Dipirona        | 4.5
    Paracetamol     | 7.0
    Ibuprofeno      | 12.5
    Amoxicilina     | 18.0
    Omeprazol       | 9.9
    -------------------------------------------------
    Medicamento mais barato - R$4.5
    Media aritmetica dos preços: R$ 10.38""")

contador = 1
soma = 0

nome_mais_barato = ""
preco_mais_barato = 0

while contador <= 5:
    print(f"Medicamento: {contador}")
    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))

    soma = soma + preco

    if contador == 1:
        nome_mais_barato = nome
        preco_mais_barato = preco
    else:
        if preco < preco_mais_barato:
            nome_mais_barato = nome
            preco_mais_barato = preco

    contador = contador + 1

media = soma / 5

print(f"O medicamento mais barato é:  {nome_mais_barato}")
print(f"Preço: {preco_mais_barato}")
print(f"Media dos preços: {media}")