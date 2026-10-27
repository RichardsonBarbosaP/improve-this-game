from personagem import Personagem  # Importa a classe Personagem

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

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()

    def __str__(self):
        return f'Vilão: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Status de Intimidação: {self.intimidacao}'