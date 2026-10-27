from .personagem import Personagem # Importa a classe Personagem
#from heroi import Heroi

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.coragem = None

    def golpe(self, vilao):
        """
        Mecânica de ataque entre personagens. Calcula o dano com base no ataque do atacante e na defesa do alvo.
        """
        while vilao.vida > 0 and self.vida > 0:
            dano = self.ataque - vilao.defesa
            dano = min(dano, 1)
            vilao.vida -= dano
        
            if vilao.vida < 0:  
                vilao.vida = 0

            print(f'Você deu {self.ataque} de dano em {vilao.nome}!')
            vilao.downgrade_vida()

            vilao.golpe(self)
        # dano = self.ataque - vilao.defesa
        # dano = min(dano, 1)
        # vilao.vida -= dano
    
        # if vilao.vida < 0:  
        #     vilao.vida = 0


    # Melhorando a vida do herói
    # heroi.upgrade_vida(20)
    # print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    def __str__(self):
        return f'Herói: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'