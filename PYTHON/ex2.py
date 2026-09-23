def registrarTentativas():
    tentativas = []
    print("---ARREMESOS ---")
    print("Digite: 0 Erro, 1 Ponto, 2 Pontos, 3 Pontos\n")
    
    i = 0
    while i < 10:
        entrada = int(input(f"Tentativa {i + 1}: "))
        
        if entrada in [0, 1, 2, 3]:
            tentativas.append(entrada)
            i += 1
        else:
            print("Valor inválido! Digite apenas 0, 1, 2 ou 3.")
            
    return tentativas

def calcularPontuacao(tentativas):
    total = 0
    for valor in tentativas:
        total += valor
    return total

def calcularAproveitamento(tentativas):
    convertidos = 0
    errados = 0
    
    for valor in tentativas:
        if valor > 0:
            convertidos += 1
        else:
            errados += 1
            
    percentual = (convertidos / len(tentativas)) * 100
    
    return convertidos, errados, percentual

def encontrarCestaMaisFrequente(tentativas):
    cesta1 = 0
    cesta2 = 0
    cesta3 = 0
    
    for valor in tentativas:
        if valor == 1:
            cesta1 += 1
        elif valor == 2:
            cesta2 += 1
        elif valor == 3:
            cesta3 += 1
            
    if cesta1 == 0 and cesta2 == 0 and cesta3 == 0:
        return "Nenhuma cesta foi convertida"
    elif cesta1 > cesta2 and cesta1 > cesta3:
        return f"Cesta de 1 ponto (convertida {cesta1} vezes)"
    elif cesta2 > cesta1 and cesta2 > cesta3:
        return f"Cesta de 2 pontos (convertida {cesta2} vezes)"
    elif cesta3 > cesta1 and cesta3 > cesta2:
        return f"Cesta de 3 pontos (convertida {cesta3} vezes)"
    else:
        return "Houve empate entre os tipos de cestas mais frequentes"

tentativas = registrarTentativas()

pontuacao_total = calcularPontuacao(tentativas)
convertidos, errados, percentual = calcularAproveitamento(tentativas)
cesta_frequente = encontrarCestaMaisFrequente(tentativas)

print("\n--- RELATÓRIO DE DESEMPENHO ---")
print(f"Tentativas registradas: {tentativas}")
print(f"Pontuação total: {pontuacao_total} pontos")
print(f"Arremessos convertidos: {convertidos}")
print(f"Arremessos errados: {errados}")
print(f"Aproveitamento: {percentual:.1f}%")
print(f"Tipo de cesta mais frequente: {cesta_frequente}")