import pygame

janela = pygame.display.set_mode([960, 540])

pygame.display.set_caption('CS 0.1')

imagem_fundo = pygame.image.load('C:/Users/55129/Documents/Projetos/Python_01/space bg game.png')

nave_player = pygame.image.load('C:/Users/55129/Documents/Projetos/Python_01/sprite_nave_pequena.png')

nave_inimica = pygame.image.load('C:/Users/55129/Documents/Projetos/Python_01/nave_inimiga_pequena.png')

#posicao da nave
pos_y_player = 400
pos_x_player = 420
vel_nave_player = 10

loop = True

while loop:

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            loop = False
        
        teclas = pygame.key.get_pressed()

        #se pressionar a seta pra cima, vai pra cima
        if teclas[pygame.K_UP]:
            pos_y_player -= vel_nave_player

        #se pressionar a seta pra baixo, vai pra baixo
        if teclas[pygame.K_DOWN]:
            pos_y_player += vel_nave_player

        #se pressionar a seta pro lado esquerdo, vai pra esquerda
        if teclas[pygame.K_LEFT]:
            pos_x_player -= vel_nave_player

        #se pressionar a seta pro lado direito, vai pra direita
        if teclas[pygame.K_RIGHT]:
            pos_x_player += vel_nave_player

    janela.blit(imagem_fundo, (0, 0))
    janela.blit(nave_player, (pos_x_player, pos_y_player))
    janela.blit(nave_inimica, (400, 50))
    
    pygame.display.update()