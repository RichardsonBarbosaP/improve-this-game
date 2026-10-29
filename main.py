import pygame
import sys
from objects.heroi import Heroi
from objects.vilao import Vilao
from interface import botao_de_atacar

# Definindo função principal (main) do jogo:
def main():
    print("> Iniciando... 🔁")
    pygame.init()
    print("> Criando a tela... 🖥️")
    screen = pygame.display.set_mode((600, 480))
    print("> Executando... 🚀")
    pygame.display.set_caption("Star Boy vs Supernova")
    fonte = pygame.font.SysFont('Arial', 24)
    clock = pygame.time.Clock()

    # Atributos dos personagens (Nome, Vida, Ataque, Defesa):
    heroi = Heroi('Star Boy', 850, 100, 60)
    vilao = Vilao('Supernova', 3000, 200, 60)

    # Imprime os atributos dos personagens no Terminal:
    print("             Personagens:")
    print(heroi)
    print(vilao)

    turnos = 0
    jogo_encerrado = False  # Variável para controlar o estado do jogo

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("> Fechando... ❌")
                running = False

            # Cliques na tela só são válidos se o jogo não acabou e o vilão não está atacando (no estado "parado")
            if event.type == pygame.MOUSEBUTTONDOWN and not jogo_encerrado and vilao.estado == "parado":

                if botao_de_atacar.collidepoint(event.pos):
                    turnos += 1 # aumenta quantidade de turnos
                    print(f'            -- Turno {turnos}: --')
                    heroi.golpe(vilao)
                    if vilao.vida <= 0:
                        print(f'{vilao.nome} foi derrotado por {heroi.nome}!\nVocê venceu o combate! Parabéns!')
                        jogo_encerrado = True
                    else:
                        vilao.iniciar_ataque()

            # Apertar ESPAÇO = Parry (defende, mas só funciona dentro da janela de quadros do vilão)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jogo_encerrado:
                vilao.tentar_parry()

        # Uma vez por frame: atualiza o ataque do vilão (sem travar a janela)
        if not jogo_encerrado:
            resultado = vilao.atualizar(heroi)
            if resultado:
                print(resultado)
                if heroi.vida <= 0: # Caso o HP do herói chegue a 0, o jogo acaba
                    print(f'{heroi.nome} foi derrotado por {vilao.nome}...\nVocê perdeu o combate! Mais sorte na próxima vez!')
                    jogo_encerrado = True

        # Tela preta (infelizmente)
        screen.fill((0, 0, 0))

        # Vida dos personagens mostradas em texto
        texto_heroi = fonte.render(f'{heroi.nome}: {heroi.vida}', True, (255, 255, 255))
        texto_vilao = fonte.render(f'{vilao.nome}: {vilao.vida}', True, (255, 255, 255))
        screen.blit(texto_heroi, (20, 20))
        screen.blit(texto_vilao, (20, 55))

        if not jogo_encerrado:
            pygame.draw.rect(screen, (150, 0, 0), botao_de_atacar)
            texto_botao = fonte.render("Ataque", True, (255, 255, 255))
            screen.blit(texto_botao, (botao_de_atacar.x + 60, botao_de_atacar.y + 12))

            # Avisos do ataque do vilão na tela
            if vilao.estado == "preparando":
                aviso = fonte.render(f'Cuidado! {vilao.nome} está preparando um ataque...', True, (255, 255, 0))
                screen.blit(aviso, (120, 300))
            elif vilao.estado == "janela":
                aviso = fonte.render('APERTE ESPAÇO!', True, (255, 80, 80))
                screen.blit(aviso, (210, 300))
        else:
            texto_fim = fonte.render("COMBATE ENCERRADO!", True, (255, 0, 0))
            screen.blit(texto_fim, (170, 400))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()