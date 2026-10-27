import pygame
import sys
from objects.heroi import Heroi
from objects.vilao import Vilao

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Placeholder")

    # Criando personagens e vilões (Nome, Vida, Ataque, Defesa, Coragem/Intimidação)
    heroi = Heroi('Star Boy', 120, 35, 30)
    vilao = Vilao('Supernova', 250, 40, 30)
    print(heroi)
    print(vilao)
    heroi.golpe(vilao)
    vilao.golpe(heroi)

    running = True # enquanto o jogo estiver rodando, o loop continua
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Preenche a tela com preto
        pygame.display.flip()  # Atualiza a tela

#def __str__(self):
    #return f'Personagem: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'

# def golpe(self, alvo):
    # """
    # Mecânica de ataque entre personagens. Calcula o dano com base no ataque do atacante e na defesa do alvo.
    # """
    # dano = self.golpe - alvo.defesa
    # dano = min(dano, 1)
    # alvo.vida -= dano
    
    # if alvo.vida < 0:  
    #     alvo.vida = 0

    # print(f'{self.nome} atacou {alvo.nome}!')
    # alvo.downgrade_vida()


    # # Melhorando a vida do herói
    # heroi.upgrade_vida(20)
    # print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

pygame.quit() # Encerra o Pygame
sys.exit() # encerrar o programa

if __name__ == "__main__":
    main()