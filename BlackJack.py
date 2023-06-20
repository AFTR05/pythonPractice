import random
import math
def randomGenerator():
    return math.floor(random.random() * 10) + 1

player=input("Ingrese su nombre: ")
cardRandom=0
operation=""
print("Bienvenido ",player)
print("Empecemos a jugar")
cardRandom=randomGenerator()
pointPlayer=cardRandom
print("sacaste una carta con puntaje de ",cardRandom," tu puntaje ahora es: ",pointPlayer
      ,"\nAhora sigue el turno de la maquina")
pointsMachine=randomGenerator()
playerCardVal=True
while (playerCardVal!=False):
    text=input(f"Tu puntaje es {pointPlayer}, ¿desea otra carta? (y/n): ")
    if(text=="y"):
        cardRandom=randomGenerator()
        pointPlayer+=cardRandom
        print("`Sacaste una carta con puntaje de ",cardRandom,",Tu puntaje ahora es: ",pointPlayer,".\nAhora sigue el turno de la maquina")    
        if (pointPlayer>=21) :
            playerCardVal=False
    else: playerCardVal=False

print("Esta bien, espera las decisiones de tu rival....")
while(operation!="finish"):
    if(pointsMachine<=17):
        pointsMachine+=randomGenerator()
        operation="sigo"
    else: operation="finish"
print("Desiciones finalizadas, miremos quien gano")
if((pointPlayer>pointsMachine and pointPlayer<=21) or (pointsMachine>21)):
    print("El ganador es: ",player," con un puntaje de ",pointPlayer,".\n Ya que el puntaje del rival fue ",pointsMachine,"\nFelicidades")
elif((pointsMachine>pointPlayer and pointsMachine<=21) or (pointPlayer>21)):
    print("Te gano tu rival: la computadora, con un puntaje de ",pointsMachine,".\nYa que tu puntaje fue ",pointPlayer,"\nSuerte en la proxima :(")
else:
    print("No hubo ganador.\nTu puntaje es: ",pointPlayer,"\nPuntaje de maquina es ",pointsMachine)