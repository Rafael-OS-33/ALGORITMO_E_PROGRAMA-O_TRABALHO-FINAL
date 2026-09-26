# ==========================================
# FUNÇÕES
# ==========================================

def mostrar_cardapio():
    print("\n===== CARDÁPIO =====")
    print("Qual o seu pedido?")
    print("1 - Macarrão Carbonara - R$ 39,99")
    print("2 - Pizza - R$ 69,99")
    print("3 - Lasanha - R$ 49,99")
    print("4 - Gelato - R$ 29,99")
    print("5 - Bistecca alla Fiorentina - R$ 89,99")
    print("6 - Bebidas gaseificadas - R$ 9,99")


def mostrar_comanda(nome_cliente, qtd_carbonara, qtd_pizza, qtd_lasanha,
                    qtd_gelato, qtd_bistecca, qtd_bebida, total_compra):

    print("\n===== REVISÃO DO PEDIDO =====")
    print("Cliente:", nome_cliente)

    if qtd_carbonara > 0:
        print("\nMacarrão Carbonara")
        print("Quantidade:", qtd_carbonara)
        print("Valor unitário: R$ 39.99")
        print("Total: R$", qtd_carbonara * 39.99)

    if qtd_pizza > 0:
        print("\nPizza")
        print("Quantidade:", qtd_pizza)
        print("Valor unitário: R$ 69.99")
        print("Total: R$", qtd_pizza * 69.99)

    if qtd_lasanha > 0:
        print("\nLasanha")
        print("Quantidade:", qtd_lasanha)
        print("Valor unitário: R$ 49.99")
        print("Total: R$", qtd_lasanha * 49.99)

    if qtd_gelato > 0:
        print("\nGelato")
        print("Quantidade:", qtd_gelato)
        print("Valor unitário: R$ 29.99")
        print("Total: R$", qtd_gelato * 29.99)

    if qtd_bistecca > 0:
        print("\nBistecca alla Fiorentina")
        print("Quantidade:", qtd_bistecca)
        print("Valor unitário: R$ 89.99")
        print("Total: R$", qtd_bistecca * 89.99)

    if qtd_bebida > 0:
        print("\nBebidas gaseificadas")
        print("Quantidade:", qtd_bebida)
        print("Valor unitário: R$ 9.99")
        print("Total: R$", qtd_bebida * 9.99)

    print("\nTotal da compra: R$", total_compra)


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
# VALORES INICIAIS
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

    # FASE 1 - ADICIONAR PRODUTOS
    if fase == 1:

        mostrar_cardapio()

        codigo_produto = int(input("\nDigite o código do produto desejado: "))


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
            print("Código de produto inválido.")


        if codigo_produto >= 1 and codigo_produto <= 6:

            print("Produto escolhido:", produto)
            print("Preço unitário: R$", preco)

            quantidade = int(input("Digite a quantidade desejada: "))


            if quantidade > 0:

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


                subtotal = preco * quantidade

                total_compra = total_compra + subtotal

                print("\nProduto adicionado com sucesso.")
                print("Quantidade:", quantidade)
                print("Subtotal: R$", subtotal)
                print("Total da comanda: R$", total_compra)

            else:
                print("Quantidade inválida.")


        print("\nDeseja escolher mais algum produto?")
        print("1 - Adicionar mais produtos")
        print("2 - Finalizar pedido")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            fase = 1

        elif opcao == 2:
            fase = 2

        else:
            print("Opção inválida.")
            fase = 1


    # ==========================================
    # FASE 2 - REVISÃO DO PEDIDO
    # ==========================================

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

        confirmacao = int(input("Digite a opção desejada: "))


        # CONFIRMAR
        if confirmacao == 1:
            fase = 3


        # REVISAR
        elif confirmacao == 2:

            print("\n===== REVISAR PEDIDO =====")
            print("1 - Adicionar produto")
            print("2 - Remover produto")
            print("3 - Voltar para finalização")

            opcao_revisao = int(input("Digite a opção desejada: "))


            # ADICIONAR OUTRO PRODUTO
            if opcao_revisao == 1:
                fase = 1


            # REMOVER PRODUTO
            elif opcao_revisao == 2:

                print("\n===== REMOVER PRODUTO =====")
                print("1 - Macarrão Carbonara")
                print("2 - Pizza")
                print("3 - Lasanha")
                print("4 - Gelato")
                print("5 - Bistecca alla Fiorentina")
                print("6 - Bebidas gaseificadas")

                produto_remover = int(input("Digite o código do produto: "))
                quantidade_remover = int(input("Digite a quantidade que deseja remover: "))


                if produto_remover == 1:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_carbonara:
                        qtd_carbonara = qtd_carbonara - quantidade_remover
                        total_compra = total_compra - (39.99 * quantidade_remover)
                        print("Produto removido com sucesso.")

                    else:
                        print("Quantidade inválida.")


                elif produto_remover == 2:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_pizza:
                        qtd_pizza = qtd_pizza - quantidade_remover
                        total_compra = total_compra - (69.99 * quantidade_remover)
                        print("Produto removido com sucesso.")

                    else:
                        print("Quantidade inválida.")


                elif produto_remover == 3:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_lasanha:
                        qtd_lasanha = qtd_lasanha - quantidade_remover
                        total_compra = total_compra - (49.99 * quantidade_remover)
                        print("Produto removido com sucesso.")

                    else:
                        print("Quantidade inválida.")


                elif produto_remover == 4:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_gelato:
                        qtd_gelato = qtd_gelato - quantidade_remover
                        total_compra = total_compra - (29.99 * quantidade_remover)
                        print("Produto removido com sucesso.")

                    else:
                        print("Quantidade inválida.")


                elif produto_remover == 5:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_bistecca:
                        qtd_bistecca = qtd_bistecca - quantidade_remover
                        total_compra = total_compra - (89.99 * quantidade_remover)
                        print("Produto removido com sucesso.")

                    else:
                        print("Quantidade inválida.")


                elif produto_remover == 6:

                    if quantidade_remover > 0 and quantidade_remover <= qtd_bebida:
                        qtd_bebida = qtd_bebida - quantidade_remover
                        total_compra = total_compra - (9.99 * quantidade_remover)
                        print("Produto removido com sucesso.")

                    else:
                        print("Quantidade inválida.")


                else:
                    print("Código de produto inválido.")

                fase = 2


            # VOLTAR PARA A FINALIZAÇÃO
            elif opcao_revisao == 3:
                fase = 2

            else:
                print("Opção inválida.")
                fase = 2


        else:
            print("Opção inválida.")
            fase = 2


