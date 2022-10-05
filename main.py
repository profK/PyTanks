# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pgzrun
import pymunk
#from pgzero import keyboard
import math  # has PI in it
from Tank import Tank

WIDTH = 800
HEIGHT = 600

# Press the green button in the gutter to run the script.

def update():
    space.step(1 / 50.0)
    if keyboard.right :
        #turn right
        tank.rotate(-1)
    if keyboard.left :
        #turn left
        tank.rotate(1)
    if keyboard.up :
        tank.move(1)
    if keyboard.down:
        tank.move(-1)


def draw():
    screen.fill((0, 0, 0))
    tank.draw()
    clock.tick(50)


space = pymunk.Space()

tank: Tank = Tank("green_tank",{400,300})

pgzrun.go()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
