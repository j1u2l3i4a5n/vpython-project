
# coding: utf-8

# In[17]:

from vpython import *
import time
import random

scene = canvas()
drag = False
def draw_bar(L = 100, speed = 10 , R = 100):
    yellow_bar = box(pos = vector(-450, 60, 50), length=L, height=20, width=1, color = color.yellow, shininess = 0)
    blue_bar = box(pos = vector(-450, -60, 50), length=L, height=20, width=1, color = color.blue, shininess = 0) 
    time_count = 0
    move_way = 'right'
    timestamp = 0
    while timestamp < 10:
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
        
    yellow_bar.visible = False
    blue_bar.visible = False
    del yellow_bar
    del blue_bar
    
def fixation_point(L = 10, H = 1, span = 0.5):
    hori = box(pos = vector(0,0,0), axis = vector(1,0,0), length = L, horizontal = H, width = 1)
    verti = box(pos = vector(0,0,0), axis = vector(0,1,0), length = L, horizontal = H, width = 1)
    time.sleep(span)
    hori.visible = False
    verti.visible = False
    del hori
    del verti
    
def pipeline():
    feature_speed = [5,8,10]
    feature_length = [50, 100, 200]
    bar_wigth = []
    bar_contrast = []
    pool = [feature_speed, feature_length, bar_wigth, bar_contrast]
    all_combination = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(2):
                    all_combination.append((i,j,k,l))
    random.shuffle(all_combination)
    
    data_dict = {}
    
    for i in all_combination:
        
        
        
        
        
        
        fixation_point()
        result = 
        index = str(i[0])+str(i[1])+str(i[2])+str(i[3])
        if index in data_dict:
            data_dict[index].append(result)
        else:
            data_dict[index] = [result]
    
    
def write_file(filename = 'data.csv', id_num, data):
    with open(filename, 'a') as files:
        files.write('%s,'%(id_num))
        for i in data:
            files.write(data[i])
            
        files.write('\n')
    
scene.camera.pos = vector(0, 0, 50)
scene.userzoom = False
scene.userspin = False
#draw_bar(L = 50, speed = 5, R = 20)
fixation_point()





# In[22]:




# In[18]:




# In[ ]:



