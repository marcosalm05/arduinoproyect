#control de servomotor
from pyfirmata import Arduino, SERVO
from time import sleep

#establecer comunicacion Arduino
port = 'COM6'
board = Arduino(port)
#tiempo necesario para establecer comunicacion con arduino
sleep(5)

#establecer el pin donde se conecta el Servomotor
pin = 3
board.digital[pin].mode = SERVO

#angulo para mover el servo
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

#testea la funcion por donde esta rotando el motor
while True:
    for i in range(0, 180):
        setServoAngle(pin, i)
    for i in range(180, 1, -1):
        setServoAngle(pin, i)
    # continuar o salir del bucle testing
    i = raw_input("Ingresa 'y' para continuar o presiona salir")
    if i == 'y':
        pass
    else:
        board.exit()
        break