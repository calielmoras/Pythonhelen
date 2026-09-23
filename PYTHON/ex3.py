nomes = ["Dipirona", "Paracetamol", "Loratadina", "Ibuprofeno", "Omeprazol"]
precos = [12.50, 9.90, 18.75, 15.00, 22.30]
estoques = [20, 15, 4, 2, 10]


def listarMedicamentos():
    print("\n--- LISTA DE MEDICAMENTOS ---")
    for i in range(len(nomes)):
        print(
            f"{i + 1}. Nome: {nomes[i]} | Preço: R$ {precos[i]:.2f} | Estoque: {estoques[i]}"
        )


def buscarIndiceMedicamento(nome_busca):
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_busca.lower():
            return i
    return -1


def pesquisarMedicamento():
    print("\n--- PESQUISAR MEDICAMENTO ---")
    nome = input("Digite o nome do medicamento: ").strip()
    indice = buscarIndiceMedicamento(nome)

    if indice != -1:
        print(
            f"Encontrado! Nome: {nomes[indice]} | Preço: R$ {precos[indice]:.2f} | Estoque: {estoques[indice]}"
        )
    else:
        print("Erro: Medicamento não encontrado no sistema.")


def registrarVenda():
    print("\n--- REGISTRAR VENDA ---")
    nome = input("Digite o nome do medicamento vendido: ").strip()
    indice = buscarIndiceMedicamento(nome)

    if indice == -1:
        print("Erro: Medicamento não encontrado no sistema.")
        return

    try:
        qtd = int(input("Digite a quantidade vendida: "))
    except ValueError:
        print("Erro: Digite um valor numérico válido.")
        return

    if qtd <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
    elif qtd > estoques[indice]:
        print(
            f"Erro: Estoque insuficiente! Estoque atual de {nomes[indice]}: {estoques[indice]} unidades."
        )
    else:
        estoques[indice] -= qtd
        total = precos[indice] * qtd
        print(
            f"Venda realizada com sucesso! Total: R$ {total:.2f}. Novo estoque de {nomes[indice]}: {estoques[indice]}"
        )


def reporEstoque():
    print("\n--- REPOR ESTOQUE ---")
    nome = input("Digite o nome do medicamento para reposição: ").strip()
    indice = buscarIndiceMedicamento(nome)

    if indice == -1:
        print("Erro: Medicamento não encontrado no sistema.")
        return

    try:
        qtd = int(input("Digite a quantidade a ser adicionada: "))
    except ValueError:
        print("Erro: Digite um valor numérico válido.")
        return

    if qtd <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
    else:
        estoques[indice] += qtd
        print(
            f"Reposição realizada com sucesso! Novo estoque de {nomes[indice]}: {estoques[indice]}"
        )


def verificarEstoqueBaixo():
    print("\n--- MEDICAMENTOS COM ESTOQUE BAIXO (< 5) ---")
    encontrou = False
    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(f"- {nomes[i]}: {estoques[i]} unidade(s) [Estoque Baixo]")
            encontrou = True

    if not encontrou:
        print("Nenhum medicamento com estoque baixo no momento.")


def menu():
    while True:
        print("      SISTEMA DA FARMÁCIA     ")
        print("1 - Listar medicamentos")
        print("2 - Pesquisar medicamento")
        print("3 - Registrar venda")
        print("4 - Repor estoque")
        print("5 - Mostrar estoque baixo")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            listarMedicamentos()
        elif opcao == "2":
            pesquisarMedicamento()
        elif opcao == "3":
            registrarVenda()
        elif opcao == "4":
            reporEstoque()
        elif opcao == "5":
            verificarEstoqueBaixo()
        elif opcao == "6":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número de 1 a 6.")


menu()