# ==========================================
# DESCONTO
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

    opcao_pagamento = int(input("Digite a forma de pagamento: "))


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
        print("Forma de pagamento inválida.")


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
    print("Valor unitário: R$ 39.99")
    print("Total: R$", qtd_carbonara * 39.99)


if qtd_pizza > 0:
    print("\nPizza")
    print("Quantidade:", qtd_pizza)
    print("Valor unitário: R$ 69.99")
    print("Total: R$", qtd_pizza * 69.99)


if qtd_lasanha > 0:
    print("\nLasanha")
    print("Quantidade:", qtd_lasanha)
    print("Valor unitário: R$ 49.99")
    print("Total: R$", qtd_lasanha * 49.99)


if qtd_gelato > 0:
    print("\nGelato")
    print("Quantidade:", qtd_gelato)
    print("Valor unitário: R$ 29.99")
    print("Total: R$", qtd_gelato * 29.99)


if qtd_bistecca > 0:
    print("\nBistecca alla Fiorentina")
    print("Quantidade:", qtd_bistecca)
    print("Valor unitário: R$ 89.99")
    print("Total: R$", qtd_bistecca * 89.99)


if qtd_bebida > 0:
    print("\nBebidas gaseificadas")
    print("Quantidade:", qtd_bebida)
    print("Valor unitário: R$ 9.99")
    print("Total: R$", qtd_bebida * 9.99)


print("\n--------------------------------")
print("Valor original: R$", total_compra)
print("Percentual de desconto:", percentual_desconto * 100, "%")
print("Valor do desconto: R$", valor_desconto)
print("Valor final: R$", valor_final)
print("Forma de pagamento:", forma_pagamento)
print("--------------------------------")

print("\nPedido finalizado. Obrigado,", nome_cliente)