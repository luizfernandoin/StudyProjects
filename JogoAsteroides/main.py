#Importa as bibliotecas necessárias
import pygame
import random
from nave import Nave
from meteoro import Meteoro
from tiro import Tiro

#Largura e altura da tela
LARGURA = 700
ALTURA = 680

# Início, janela e variáveis
pygame.init()
pygame.font.init()

#Sons utilizados no jogo
pygame.mixer.music.load('songs\\musica_de_fundo.mp3')
pygame.mixer.music.play(-1)
som_colisao1 = pygame.mixer.Sound('songs\\explosao.mp3')
som_tiro = pygame.mixer.Sound('songs\\som_de_tiro.mp3')
som_ponto = pygame.mixer.Sound('songs\\som_ponto.mp3')

#Pontuação Inicial do jogador
pontuacao_inicial = 0

#Função com as informações dos textos
def exibir_mensagem(mensagem, tamanho, cor):
    font = pygame.font.SysFont("SHOWCARD GOTHIC", tamanho, False, False)
    mensagem1 = f'{mensagem}'
    text = font.render(mensagem1, True, cor)
    return text

#Função para quando, e se, o jogo for resetado
def restart_game():
    global pontuacao_inicial, colidiu, timer, GameOver
    pontuacao_inicial = 0
    timer = 0
    nave.rect.center = [LARGURA // 2, 630]
    colidiu = False
    GameOver = False
    pygame.mixer.music.play(-1)

#Tela e nome do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Space Fall')

#Função para auxílio no desempenho das colisões
colidiu = False

#Grupos que armazenam as sprites
groupOBJ = pygame.sprite.Group()
groupmeteoro = pygame.sprite.Group()
grouptiro = pygame.sprite.Group()

#Fundo/Cenário
fundo = pygame.sprite.Sprite(groupOBJ)
fundo.image = pygame.image.load('images\\espaço.png')
fundo.image = pygame.transform.scale(fundo.image, [700, 680])
fundo.rect = fundo.image.get_rect()

#Nave/Player
nave = Nave(groupOBJ)
nave.rect.center = [LARGURA // 2, 630]

#Eventos
running = True
GameOver = False
timer = 20
clock = pygame.time.Clock()

if __name__ == "__main__":
    while running:

        clock.tick(70)
        pygame.time.delay(100)

        #Eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not GameOver:
                    som_tiro.play()
                    tiro = Tiro(groupOBJ, grouptiro)
                    tiro.rect.center = nave.rect.center

                if event.key == pygame.K_r and colidiu == True:
                    restart_game()

#Desenhos na tela e colisões
        if not GameOver:
            tela.fill([50, 50, 50])
            groupOBJ.draw(tela)

            colisao1 = pygame.sprite.spritecollide(nave, groupmeteoro, True, pygame.sprite.collide_mask)
            colisao2 = pygame.sprite.groupcollide(grouptiro, groupmeteoro, True, True, pygame.sprite.collide_mask)

            if colisao1 and colidiu == False:
                pygame.mixer.music.stop()
                som_colisao1.play()
                gameover = exibir_mensagem("GAME OVER", 50, (255, 255, 255))
                frase = exibir_mensagem("Sua Pontuação:", 40, (255, 0, 0))
                pontos = exibir_mensagem(pontuacao_inicial, 45, (0, 255, 0))
                restart = exibir_mensagem("Clique em 'R' para reiniciar", 20, (255, 255, 255))
                tela.blit(gameover, (200, 200))
                tela.blit(frase, (190, 250))
                tela.blit(pontos, (LARGURA // 2, 300))
                tela.blit(restart, (210, 350))
                colidiu = True
                GameOver = True

            if colisao2 and colidiu == False:
                pontuacao_inicial += 1
                som_ponto.play()
                pontos = exibir_mensagem(pontuacao_inicial, 40, (255, 0, 0))
                tela.blit(pontos, (50, 50))

            if colidiu:
                pass

            else:
                groupOBJ.update()#Faz a atualização dos objetos do grupo citado

                #Faz com que os meteoros apareçam de forma aleatória na tela
                timer += 2
                if timer > 17:
                    timer = 0
                    if random.random() > 0.2:
                        meteoro = Meteoro(groupOBJ, groupmeteoro)

        #Atualiza o jogo
        pygame.display.update()
    pygame.quit()