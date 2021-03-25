#!/usr/bin/env python

import turtle
import sys
import tkinter as tk

#s = turtle.getscreen()
t = turtle.Turtle()
#color('red', 'yellow')

while True:
    t.forward(200)
    t.left(150)
    if abs(t.pos()) < 1:
        break
        #t.circle(60)

t.end_fill()
sys.exit()
