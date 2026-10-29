import random
import pygame
from .personagem import Personagem  
preparo_ms = 800        
janela_parry_ms = 350   # Variável global para a duração da janela de parry (em milissegundos)

class Vilao(Personagem):
    # """
    # A classe Vilao representa as características de um vilão no jogo.
    # Herda da classe Personagem.
    # """

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.estado = "parado"  
        self.inicio_estado = 0
        self.parry_feito = False

    def __str__(self):
        return f'Vilão: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'

    def iniciar_ataque(self):
        #"""Começa o ataque do vilão (não trava o jogo, só muda o estado)."""
        self.preparo_ms = random.randint(250, 1300)
        print(self.preparo_ms)
        self.estado = "preparando"
        self.inicio_estado = pygame.time.get_ticks()
        self.parry_feito = False

    def tentar_parry(self):
        #"""Chamado quando o jogador aperta ESPAÇO. Só vale dentro da janela."""
        if self.estado == "janela":
            self.parry_feito = True

    def atualizar(self, alvo):
        # """
        # Chamar uma vez por frame.
        # Retorna uma mensagem quando o ataque for resolvido, ou None.
        # """
        agora = pygame.time.get_ticks()
        decorrido = agora - self.inicio_estado

        if self.estado == "preparando" and decorrido >= preparo_ms:
            self.estado = "janela"
            self.inicio_estado = agora
            print("Aperte ESPAÇO rapidamente para se defender!")

        elif self.estado == "janela":
            if self.parry_feito:
                self.estado = "parado"
                return f'{alvo.nome} conseguiu se defender do ataque de {self.nome}!'
            if decorrido >= janela_parry_ms:
                self.estado = "parado"
                self.golpe(alvo)
                return f'{self.nome} atacou {alvo.nome}!'

        return None