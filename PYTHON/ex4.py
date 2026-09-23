colunas = ["A", "B", "C", "D", "E", "F"]

assentos = [
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
]

categorias_vendidas = []
valores_vendidos = []


def calcularPreco(fileira):
    if fileira == 1:
        return "Executiva", 850.00
    elif fileira == 2 or fileira == 3:
        return "Espaço extra", 600.00
    else:
        return "Econômica", 400.00


def validarAssento(codigo):
    numero = codigo[:-1]
    letra = codigo[-1]

    if not numero.isdigit():
        return None, None

    fileira = int(numero)
    if fileira < 1 or fileira > 5:
        return None, None
    if letra not in colunas:
        return None, None

    linha = fileira - 1
    coluna = colunas.index(letra)
    return linha, coluna


def verificarDisponibilidade(linha, coluna):
    return assentos[linha][coluna] == "L"


def mostrarAssentos():
    for linha in assentos:
        print(linha)


def comprarAssento():
    codigo = input("Assento desejado (ex: 2C): ").upper()
    linha, coluna = validarAssento(codigo)

    if linha is None:
        print("Assento inválido.")
        return

    if not verificarDisponibilidade(linha, coluna):
        print("O assento", codigo, "já está ocupado.")
        return

    categoria, preco = calcularPreco(linha + 1)
    print("Categoria:", categoria)
    print("Valor: R$", preco)

    confirmar = input("Confirmar compra? (S/N): ").upper()
    if confirmar != "S":
        print("Compra cancelada.")
        return

    assentos[linha][coluna] = "O"
    categorias_vendidas.append(categoria)
    valores_vendidos.append(preco)
    print("Compra realizada com sucesso.")
    print("O assento", codigo, "agora está indisponível.")


def mostrarResumo():
    livres = 0
    ocupados = 0
    for linha in assentos:
        for assento in linha:
            if assento == "L":
                livres += 1
            else:
                ocupados += 1

    faturamento = 0
    for valor in valores_vendidos:
        faturamento += valor

    executiva = 0
    espaco_extra = 0
    economica = 0
    for categoria in categorias_vendidas:
        if categoria == "Executiva":
            executiva += 1
        elif categoria == "Espaço extra":
            espaco_extra += 1
        else:
            economica += 1

    print("Assentos livres:", livres)
    print("Assentos ocupados:", ocupados)
    print("Percentual de ocupação:", (ocupados / 30) * 100, "%")
    print("Faturamento total: R$", faturamento)
    print("Vendas por categoria:")
    print("Executiva:", executiva)
    print("Espaço extra:", espaco_extra)
    print("Econômica:", economica)


while True:
    print("\n1 - Visualizar assentos")
    print("2 - Comprar assento")
    print("3 - Consultar assento")
    print("4 - Mostrar resumo do voo")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrarAssentos()
    elif opcao == "2":
        comprarAssento()
    elif opcao == "3":
        codigo = input("Assento a consultar (ex: 2C): ").upper()
        linha, coluna = validarAssento(codigo)
        if linha is None:
            print("Assento inválido.")
        else:
            categoria, preco = calcularPreco(linha + 1)
            if verificarDisponibilidade(linha, coluna):
                situacao = "livre"
            else:
                situacao = "ocupado"
            print("Assento", codigo, "-", situacao, "- Categoria:", categoria)
    elif opcao == "4":
        mostrarResumo()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")