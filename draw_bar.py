# coding: utf-8

from vpython import *
import time
canvas()
def draw_bar(L = 100, speed = 10 , R = 100):
    yellow_bar = box(pos = vector(-450, 60, 50), length=L, height=20, width=1, color = color.yellow)
    blue_bar = box(pos = vector(-450, -60, 50), length=L, height=20, width=1, color = color.blue) 
    time_count = 0
    move_way = 'right'
    timestamp = 0
    while timestamp < 20:
        if move_way == 'right':
            move_vec = vector(900 / (speed * R), 0, 0)
        else:
            move_vec = vector(-900 / (speed * R), 0, 0)
        yellow_bar.pos += move_vec
        blue_bar.pos += move_vec
        if yellow_bar.pos.x >= 450:
            move_way = 'left'
        elif yellow_bar.pos.x <= -450:
            move_way = 'right'
        rate(R)
        timestamp += 1/R
    
    
draw_bar(L = 50, speed = 5, R = 20)




