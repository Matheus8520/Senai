import random

def atividade1():
    al = random.randint(5,10)
    return al

def atividade2():
    al1 = random.randint(1,10)
    al2 = random.randint(2,10)
    al3 = random.randint(3,10)
    print(al1, al2, al3)

def atividade3():
    al  = random.randrange(10,30)
    print(al)


def atividade4():
    for i in range(10,0,-1):
        print(i)
        input("Pressione enter para continuar...")
        print("Fogo")
atividade4()

def atividade5():
    num=int(input("Digite um Numero inteiro: "))
    print(f'tabuada de mult de{num}:')
    for i in range(1,11):
        print(f"{num} x {i}={num * i }")
atividade5()       

def atividade6():
    for i in range(99,1,-2):
        print(i)
atividade6()        


# # MANIPULAÇÃO DE EVENTOS 
# # JOGO PONG


# import pygame


# pygame.init()


# janela = pygame.display.set_mode([500, 500])
# pygame.display.set_caption('Ping Pong')


# BRANCO = (255, 255, 255)
# PRETO = (0, 0, 0)

# raquete1_x, raquete1_y = 50, 225
# raquete2_x, raquete2_y = 450, 225
# bola_x, bola_y = 250, 250


# velocidade_raquete = 5
# velocidade_bola_x, velocidade_bola_y = 1 , 1


# raquete_largura, raquete_altura = 20, 100
# bola_largura, bola_altura = 20, 20


# placar1 = 0
# placar2 = 0
# font = pygame.font.SysFont(None, 55)

# # Função para desenhar elementos
# def desenhar():
#     # Limpa a tela
#     janela.fill(BRANCO)
    
    
#     pygame.draw.rect(janela, PRETO, (raquete1_x, raquete1_y, raquete_largura, raquete_altura))
#     pygame.draw.rect(janela, PRETO, (raquete2_x, raquete2_y, raquete_largura, raquete_altura))
#     pygame.draw.ellipse(janela, PRETO, (bola_x, bola_y, bola_largura, bola_altura))
    

#     placar_texto = font.render(f'{placar1} - {placar2}', True, PRETO)
#     janela.blit(placar_texto, (200, 20))


# LOOP = True

# while LOOP:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             LOOP = False

#     # Movimentação das raquetes
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w] and raquete1_y > 0:
#         raquete1_y -= velocidade_raquete
#     if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
#         raquete1_y += velocidade_raquete
#     if keys[pygame.K_UP] and raquete2_y > 0:
#         raquete2_y -= velocidade_raquete
#     if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
#         raquete2_y += velocidade_raquete

 
#     bola_x += velocidade_bola_x
#     bola_y += velocidade_bola_y

#     if bola_y <= 0 or bola_y >= 500 - bola_altura:
#         velocidade_bola_y = -velocidade_bola_y

   
#     if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y + raquete_altura):
#         velocidade_bola_x = -velocidade_bola_x
#     if (raquete2_x < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y + raquete_altura):
#         velocidade_bola_x = -velocidade_bola_x

 
#     if bola_x <= 0:  
#         placar2 += 1
#         bola_x, bola_y = 250, 250 
#         velocidade_bola_x = -velocidade_bola_x  
#     if bola_x >= 500 - bola_largura:  
#         placar1 += 1
#         bola_x, bola_y = 250, 250  
#         velocidade_bola_x = -velocidade_bola_x  

   
#     desenhar()

  
#     pygame.display.update()


# pygame.quit()

# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/





# largura, altura = 400, 400
# tela = pygame.display.set_mode((largura, altura))
# pygame.display.set_caption("Labirinto")


# preto = (176,196,222)
# branco = (0,255,255)
# vermelho = (128,0,128)


# tamanho_celula = 40
# labirinto = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]


# x, y = 1 * tamanho_celula, 1 * tamanho_celula
# velocidade = 40

# def desenhar_labirinto():
#     for linha in range(len(labirinto)):
#         for coluna in range(len(labirinto[linha])):
#             cor = preto if labirinto[linha][coluna] == 1 else branco
#             pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))


# executando = True
# while executando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             executando = False


#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_LEFT]:
#         novo_x = x - velocidade
#         if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
#             x = novo_x
#     if teclas[pygame.K_RIGHT]:
#         novo_x = x + velocidade
#         if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
#             x = novo_x
#     if teclas[pygame.K_UP]:
#         novo_y = y - velocidade
#         if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
#             y = novo_y
#     if teclas[pygame.K_DOWN]:
#         novo_y = y + velocidade
#         if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
#             y = novo_y


#     tela.fill(branco)

    
#     desenhar_labirinto()
#     pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))


#     pygame.display.flip()


#     pygame.time.Clock().tick(10)


# pygame.quit()
