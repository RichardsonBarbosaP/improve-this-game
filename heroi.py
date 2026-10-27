from personagem import Personagem
#from heroi import Heroi

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.coragem = None

    def ataque(self, vilao):
        """
        Reduz a vida de um vilão atacado pelo herói.
        """
        print(f'Você deu {self.ataque} de dano em {vilao.nome}!')
        vilao.downgrade_vida()

    def __str__(self):
        return f'Herói: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Status de Coragem: {self.coragem}'