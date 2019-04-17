import pygame

try:
    pygame.init()
except:
    print("O modulo pygame não foi iniciado com sucesso")

estado = 0

while True:
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
    elif estado == 9:
        #Sair
        break


pygame.quit()
exit()
