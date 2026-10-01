# ==========================================
# SISTEMA DE ATENDIMENTO E PEDIDOS
# ==========================================


# Função responsável por mostrar o cardápio
def mostrar_cardapio():
    print("\n===== CARDÁPIO =====")
    print("Qual o seu pedido?")
    print("1 - Macarrão Carbonara - R$ 39,99")
    print("2 - Pizza - R$ 69,99")
    print("3 - Lasanha - R$ 49,99")
    print("4 - Gelato - R$ 29,99")
    print("5 - Bistecca alla Fiorentina - R$ 89,99")
    print("6 - Bebidas gaseificadas - R$ 9,99")


# Função responsável por mostrar a comanda
def mostrar_comanda(nome_cliente, qtd_carbonara, qtd_pizza, qtd_lasanha,
                    qtd_gelato, qtd_bistecca, qtd_bebida, total_compra):

    print("\n===== REVISÃO DO PEDIDO =====")
    print("Cliente:", nome_cliente)

    if qtd_carbonara > 0:
        print("\nMacarrão Carbonara")
        print("Quantidade:", qtd_carbonara)
        print("Valor unitário: R$ 39,99")
        print("Total: R$", round(qtd_carbonara * 39.99, 2))

    if qtd_pizza > 0:
        print("\nPizza")
        print("Quantidade:", qtd_pizza)
        print("Valor unitário: R$ 69,99")
        print("Total: R$", round(qtd_pizza * 69.99, 2))

    if qtd_lasanha > 0:
        print("\nLasanha")
        print("Quantidade:", qtd_lasanha)
        print("Valor unitário: R$ 49,99")
        print("Total: R$", round(qtd_lasanha * 49.99, 2))

    if qtd_gelato > 0:
        print("\nGelato")
        print("Quantidade:", qtd_gelato)
        print("Valor unitário: R$ 29,99")
        print("Total: R$", round(qtd_gelato * 29.99, 2))

    if qtd_bistecca > 0:
        print("\nBistecca alla Fiorentina")
        print("Quantidade:", qtd_bistecca)
        print("Valor unitário: R$ 89,99")
        print("Total: R$", round(qtd_bistecca * 89.99, 2))

    if qtd_bebida > 0:
        print("\nBebidas gaseificadas")
        print("Quantidade:", qtd_bebida)
        print("Valor unitário: R$ 9,99")
        print("Total: R$", round(qtd_bebida * 9.99, 2))

    print("\nTotal da compra: R$", round(total_compra, 2))


# Função responsável por calcular o desconto
def calcular_desconto(total_compra):

    if total_compra < 50:
        percentual_desconto = 0

    elif total_compra < 100:
        percentual_desconto = 0.05

    else:
        percentual_desconto = 0.10

    return percentual_desconto


# ==========================================
# INÍCIO DO PROGRAMA
# ==========================================

print("===== INICIAR =====")

nome_cliente = input("Digite o nome do cliente: ")

print("Olá,", nome_cliente)


# ==========================================
# VARIÁVEIS INICIAIS
# ==========================================

total_compra = 0

qtd_carbonara = 0
qtd_pizza = 0
qtd_lasanha = 0
qtd_gelato = 0
qtd_bistecca = 0
qtd_bebida = 0

fase = 1


# ==========================================
# PEDIDO E REVISÃO
# ==========================================

