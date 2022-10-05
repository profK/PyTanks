import pymunk
import math
from pgzero import actor

class Tank : # inhrits from pygmezero actor class
    def __init__(self,imageName: str, pos: tuple  ) :
        self.actor = actor.Actor(imageName,pos)

    def draw(self) :
        self.actor.draw()

    def rotate(self,degrees: float):
        self.actor.angle += degrees

    def move(self,distance: float) :
        pos: tuple = self.actor.pos
        angle: float = math.radians(self.actor.angle)
        #0 radians is down, not right, which revrse what we would expect x and y to be
        dy: float = math.cos(angle)*distance
        dx: float = math.sin(angle)*distance;
        self.actor.pos = (pos[0]+dx,pos[1]+dy)


