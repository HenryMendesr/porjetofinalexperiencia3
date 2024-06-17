#Para o computador escolher aleatorio
import random
#para que o resultado inicial seja 0 a 0
playerj1 = 0
playerj2 = 0

print('Bem-Vindo, bora jogar?')

#escolha entre modos de jogo
Mododejogo = float(input('Escolha entre as tres estilos de jogo:  1-humano x humano, 2-humano x computador ou 3-computador x computador:'))
#Os modos operantes
while True:
    if Mododejogo == 1:
        player1 = float(input('Escolha ente: 1-Pedra 2-Papel 3-Tesoura:'))
        player2 = float(input('Escolha ente: 1-Pedra 2-Papel 3-Tesoura:'))
    elif Mododejogo == 2:
        player1 = float(input('Escolha ente: 1-Pedra 2-Papel 3-Tesoura:'))
        player2 = (random.choice(['1-Pedra', '2-Papel', '3-Tesoura']))
        print(player2)
    else:
        player1 = (random.choice(['1-Pedra', '2-Papel', '3-Tesoura']))
        player2 = (random.choice(['1-Pedra', '2-Papel', '3-Tesoura']))
        print(player1)
        print(player2)
#Resultados possiveis
    if player1 == player2:
       Resultado = ('Empate')
    elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 3):
        Resultado = ('Player2 vence')
        playerj2 = playerj2  + 1
    else:
        Resultado = ('Player1 vence')
        playerj1 = playerj1 + 1
    print(Resultado)
    #Tabela de pontos
    print("Pontos Totais")
    print('Player1', playerj1)
    print('Player2', playerj2)
    float(input('Você gostaria de continuar jogando:'))
