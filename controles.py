config = open("config/config.cfg").read()
linha = ""
linhas = []

for i in config:
    if not(i == "\n"):
        linha = linha+i
    else:
        linhas.append(linha)
        linha = ""
linhas.append(linha)

P1Cima = int(linhas[0])
P1Baixo = int(linhas[1])
P1Direita = int(linhas[2])
P1Esquerda = int(linhas[3])
P1SocoFraco = int(linhas[4])
P1SocoForte = int(linhas[5])
P1ChuteBaixo = int(linhas[6])
P1ChuteAlto = int(linhas[7])

P2Cima = int(linhas[8])
P2Baixo = int(linhas[9])
P2Direita = int(linhas[10])
P2Esquerda = int(linhas[11])
P2SocoFraco = int(linhas[12])
P2SocoForte = int(linhas[13])
P2ChuteBaixo = int(linhas[14])
P2ChuteAlto = int(linhas[15])