import pygame as py
import random
import pygame
import sys
import os
fx = 100
fy = 80
fx1 = 75
fy1 = 65
num_fx = 6
num_fy = 5
num_ftotal =30
screenX = 800
screenY = 560
player_size = 64 
margin = 2

pl = os.listdir('players_image')
b1 = "Assets/b1.jpg"
b2 = "Assets/b2.png"
b3 = "Assets/b3.png"
info = "Assets/info.png"
pl1 = "players_image/"+random.choice(pl)
pl2 = "players_image/"+random.choice(pl)
while pl1 == pl2:
    pl2 = "players_image/"+random.choice(pl)

rocket = "Assets/Astronaut.png"
space = "Assets/Frame.png"
status_bar1 = "Assets/status_bar.png"
sound_icon1 = "Assets/sound.png"
back_icon1 = "Assets/back.png"
roll_butt1 = "Assets/Roll.png"
asteroid1 = "Assets/asteroid.png"
blackhole1 =  "Assets/black-hole.png"
star1 = "Assets/shooting-star.png"
dice_1 = "Assets/dice1.png"
dice_2 = "Assets/dice2.png"
dice_3 = "Assets/dice3.png"
dice_4 = "Assets/dice4.png"
dice_5 = "Assets/dice5.png"
dice_6 = "Assets/dice6.png"
winner = "Assets/winner.png"
icon = "Assets/shuttle.png"
asteroid_music = "Music/asteroid.wav"
star_music = "Music/shooting-star.wav"
blackhole_music = "Music/blackhole.wav"
rocket_music = "Music/rocket_music.wav"
game_music = "Music/game_sound.wav"
open_sound = "Music/opening.wav"
winning_sound= "Music/winning.wav"

py.init()
# screen size
screen = py.display.set_mode((800, 560))

# setting caption and game icon
py.display.set_caption("SpaceX")
icon =py.image.load(icon)
py.display.set_icon(icon)

#the layout of game grid
frames = list()
for i in range(30):
    frames.append(py.Surface((100,80)))
    frames[i].set_alpha(240)

background1 = py.image.load(b1).convert()
background1.set_alpha(180)
rocketImg = py.image.load(rocket)
background2 = py.image.load(b2)
background3 = py.image.load(b3)
background3.set_alpha(120)
infoImg = py.image.load(info).convert()
status_bar = py.image.load(status_bar1)
sound_icon = py.image.load(sound_icon1)
back_icon = py.image.load(back_icon1)
roll_icon = py.image.load(roll_butt1)
asteroid = py.image.load(asteroid1)
blackhole = py.image.load(blackhole1)
star = py.image.load(star1)
dice1 = py.image.load(dice_1)
dice2 = py.image.load(dice_2)
dice3 = py.image.load(dice_3)
dice4 = py.image.load(dice_4)
dice5 = py.image.load(dice_5)
dice6 = py.image.load(dice_6)
p1Img = py.image.load(pl1)
p2Img = py.image.load(pl2)
winnerImg = py.image.load(winner).convert()
menu_butt = py.Rect(0, 0, 800, 560)
menu_butt2 = py.Rect(0, 0, 800, 560)
start_butt = py.Rect(155, 358 , 100, 50)
start_butt.center = (400, 180)
resume_butt = py.Rect(0, 0, 160, 50)
resume_butt.center = (400, 240)
quit_butt = py.Rect(0, 0, 86, 50)
quit_butt.center = (400, 300)
roll_butt = py.Rect((273, 490, 162, 60))
sound_butt = py.Rect((18, 500, 52, 52))
back_butt = py.Rect((742, 500, 40,40))
b_s = py.mixer.Sound(blackhole_music)
s_s = py.mixer.Sound(star_music)
a_s = py.mixer.Sound(asteroid_music)
r_s = py.mixer.Sound(rocket_music)
o_s = py.mixer.Sound(open_sound)
w_s = py.mixer.Sound(winning_sound)

def ob(x, music=0):
    if music == 1: 
        py.mixer.music.pause()    
    if x == 1:
        py.mixer.Sound.play(a_s)
    elif x == 2:
        py.mixer.Sound.play(s_s)
    elif x == 3:
        py.mixer.Sound.play(b_s)
    elif x == 4:
        py.mixer.Sound.play(r_s)
    elif x == 5:
        py.mixer.Sound.play(o_s)
    elif x == 6:
        py.mixer.Sound.play(w_s)           
    if music == 1:    
        py.mixer.music.unpause()    

