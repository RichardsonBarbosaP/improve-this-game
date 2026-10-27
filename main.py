from personagem import Personagem
from heroi import Heroi
from vilao import Vilao

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("Jogo de Aventura")

def main():
    # Criando personagens e vilões (Nome, Vida, Ataque, Defesa, Coragem/Intimidação)
    heroi = Heroi('Star Boy', 120, 35, 30)
    npc = Personagem('Cone Guy', 100, 20, 20)
    vilao = Vilao('Supernova', 250, 40, 30)

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Ataques
    heroi.ataque(vilao)
    vilao.ataque(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Cone Guy')
    print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()

pygame.quit()
sys.exit()