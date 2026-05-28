senha_correta = 123456

for tentativas in range(3):
    senha_digitada = int(input("Digite a sua senha!: "))

    if senha_digitada == senha_correta:
        print("Olá,Matheus. Seja bem-vindo ao nosso banco!!")
        break
    elif tentativas == 0:
        print("Senha incorreta! Você ainda tem 2 tentativas!")
    elif tentativas == 1:
        print("Senha incorreta! Você ainda tem 1 tentativa!")
    elif tentativas == 2:
        print("Sua senha foi bloqueada!Por favor dirija-se a um de nossos caixas. ")