#coding with sayed


import pygame
import sys
import time
import math


pygame.init()

screen=pygame.display.set_mode([660,660])
pygame.display.set_caption("Analog Clock")
bg=pygame.image.load("clock.png")


radius_s=220
radius_m=220
radius_h=180

hour_position=[]
minute_position=[]
seconds_position=[]

def get_second():

    current_sec=time.strftime("%S")

    return current_sec

def get_minute():
    current_min=time.strftime("%M")
    return current_min

def get_hour():
    current_h=time.strftime("%I")        
    return current_h


def get_am_or_pm():
    get_am_or_pm=time.strftime("%p")
    return get_am_or_pm

for h in range(0,60):
    position= [math.cos(math.radians(h*6+270))*radius_h+330,math.sin(math.radians(h*6+270))*radius_h+330] 

    hour_position.append(position)

for m in range(0,60):

    position=[math.cos(math.radians(m*6+270))*radius_m+330,math.sin(math.radians(m*6+270))*radius_m+330]

    minute_position.append(position)

for s in range(0,60):
    position=[int(math.cos(math.radians(s*6+270))*radius_s+330),int(math.sin(math.radians(s*6+270))*radius_s+330)]
    seconds_position.append(position)

    





while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    seconds=get_second()
    minute=get_minute()
    hour=get_hour()

    if int(hour)==12:
        hour_axis_X=hour_position[0*5+int(int(minute)/12)][0]
        hour_axis_Y=hour_position[0*5+int(int(minute)/12)][1]
    else:
        hour_axis_X=hour_position[int(hour)*5+int(int(minute)/12)][0]
        hour_axis_Y=hour_position[int(hour)*5+int(int(minute)/12)][1]

    minute_axis_X=minute_position[int(minute)][0]
    minute_axis_Y=minute_position[int(minute)][1]
    seconds_axis_X=seconds_position[int(seconds)][0]
    seconds_axis_Y=seconds_position[int(seconds)][1]

    screen.blit(bg,[0,0])  

    pygame.draw.line(screen,[0,80,0],(330,330),(hour_axis_X,hour_axis_Y),20)
    pygame.draw.line(screen,[0,90,0],(330,330),(minute_axis_X,minute_axis_Y),15)
    pygame.draw.line(screen,[255,0,0],(330,330),(seconds_axis_X,seconds_axis_Y),10)
   
    
    pygame.draw.circle(screen,[255,0,0],(330,330),15,0)
    font=pygame.font.Font(None,25)
    time_stamp=font.render(hour+":"+minute+":"+seconds+" "+get_am_or_pm(),1,(0,255,255))
    pygame.draw.rect(screen,[0,0,50],(20,20,130,25),0)
    screen.blit(time_stamp,[20,20])    
    
    pygame.display.flip()   
    time.sleep(1)  