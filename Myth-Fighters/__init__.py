import pygame

telaLargura = 800
telaAltura = 600
estado = 0

try:
    pygame.init()
except:
    print("O modulo pygame não foi iniciado com sucesso")

tela = pygame.display.set_mode((telaLargura, telaAltura), pygame.DOUBLEBUF, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            estado = 9
    if estado == 0:
        #estado = Abertura()
        pass
    elif estado == 1:
        #estado = Menu()
        pass
    elif estado == 2:
        #estado = Configuração()
        pass
    elif estado == 3:
        #estado = Credito()
        pass
    elif estado == 4:
        #estado = SelecionarPersonagem()
        pass
    elif estado == 5:
        #estado = SelecionarFase()
        pass
    elif estado == 6:
        #estado = Luta()
        pass
    elif estado == 7:
        #estado = FimLuta()
        pass
    elif estado == 8:
        #estado = Pause()
        pass
    elif estado == 9:
        #Sair
        break


pygame.quit()
exit()
