from .personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.intimidacao = None
            #ataque.heroi -= 8  # Reduz o ataque do herói em 8 pontos
        #self.intimidacao = intimidacao

    def golpe(self, heroi):
        """
        Mecânica de ataque entre personagens. Calcula o dano com base no ataque do atacante e na defesa do alvo.
        """
        while heroi.vida > 0 and self.vida > 0:
            dano = self.ataque - heroi.defesa
            dano = min(dano, 1)
            heroi.vida -= dano
                
            if heroi.vida < 0:  
                heroi.vida = 0
        
            print(f'{self.nome} deu {self.ataque} de dano em {heroi.nome}! Tente se proteger da próxima vez!')
            heroi.downgrade_vida()
        
            heroi.golpe(self)

    def __str__(self):
        return f'Vilão: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'