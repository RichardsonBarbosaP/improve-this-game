from personagem import Personagem
from heroi import Heroi

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa, coragem):
        super().__init__(nome, vida, ataque, defesa, coragem)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if coragem not in niveis_validos:
            raise ValueError(f"Status de coragem inválido! Escolha entre {niveis_validos}")
        if coragem == 'Alta':   
            self.ataque += 8 # aumenta o ataque do herói em 8 pontos
        self.coragem = coragem

    def ataque(self, vilao):
        """
        Reduz a vida de um vilão atacado pelo herói.
        """
        print(f'Você deu {self.ataque} de dano em {vilao.nome}!')
        vilao.downgrade_vida()

    def __str__(self):
        return f'Herói: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Status de Coragem: {self.coragem}'