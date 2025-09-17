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
        deposito = int(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")



    elif opcao == "s":
        valor = int(input("Digite o valor de saque: "))
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        excedeu_limite = valor > limite
        
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("operação falhou, você não possui saldo sufiiciente")

        elif excedeu_limite:
            print("operação falhou, você excedeu o limite de saque")

        elif excedeu_saques:
            print("operação falhou, você excedeu o núemro de saques diários")

        elif valor > 0:
            saldo -= valor
            extrato += f"Valor de saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso")


    elif opcao == "e":
        print("\n============EXTRATO=============")
        print(f"\nSaldo Atual: R$ {saldo:.2f}")    
        print("\n==================================")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")