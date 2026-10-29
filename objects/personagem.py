import random

class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def golpe(self, alvo):
            """
            Mecânica de ataque entre personagens. Calcula o dano com base no ataque do atacante e na defesa do alvo.
            """
            #while alvo.vida > 0 and self.vida > 0:
            dano_variavel = random.randint(1, 120)
            dano_critico = random.random()  # Adiciona um fator de aleatoriedade ao dano
            dano = self.ataque + dano_variavel
            dano_final = dano - alvo.defesa
            dano = max(dano_final, 1)
            alvo.vida -= dano_final
            
            if self.vida < 0:  
                self.vida = 0
                print(f'{self.nome} foi derrotado por {alvo.nome}!')
                return  # Sai da função se o alvo estiver morto

            
            if dano_critico <= 0.10:
                dano *= 2 
                print("💥 GOLPE CRÍTICO!!! 💥")
            
            print(f'> {self.nome} deu {dano} de dano em {alvo.nome}!')
            alvo.downgrade_vida()

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após o ataque: {self.vida}')

    def __str__(self):
        return f'Personagem: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'
