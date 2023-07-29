menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = (float(input("Informe o valor do depósito: ")))

        if valor > 0:
            saldo += valor #adiciona o valor no saldo
            extrato += "Depósito: $ {:.2f}\n".format(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Saque")
        
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente para realizar essa operação!")
        elif excedeu_limite:
            print("O valor do saque excede o valor do limite!")
        elif excedeu_saque:
            print("Número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor 
            extrato += "Saque: R$ {:.2f}".format(valor)
            numero_saques += 1
        else:
            print("Operação falhou. O valor informado é inválido!")
    elif opcao == "e":
        print(("*" * 10) + "EXTRATO" + ("*" * 10))
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print("\nSaldo: R$ {:.2f}".format)
        print("*" * 20)



        print("Extrato")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")