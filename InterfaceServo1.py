from logging import root
from msilib.schema import CompLocator
from tkinter import HORIZONTAL, Button, Scale, Tk
from turtle import pos
import tkinter
from tkinter import *
from time import sleep
from pyfirmata import Arduino, util, SERVO

#configuracion de placa Arduino

board = Arduino('COM6')
#puerto de comunicaciones de la placa
sleep(5)
#datos de posiciones del servomotor
board.digital[3].mode = SERVO

#funcion para mover el servomotor
def servo(posiciones):
 
    #escritura de angulo en servomotor
    board.digita[3].write(posiciones)

#encender Led

def led_on():

    board.digital[13].write(1)

def led_off():
     
    board.digital[13].write(0)

root = Tk()

root.title("Control de Servomotor")
root.minsize(300, 150)

#Barra de Angulo
angulo = Scale(root,
                command= servo,
                from_=50,
                to = 100,
                orient= HORIZONTAL,
                troughcolor= 'gray',
                width=30,
                cursor='dot',
                label='Angulo Servo'
                )

angulo.grid(column=2, row=1)

#boton encendido

Bon = Button(root, text="Encender LED", command=led_on)
Bon.grid(column=1, row=3)

Boff = Button(root, text="Apagar Led", command=led_off)
Boff.grid(column=3, row=3)

root.mainloop()
#este cod funciona