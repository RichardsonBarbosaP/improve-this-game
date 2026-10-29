from .personagem import Personagem # Importa a classe Personagem
#from heroi import Heroi

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        #self.coragem = None

    def usar_item(self):
        self.upgrade_vida(20)

    def __str__(self):
        return f'Herói: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'