while fase != 3:

    # ======================================
    # FASE 1 - ADICIONAR PRODUTOS
    # ======================================

    if fase == 1:

        mostrar_cardapio()

        codigo_produto = int(
            input("\nDigite o código do produto desejado: ")
        )


        # Identificação do produto
        if codigo_produto == 1:
            produto = "Macarrão Carbonara"
            preco = 39.99

        elif codigo_produto == 2:
            produto = "Pizza"
            preco = 69.99

        elif codigo_produto == 3:
            produto = "Lasanha"
            preco = 49.99

        elif codigo_produto == 4:
            produto = "Gelato"
            preco = 29.99

        elif codigo_produto == 5:
            produto = "Bistecca alla Fiorentina"
            preco = 89.99

        elif codigo_produto == 6:
            produto = "Bebidas gaseificadas"
            preco = 9.99

        else:
            print("\nCódigo de produto inválido.")


        # Só continua se o código for válido
        if codigo_produto >= 1 and codigo_produto <= 6:

            print("\nProduto escolhido:", produto)
            print("Preço unitário: R$", preco)

            quantidade = int(
                input("Digite a quantidade desejada: ")
            )


            # Validação da quantidade
            if quantidade > 0:

                # Guarda a quantidade de cada produto
                if codigo_produto == 1:
                    qtd_carbonara = qtd_carbonara + quantidade

                elif codigo_produto == 2:
                    qtd_pizza = qtd_pizza + quantidade

                elif codigo_produto == 3:
                    qtd_lasanha = qtd_lasanha + quantidade

                elif codigo_produto == 4:
                    qtd_gelato = qtd_gelato + quantidade

                elif codigo_produto == 5:
                    qtd_bistecca = qtd_bistecca + quantidade

                elif codigo_produto == 6:
                    qtd_bebida = qtd_bebida + quantidade


                # Cálculo do subtotal
                subtotal = preco * quantidade

                # Acumula o valor da compra
                total_compra = total_compra + subtotal

                print("\nProduto adicionado com sucesso.")
                print("Quantidade:", quantidade)
                print("Subtotal: R$", round(subtotal, 2))
                print(
                    "Total da comanda: R$",
                    round(total_compra, 2)
                )

            else:
                print("\nQuantidade inválida.")


        # Só pergunta sobre finalização se houver
        # algum produto na comanda
        if total_compra > 0:

            print("\nDeseja escolher mais algum produto?")
            print("1 - Adicionar mais produtos")
            print("2 - Finalizar pedido")

            opcao = int(
                input("Digite a opção desejada: ")
            )

            if opcao == 1:
                fase = 1

            elif opcao == 2:
                fase = 2

            else:
                print("\nOpção inválida.")
                fase = 1


    # ======================================
    # FASE 2 - REVISÃO
    # ======================================

    elif fase == 2:

        mostrar_comanda(
            nome_cliente,
            qtd_carbonara,
            qtd_pizza,
            qtd_lasanha,
            qtd_gelato,
            qtd_bistecca,
            qtd_bebida,
            total_compra
        )


        print("\nO que deseja fazer?")
        print("1 - Confirmar pedido")
        print("2 - Revisar pedido")

        confirmacao = int(
            input("Digite a opção desejada: ")
        )


        # CONFIRMAR O PEDIDO
        if confirmacao == 1:
            fase = 3


        # REVISAR O PEDIDO
        elif confirmacao == 2:

            print("\n===== REVISAR PEDIDO =====")
            print("1 - Adicionar produto")
            print("2 - Remover produto")
            print("3 - Voltar para finalização")

            opcao_revisao = int(
                input("Digite a opção desejada: ")
            )


            # Adicionar outro produto
            if opcao_revisao == 1:
                fase = 1


            # Remover produto
            elif opcao_revisao == 2:

                print("\n===== REMOVER PRODUTO =====")
                print("1 - Macarrão Carbonara")
                print("2 - Pizza")
                print("3 - Lasanha")
                print("4 - Gelato")
                print("5 - Bistecca alla Fiorentina")
                print("6 - Bebidas gaseificadas")

                produto_remover = int(
                    input("Digite o código do produto: ")
                )

                quantidade_remover = int(
                    input("Digite a quantidade que deseja remover: ")
                )


                # Carbonara
                if produto_remover == 1:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_carbonara:

                        qtd_carbonara = qtd_carbonara - quantidade_remover

                        total_compra = total_compra - (
                            39.99 * quantidade_remover
                        )

                        print("\nProduto removido com sucesso.")

                    else:
                        print("\nQuantidade inválida.")


                # Pizza
                elif produto_remover == 2:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_pizza:

                        qtd_pizza = qtd_pizza - quantidade_remover

                        total_compra = total_compra - (
                            69.99 * quantidade_remover
                        )

                        print("\nProduto removido com sucesso.")

                    else:
                        print("\nQuantidade inválida.")


                # Lasanha
                elif produto_remover == 3:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_lasanha:

                        qtd_lasanha = qtd_lasanha - quantidade_remover

                        total_compra = total_compra - (
                            49.99 * quantidade_remover
                        )

                        print("\nProduto removido com sucesso.")

                    else:
                        print("\nQuantidade inválida.")


                # Gelato
                elif produto_remover == 4:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_gelato:

                        qtd_gelato = qtd_gelato - quantidade_remover

                        total_compra = total_compra - (
                            29.99 * quantidade_remover
                        )

                        print("\nProduto removido com sucesso.")

                    else:
                        print("\nQuantidade inválida.")


                # Bistecca
                elif produto_remover == 5:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_bistecca:

                        qtd_bistecca = qtd_bistecca - quantidade_remover

                        total_compra = total_compra - (
                            89.99 * quantidade_remover
                        )

                        print("\nProduto removido com sucesso.")

                    else:
                        print("\nQuantidade inválida.")


                # Bebida
                elif produto_remover == 6:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_bebida:

                        qtd_bebida = qtd_bebida - quantidade_remover

                        total_compra = total_compra - (
                            9.99 * quantidade_remover
                        )

                        print("\nProduto removido com sucesso.")

                    else:
                        print("\nQuantidade inválida.")


                else:
                    print("\nCódigo de produto inválido.")


                # Evita pequenos valores negativos
                if total_compra < 0:
                    total_compra = 0


                # Se todos os produtos forem removidos,
                # volta para o cardápio
                if total_compra == 0:

                    print("\nA comanda está vazia.")
                    print("Voltando ao cardápio.")

                    fase = 1

                else:
                    fase = 2


            # Voltar para a tela de finalização
            elif opcao_revisao == 3:
                fase = 2


            else:
                print("\nOpção inválida.")
                fase = 2


        else:
            print("\nOpção inválida.")
            fase = 2


