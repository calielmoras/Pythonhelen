jogadores = []
gols = []

print("--- CADASTRO DOS JOGADORES ---")
for i in range(5):
    nome = input(f"Digite o nome do jogador {i+1}: ")
    qtd_gols = int(input(f"Digite a quantidade de gols de {nome}: "))
    jogadores.append(nome)
    gols.append(qtd_gols)
print("\n")

def calcularTotalGols(gols_lista):
    total = 0
    for gol in gols_lista:
        total += gol
    return total

def calcularMediaGols(gols_lista):
    total = calcularTotalGols(gols_lista)
    media = total / len(gols_lista)
    return media

def encontrarArtilheiros(jogadores_lista, gols_lista):
    maior_gol = max(gols_lista)
    artilheiros = []
    
    for i in range(len(jogadores_lista)):
        if gols_lista[i] == maior_gol:
            artilheiros.append(jogadores_lista[i])
            
    return artilheiros, maior_gol

def mostrarRelatorio(jogadores_lista, gols_lista):
    print("--- Rsultado ---")
    
    for i in range(len(jogadores_lista)):
        print(f"Jogador: {jogadores_lista[i]} - Gols: {gols_lista[i]}")
    
    print("-" * 31)
    
    total = calcularTotalGols(gols_lista)
    media = calcularMediaGols(gols_lista)
    print(f"Total de gols do time: {total}")
    print(f"Média de gols por jogador: {media:.2f}")
    
    print("-" * 31)
    
    print("Jogadores com gols acima da média:")
    for i in range(len(jogadores_lista)):
        if gols_lista[i] > media:
            print(f"- {jogadores_lista[i]} ({gols_lista[i]} gols)")
            
    print("-" * 31)
    
    artilheiros, maior_gol = encontrarArtilheiros(jogadores_lista, gols_lista)
    
    if len(artilheiros) > 1:
        print(f"Houve EMPATE na artilharia com {maior_gol} gols cada!")
        print("Artilheiros:", ", ".join(artilheiros))
    else:
        print(f"Artilheiro: {artilheiros[0]} com {maior_gol} gols!")

mostrarRelatorio(jogadores, gols)