def button(mouseX, mouseY):
    if 350 < mouseX < 450 and 155 < mouseY< 215:
            text("Start", 40, "verdana", (255, 255, 255, 150), (0, 0, 0, 0) , 800//2, 180, True)
    else :    
        text("Start", 40, "verdana", (255, 255, 255, 150), None, 800//2, 180, True)
    if 320 < mouseX < 480 and 215 < mouseY< 265:
        text("How to play", 40, "verdana", (255, 255, 255, 100), (0, 0, 0, 100), 800//2, 240, True)
    else :
        text("How to play", 40, "verdana", (255, 255, 255, 100), None, 800//2, 240, True)
    if 358 < mouseX < 442  and 265 < mouseY < 315:
        text("Quit", 40, "verdana", (255, 255, 255, 150), (0, 0, 0, 0), 800//2, 300, True) 
    else :
        text("Quit", 40, "verdana", (255, 255, 255, 150), None, 800//2, 300, True) 
    py.display.update()

def music(name, l, cm, vol):
    py.mixer.music.set_volume(vol)  
    if cm == 0 :
        py.mixer.music.play(l)  
    elif cm == 1:
        py.mixer.music.pause()
    elif cm == 2:
        py.mixer.music.unpause()
    elif cm == 3:
        py.mixer.music.stop()

def roll_blit(dice):
    if dice == 1:
        screen.blit(dice1, (440, 490)) 
    elif dice == 2:
        screen.blit(dice2, (440, 490))
    elif dice == 3:
        screen.blit(dice3, (440, 490))
    elif dice == 4:
        screen.blit(dice4, (440, 490))
    elif dice == 5:
        screen.blit(dice5, (440, 490))
    elif dice == 6:
        screen.blit(dice6, (440, 490))                   
    py.display.update() 
    py.time.delay(800)            
    
def text(txt, size, style, fcolor, bcolor, x, y, b_smooth):
    font = py.font.SysFont(style, size)
    text = font.render(txt, b_smooth, fcolor, bcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def rocket(x1, y1):
    screen.blit(rocketImg, (x1, y1))     

def player(pos1, pos2, flag, m, num1 = 0, num2 = 0):
    #sequence decides which comes above
    screen.blit(background3, (0, 0))
    screen.blit(status_bar, (0, 0))
    screen.blit(sound_icon, (18, 500))
    screen.blit(back_icon, (742, 500))
    screen.blit(roll_icon, (273, 490))
    screen.blit(p1Img, (10, 80))
    screen.blit(p2Img, (720, 80))
    frames[7].blit(blackhole, (8,4))
    frames[14].blit(blackhole, (8,4))
    frames[22].blit(blackhole, (8,4))
    frames[28].blit(blackhole, (8,4))
    frames[2].blit(asteroid, (6,4))
    frames[6].blit(asteroid, (6,4))
    frames[12].blit(asteroid, (6,4))
    frames[18].blit(asteroid, (6,4))
    frames[26].blit(asteroid, (6,4))
    frames[3].blit(star, (12,8))
    frames[24].blit(star, (12,8))
    frames[10].blit(star, (12,8))
    frames[17].blit(star, (12,8))
    frames[20].blit(star, (12,8))

    block=29    
    for i in range(5):
        for j in range(6):
            if i % 2 != 0:
                x = (100+100*j)
                y = (80+(80*i))
                #gc.p2Img = py.transform.scale(p2Img, (gc.fx - 2*gc.margin, gc.fy - 2*gc.margin))
                frames[block] = py.transform.scale(frames[block], (fx - 2*margin, fy - 2*margin))
                screen.blit(frames[block], (x, y))
                if block == pos1:
                    screen.blit(p2Img, (x+18, y+8))
                if block == pos2:
                    screen.blit(p1Img, (x+18, y+8))
                text(str(block+1), 10, "verdana", (255, 255, 255, 150), None, x+80, y+10, True)
            else:
                x = (600-100*j)
                y = (80+(80*i))
                #gc.p2Img = py.transform.scale(p2Img, (gc.fx - 2*gc.margin, gc.fy - 2*gc.margin))
                frames[block] = py.transform.scale(frames[block], (fx - 2*margin, fy - 2*margin))
                screen.blit(frames[block], (x, y))
                if block == pos1:
                    screen.blit(p2Img, (x+18, y+8))
                if block == pos2:
                    screen.blit(p1Img, (x+18, y+8))
                text(str(block+1), 10, "verdana", (255, 255, 255, 150), None, x+80, y+10, True)
            block=block-1
      
    if num1 == 1 or num2 == 1:
        text("2 Tiles Back", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True) 
        ob(1, m)
        py.display.update()
    elif num1 == 2 or num2 == 2:
        text("1 Tile Back", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True)
        ob(1, m)
        py.display.update()
    elif num1 == 3 or num2 == 3:
        text("3 Tiles Back", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True) 
        ob(3, m)
        py.display.update() 
    elif num1 == 4 or num2 == 4:
        text("5 Tiles Back", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True) 
        ob(3, m)
        py.display.update() 
    elif num1 == 5 or num2 == 5:
        text("5 Tiles Ahead", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True) 
        ob(2, m)
        py.display.update()
    elif num1 == 6 or num2 == 6:
        text("3 Tiles Ahead", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True) 
        ob(2, m)
        py.display.update() 
    elif num1 == 7 or num2 == 7:
        text("4 Tiles Ahead", 20, "verdana", (255, 255, 255, 100), None, 400, 30, True) 
        ob(2, m)
        py.display.update()                   


def roll():
    x = random.randint(1,6)
    return x


def obstacle(pos):
    old_pos = sum(pos)
    if old_pos==3 or old_pos==7 or old_pos==19:
        new_pos = sum(pos)-2 
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 1, old_pos
    elif old_pos==13 or old_pos==27: 
        new_pos = sum(pos)-1 
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 2, old_pos 
    elif old_pos == 8 or old_pos == 23:
        new_pos = sum(pos)-3 
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 3, old_pos
    elif old_pos == 15 or old_pos ==29: 
        new_pos = sum(pos)-5
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 4, old_pos  
    elif old_pos == 4 or old_pos == 21:
        new_pos = sum(pos)+5 
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 5, old_pos
    elif old_pos == 11 or old_pos == 25:
        new_pos = sum(pos)+3 
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 6, old_pos   
    elif old_pos == 18 :
        new_pos = sum(pos)+4 
        pos=[]
        pos=[1,(new_pos-1)]
        return pos, True, 7, old_pos      
    else:
        return pos, False,0, old_pos


x2=800
y2=100
def start(x2 = 270 ,y2 = 250, s = 1):
    if s == 0:
        ob(4)
    while True:
        screen.fill((0, 50, 110))
        screen.blit(background1, (0,0))
        text("SpaceX", 80, "verdana", (255, 255, 255), None, 800//2, 200, True)
        text("click to start", 20, "arial", (255, 255, 255, 100), None, 800//2, 515, True)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit() 
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit() 
                    sys.exit() 

            if event.type == py.MOUSEBUTTONDOWN:
                mouseX, mouseY = py.mouse.get_pos()
                if menu_butt.collidepoint((mouseX, mouseY)):
                    menu()

        x2 = x2 - 1
        if x2 < 270 :
            x2 = 270  
        rocket(x2, y2)        
        py.display.update() 


def menu(c=1):
    py.mixer.music.load(game_music)
    py.mixer.music.play(-1)
    command = 1
    running = True
    while running:
        screen.fill((0, 0, 0))
        background2 = py.image.load(b2)
        screen.blit(background2, (0, 2))
        screen.blit(sound_icon, (18, 500))
        screen.blit(back_icon, (742, 500))
        mX, mY = py.mouse.get_pos()
        button(mX,mY)    
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False 
                start()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False  
                    start()

            if event.type == py.MOUSEBUTTONDOWN:
                mouseX, mouseY = py.mouse.get_pos()
                if back_butt.collidepoint(mouseX, mouseY):
                    running = False
                    start()
                if sound_butt.collidepoint(mouseX, mouseY):
                    print("clicked")
                    if command == 0:
                        py.mixer.music.play()
                        command = 1
                    elif command == 1 : 
                        py.mixer.music.stop()
                        command = 0          
                if start_butt.collidepoint((mX, mY)):
                    game(command)
                if resume_butt.collidepoint((mX, mY)):
                    info(command)
                if quit_butt.collidepoint((mX, mY)):
                    sys.exit()    
                     
            if event.type == py.KEYDOWN:
                if event.key == py.K_DOWN or event.key == py.K_UP :
                    pass


path1 = []*30
path2 = []*30
chance = 0
def game(c):
    path1 = []*30
    path2 = []*30
    chance = 1
    screen.fill((0,0,0))
    flag1 = False
    flag2 = False

    #frame_color
    for i in range(30):
        if i % 2 == 0:
            frames[i].fill((0, 0, 0))
  
        else :
            frames[i].fill((0, 0, 10))
    command = c  
    last = 0
    fg1 = True  
    fg2 = True
    running = True
    while running:    
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False

            if event.type == py.MOUSEBUTTONDOWN:
                mouseX, mouseY = py.mouse.get_pos()
                if back_butt.collidepoint(mouseX, mouseY):
                    running = False
                if sound_butt.collidepoint(mouseX, mouseY):
                    print("clicked")
                    if command == 0:
                        py.mixer.music.play()
                        command = 1
                    elif command == 1 : 
                        py.mixer.music.stop()
                        command = 0 
                if roll_butt.collidepoint(mouseX, mouseY):
                    dice_roll = roll()
                    roll_blit(dice_roll)
                    chance = chance+1
                    if chance % 2 != 0:
                        path1.append(dice_roll)
                        if path1[0] == 1 and fg1 == True:
                            ob(5)
                            fg1= False

                        elif path1[0]==1 and sum(path1) < 30:
                            print("player 2:"+str(path1))

                        elif sum(path1) > 30:
                            last = path1[len(path1)-1]
                            path1.pop()
                            path1.append(last-dice_roll)

                        elif sum(path1) == 30:
                            ob(6)
                            py.time.delay(500)
                            winner(command, "Player 2", "Player 1") 
                                
                        else:
                            path1.pop(0)
                    else:
                        path2.append(dice_roll)

                        if path2[0]==1 and fg2 == True:
                            ob(5)
                            fg2 = False

                        elif path2[0] == 1 and sum(path2)<30:
                            print("player 1:"+str(path2))

                        elif sum(path2) > 30:
                            last = path2[len(path2)-1]
                            path2.pop()
                            path2.append(last-dice_roll)

                        elif sum(path2) == 30:
                            ob(6)
                            py.time.delay(500)
                            winner(command, "Player 1", "Player 2")     

                        else:
                            path2.pop(0)

        oldpath1, oldpath2 = 0, 0
        ob_num1, ob_num2 = 0, 0 
        path1, flag1, ob_num1, oldpath1 = obstacle(path1)
        path2, flag2, ob_num2, oldpath2 = obstacle(path2)
        x = oldpath1 - 1
        x1 = oldpath2 - 1 
        
        if flag1 == True or flag2 == True:
            next_blit = py.time.get_ticks()+ 3*1000
        else:
            next_blit = py.time.get_ticks()    

        if next_blit > py.time.get_ticks():
            player(x, x1, True, command, ob_num1, ob_num2)
            py.time.delay(1200)
        else:    
            player(sum(path1)-1, sum(path2)-1, False, command)
        

        py.display.update()

def info(c):
    screen.fill((0,0,0))
    screen.blit(infoImg, (0, 0))
    screen.blit(back_icon, (742, 500))
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                menu()

            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False
                    menu()

            if event.type == py.MOUSEBUTTONDOWN:
                mouseX, mouseY = py.mouse.get_pos()
                if back_butt.collidepoint(mouseX, mouseY):
                    running = False        
        screen.blit(infoImg, (0, 0))
        screen.blit(back_icon, (742, 500))
        py.display.update()

def winner(c, name1= "Player1", name2 = "Player2"):
    mssg1 = name1 + " won!"
    mssg2 = name2 + " better luck next time!"
    screen.fill((0,0,0))
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                menu(c)

            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False
                    menu(c)

            if event.type == py.MOUSEBUTTONDOWN:
                mouseX, mouseY = py.mouse.get_pos()
                if back_butt.collidepoint(mouseX, mouseY):
                    running = False  
                    menu(c)      

        screen.blit(winnerImg, (0,0))
        screen.blit(back_icon, (742, 500))
        text(mssg1, 60, "verdana", (255, 255, 255), None, 400, 100, True) 
        text(mssg2, 20, "verdana", (255, 255, 255), None, 400, 180, True)
        py.display.update()



start(800, 240, 0)   