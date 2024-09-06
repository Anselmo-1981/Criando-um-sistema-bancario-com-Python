cliente = "Bernardo Soares"
saldo = [300.00]
tipo_de_operacao = ["Saldo Inicial"]
saldo_apos_operacao = [300.00]
n=0
x=0
bco_monetizar = "Banco Monetizar"
apresentacao = f""" ###################################### {bco_monetizar} ###################################### 

\t\tBem-vindo {cliente}, é um prazer ter você como cliente.

\t\tSaldo disponível em conta corrente R$ {saldo[n]:.2f}.

\t\tDigite:
\t\t[1] Sacar;
\t\t[2] Depositar;
\t\t[3] Extrato;
\t\t[4] Sair.
"""


conta_logada = True
print("\n\n",apresentacao)


while conta_logada == True:


    opcao = int(input("\t\tDigite agora a opção escolhida: "))
    while opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:

        # saque
        if opcao == 1:


            saque = float(input("\t\tInforme o valor que deseja sacar R$: "))
            if saque <= 500.00 and x < 3 and saque <= sum(saldo):

                # adiciona ao final da lista saldo
                saldo.append(-(saque))

                tipo = "    Saque    "
                # adiciona ao final da lista tipo de operação
                tipo_de_operacao.append(tipo)

                # soma os valores da lista saldo
                valor = sum(saldo)
                valor = float(valor)
                # adiciona ao final da lista saldo_apos_operacao
                saldo_apos_operacao.append(valor)

                print(f"\t\tSaque de R$ {saque:.2f} efetuaddo com sucesso.")
                print(f"\t\tSaldo em conta atualizado R$ {sum(saldo):.2f}.")
                x += 1
                print()
                print(f" ###################################### {bco_monetizar} ###################################### ")
                print()

                print("\t\tDigite:")
                print("\t\t[1] Sacar;")
                print("\t\t[2] Depositar;")
                print("\t\t[3] Extrato;")
                print("\t\t[4] Sair.\n")
                opcao = int(input("\t\tDigite agora a opção escolhida: "))


            elif saque > 500.00:

                print(f"\t\tPor motivo de segurança a operação não foi realizada.")
                print(f"\t\tVocê pode fazer até 3 saques diários de até R$ 500,00 / cada um.")
                print(f"\t\tTotal de saques efetuados hoje: {x}")
                print()
                print(f" ###################################### {bco_monetizar} ###################################### ")
                print()

                print("\t\tDigite:")
                print("\t\t[1] Sacar;")
                print("\t\t[2] Depositar;")
                print("\t\t[3] Extrato;")
                print("\t\t[4] Sair.\n")
                opcao = int(input("\t\tDigite agora a opção escolhida: "))


            elif x >= 3:

                print(f"\t\tVocê atingiu o limite de saques diários ({x}), por favor volte amanhã.")
                print(f"\t\tÉ um prazer tê-lo como cliente.")
                print()
                print(f" ###################################### {bco_monetizar} ###################################### ")
                print()

                print("\t\tDigite:")
                print("\t\t[1] Sacar;")
                print("\t\t[2] Depositar;")
                print("\t\t[3] Extrato;")
                print("\t\t[4] Sair.\n")
                opcao = int(input("\t\tDigite agora a opção escolhida: "))


            elif saque > sum(saldo):

                print(f"\t\tSaque não permitido, saldo insuficiente.")
                print(f"\t\tSaldo disponível para saque R$ {sum(saldo):.2f}.")

                print()
                print(f" ###################################### {bco_monetizar} ###################################### ")
                print()

                print("\t\tDigite:")
                print("\t\t[1] Sacar;")
                print("\t\t[2] Depositar;")
                print("\t\t[3] Extrato;")
                print("\t\t[4] Sair.\n")
                opcao = int(input("\t\tDigite agora a opção escolhida: "))


            else:
                pass


        # depósito
        elif opcao == 2:


            deposito = float(input("\t\tInforme o valor que deseja depositar R$: "))
            if deposito > 0:

                # adiciona ao final da lista saldo
                saldo.append(deposito)

                tipo = "    Depósito "
                # adiciona ao final da lista tipo de operação
                tipo_de_operacao.append(tipo)

                valor = sum(saldo)
                valor = float(valor)
                #saldo_atualizado = valor
                # adiciona ao final da lista saldo_apos_operacao
                saldo_apos_operacao.append(valor)

                print(f"\t\tDepósito de R$ {deposito:.2f} efetuaddo com sucesso.")
                print(f"\t\tSaldo em conta atualizado R$ {sum(saldo):.2f}")
                print()
                print(f" ###################################### {bco_monetizar} ###################################### ")
                print()

                print("\t\tDigite:")
                print("\t\t[1] Sacar;")
                print("\t\t[2] Depositar;")
                print("\t\t[3] Extrato;")
                print("\t\t[4] Sair.\n")
                opcao = int(input("\t\tDigite agora a opção escolhida:  "))


            elif deposito <= 0:

                print(f"\t\tDepósito não efetuado.")
                print(f"\t\tO sistema não recebe valores negativos. Tente outra vez.")
                print()
                print(f" ###################################### {bco_monetizar} ###################################### ")
                print()

                print("\t\tDigite:")
                print("\t\t[1] Sacar;")
                print("\t\t[2] Depositar;")
                print("\t\t[3] Extrato;")
                print("\t\t[4] Sair.\n")
                opcao = int(input("\t\tDigite agora a opção escolhida:  "))


            else:
                pass


        elif opcao == 3:


            print()
            print(f" ###################################### {bco_monetizar} ###################################### ")
            print()
            print("\t\tExtrato bancário para simples conferência.")

            while len(saldo) > n:

                print(f"\t\t{tipo_de_operacao[n]}   R$ {saldo[n]:.2f}  --  Saldo atualizado R$ {saldo_apos_operacao[n]:.2f}")
                n += 1

            print()
            print(f" ###################################### {bco_monetizar} ###################################### ")
            print()

            print("\t\tDigite:")
            print("\t\t[1] Sacar;")
            print("\t\t[2] Depositar;")
            print("\t\t[3] Extrato;")
            print("\t\t[4] Sair.\n")
            opcao = int(input("\t\tDigite agora a opção escolhida: "))

        elif opcao == 4:

            print()
            print(f" ###################################### {bco_monetizar} ###################################### ")
            print()
            print(f"\t\t{cliente}, volte sempre!")
            print(f"\t\tO {bco_monetizar} agradece pela confiança.")
            break

    conta_logada = False
print("\n\t\tFim do programa.")