# ==========================================
# CÁLCULO DO DESCONTO
# ==========================================

percentual_desconto = calcular_desconto(total_compra)

valor_desconto = total_compra * percentual_desconto

valor_final = total_compra - valor_desconto


# ==========================================
# FORMA DE PAGAMENTO
# ==========================================

pagamento_valido = False

while pagamento_valido == False:

    print("\n===== FORMA DE PAGAMENTO =====")
    print("1 - Dinheiro")
    print("2 - PIX")
    print("3 - Cartão")

    opcao_pagamento = int(
        input("Digite a forma de pagamento: ")
    )


    if opcao_pagamento == 1:
        forma_pagamento = "Dinheiro"
        pagamento_valido = True

    elif opcao_pagamento == 2:
        forma_pagamento = "PIX"
        pagamento_valido = True

    elif opcao_pagamento == 3:
        forma_pagamento = "Cartão"
        pagamento_valido = True

    else:
        print("\nForma de pagamento inválida.")


# ==========================================
# RECIBO FINAL
# ==========================================

print("\n================================")
print("         RECIBO FINAL")
print("================================")

print("Cliente:", nome_cliente)


if qtd_carbonara > 0:
    print("\nMacarrão Carbonara")
    print("Quantidade:", qtd_carbonara)
    print("Valor unitário: R$ 39,99")
    print(
        "Total: R$",
        round(qtd_carbonara * 39.99, 2)
    )


if qtd_pizza > 0:
    print("\nPizza")
    print("Quantidade:", qtd_pizza)
    print("Valor unitário: R$ 69,99")
    print(
        "Total: R$",
        round(qtd_pizza * 69.99, 2)
    )


if qtd_lasanha > 0:
    print("\nLasanha")
    print("Quantidade:", qtd_lasanha)
    print("Valor unitário: R$ 49,99")
    print(
        "Total: R$",
        round(qtd_lasanha * 49.99, 2)
    )


if qtd_gelato > 0:
    print("\nGelato")
    print("Quantidade:", qtd_gelato)
    print("Valor unitário: R$ 29,99")
    print(
        "Total: R$",
        round(qtd_gelato * 29.99, 2)
    )


if qtd_bistecca > 0:
    print("\nBistecca alla Fiorentina")
    print("Quantidade:", qtd_bistecca)
    print("Valor unitário: R$ 89,99")
    print(
        "Total: R$",
        round(qtd_bistecca * 89.99, 2)
    )


if qtd_bebida > 0:
    print("\nBebidas gaseificadas")
    print("Quantidade:", qtd_bebida)
    print("Valor unitário: R$ 9,99")
    print(
        "Total: R$",
        round(qtd_bebida * 9.99, 2)
    )


print("\n--------------------------------")

print(
    "Valor original: R$",
    round(total_compra, 2)
)

print(
    "Percentual de desconto:",
    percentual_desconto * 100,
    "%"
)

print(
    "Valor do desconto: R$",
    round(valor_desconto, 2)
)

print(
    "Valor final: R$",
    round(valor_final, 2)
)

print(
    "Forma de pagamento:",
    forma_pagamento
)

print("--------------------------------")

print("\nPedido finalizado. Obrigado,", nome_cliente)

