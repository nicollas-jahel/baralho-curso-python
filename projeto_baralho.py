import random

NAIPES = '♥ ♦ ♣ ♠'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio=False):
    '''Cria um baralho de 52 cartas'''
    baralho = [(n, c) for c in CARTAS for n in NAIPES] # gera uma lista de tuplas em ordem
    if aleatorio:
        random.shuffle(baralho)  # serve para embaralhar uma lista
    return baralho

def distribuir_cartas(baralho):
    '''Gerencia a mão de cartas de acordo com o baralho gerado'''
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]

def jogar():
    '''Inicia um jogo de cartas para 4 jogadores'''
    cartas = criar_baralho(aleatorio=True) # cria o baralho
    jogadores = 'P1 P2 P3 P4'.split() # cria os jogadores
    # gera um dicionário de jogador e carta tipo {'P1': [('♣', '6')]}
    maos = {j: c for j, c in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        # junta os valores da tupla do dict criando a carta com um espaço na frente
        carta = " ".join(f"{n}{c}" for (n,c) in cartas)
        print(f'{jogador}: {carta}') # imprime os valores na tela

if __name__ == '__main__':
    jogar()

'''
P1: ♠A ♥8 ♣A ♠8 ♦K ♠6 ♥9 ♣10 ♣7 ♥Q ♥7 ♣J ♠7
P2: ♣3 ♥A ♣2 ♥10 ♣8 ♦7 ♣5 ♠Q ♦5 ♦8 ♠K ♦10 ♠4
P3: ♠5 ♠10 ♦A ♣9 ♠3 ♦Q ♦2 ♥4 ♥5 ♠2 ♥K ♦4 ♦6
P4: ♠9 ♦J ♣Q ♣6 ♥3 ♥J ♥6 ♦9 ♣K ♣4 ♥2 ♦3 ♠J
'''