from pygame import *
from random import *
import time
GLOBAL_WIGHT=720
GLOBAL_HEIGHT=480
window=display.set_mode((GLOBAL_WIGHT,GLOBAL_HEIGHT))
display.set_caption('рыбалОчка')
run=True


# class Zastavka(sprite.Sprite):
#     def __init__(self,wight,height,image):
#         sprite.Sprite.__init__(self)
#         self.wight=wight
#         self.height=height
#         self.image=transform.scale(image,(self.wight,self.height))
#     def update(self):
#         window.blit(self.image,(0,0))

# class Screen2(sprite.Sprite):
#     def __init__(self,wight,height,image):
#         sprite.Sprite.__init__(self)
#         self.wight=wight
#         self.height=height
#         self.image=transform.scale(image,(self.wight,self.height))
#         self.rect=self.image.get_rect()
#         self.rect.x =0
#         self.rect.y=0
#     def update(self):
#         window.blit(self.image,(0,0))

class Screen1(sprite.Sprite):
    def __init__(self,wight,height,image,start_y,start_x):
        sprite.Sprite.__init__(self)
        self.start_y=start_y
        self.start_x=start_x
        self.wight=wight
        self.height=height
        self.image=transform.scale(image,(self.wight,self.height))
        self.rect=self.image.get_rect()
        self.rect.x =0
        self.rect.y=0
    def update(self):
        window.blit(self.image,(self.start_x,self.start_y))
        # draw.rect(window, (34, 150, 200),(5,80,50,50))


class Button1(sprite.Sprite):
    def __init__(self,image1,coord_y,coord_x,scale_x,scale_y):
        sprite.Sprite.__init__(self)
        self.scale_x=scale_x
        self.scale_y=scale_y

        self.image=transform.scale(image1, (self.scale_y,self.scale_x))
        self.x=coord_x
        self.y=coord_y
    def update(self):
        window.blit(self.image,(self.y,self.x))

class Poplavok(sprite.Sprite):
    def __init__(self, image1 , start_X, start_y , scale_x , scale_y):
        sprite.Sprite.__init__(self)
        self.wight=scale_x
        self.height=scale_y
        self.image=transform.scale(image1,(self.wight,self.height))
        self.x=start_X
        self.y=start_y
     
    def update(self,ribalka,w):
        window.blit(self.image,(self.y,self.x))  
        self.check_w=w 
        self.ribalka=ribalka

        if self.ribalka:
            self.x+=1
        if self.check_w:
            self.x-=1      

    def pos(self,x):
        self.x+=x
        return self.x
        print(self.x)
        # print(self.check, self.ribalka,self.check_w)
                

class Rod(sprite.Sprite):
    def __init__(self, image1 , start_X, start_y , scale_x , scale_y):
        sprite.Sprite.__init__(self)
        self.wight=scale_x
        self.height=scale_y
        self.image=transform.scale(image1,(self.wight,self.height))
        self.x=start_X
        self.y=start_y
     
    def update(self,ribalka,w):
        window.blit(self.image,(self.y,self.x))          
        self.ribalka=ribalka



class Fish(sprite.Sprite):
    def __init__(self,image1,scale_x,scale_y,pos_x,pos_y):
        sprite.Sprite.__init__(self)
        self.wight=scale_x
        self.height=scale_y
        self.image=transform.scale(image1,(self.wight,self.height))
        self.x_pos=pos_x
        self.y_pos=pos_y
    def update(self,):
        window.blit(self.image,(self.y_pos,self.x_pos))     
    def post(self,x_pos,y_pos):
        self.y_pos=y_pos
        self.x_pos=x_pos
        # print(self.x_pos,self.y_pos)
 

###########################################################
zastavka=image.load('game1.png')
zastavka=Screen1(GLOBAL_WIGHT, GLOBAL_HEIGHT, zastavka,0,0)

danik=image.load('pause.png')       
danik=Screen1(GLOBAL_WIGHT, GLOBAL_HEIGHT, danik,0,0)

game=image.load('fon1.png')       
game=Screen1(GLOBAL_WIGHT, GLOBAL_HEIGHT, game,0,0)

success=image.load('success.png')
success_pic=Screen1(100,40, success,220,600)
fail=image.load('fail.png')
fail_pic=Screen1(100,40, fail,220,600)

stash=image.load('stash.png')
stash=Screen1(160,190, stash,220,0)

exit_key=image.load('exit.png')
return_key=image.load('return.png')
start_key=image.load('start.png')
e_key=image.load('e.png')
w_key=image.load('w.png')
q_key=image.load('q.png')
q_key=Button1(q_key,100,10,40,40)
w_key=Button1(w_key,150,10,40,40)
e_key=Button1(e_key,200,10,40,40)
start_key=Button1(start_key, 50, 360,40,100)
return_key=Button1(return_key, 50, 200, 40, 120)
exit_key1=Button1(exit_key, 50, 420, 40, 120)
exit_key2=Button1(exit_key, 50, 260, 40, 120)


karas=image.load('fish1.png')
losos=image.load('fish2.png')
yaz=image.load('fish3.png')
seeweed=image.load('seeweed.png')

karas=Fish(karas, 50, 20,250,20)
losos=Fish(losos, 50, 20,250,20)
yaz=Fish(yaz, 50, 20,250,20)
seeweed=Fish(seeweed, 50, 20,250,20)



rod=image.load('rod_1.png')
rope=image.load('rope.png')
poplavok=image.load('polavok.png')
poplavok=Poplavok(poplavok,240 ,325 , 100, 150)
rod=Rod(rod, 160, 100,400,200)
rope=Rod(rope,205, 315, 120, 100)
###########################################################
start_check=False
pause=False
ribalka=False
check_w=False
ulov=False
in_stash=False
tic=0
toc=0
timer_check=False
happeness=False
happeness_check=0
fishka=[losos,seeweed,karas,seeweed,yaz]
ulov_group={}
fishka_list=[]


fishki=sprite.Group()
a=sprite.Group()
s=sprite.Group()
stash_group=sprite.Group()
###########################################################
print(s)
while run:

    s.update()  
    a.update(ribalka,check_w)

    if not(in_stash):
        stash_group.remove(stash)
        fishki.remove(karas,losos,yaz,seeweed)
    if in_stash:
        for i in range(len(fishka_list)):
            fishka_list[i].post(250+i*10,20+i*5)
            # print(fishka_list[i])
            fishki.add(fishka_list[i])
                            
        stash_group.add(stash)
    if start_check==False:
        pause=False
        s.add(zastavka)
        s.add(start_key)
        s.add(exit_key1)
    EVENTS=event.get()
    if poplavok.pos(0)==350:
        ribalka=False
        poplavok.pos(-1)
        ulov=True
        happeness=choice(fishka)
        print(poplavok.pos(0))
    if poplavok.pos(0)==239:
        timer_check=True
        check_w=False
        poplavok.pos(0)
        tic=time.perf_counter()
        if ulov:
            if happeness==losos:
                print('something caught')
                stash_group.add(success_pic)
                # fishki.add(losos)
                fishka_list.append(losos)
            if happeness==karas:
                print('something caught')
                stash_group.add(success_pic)
                # fishki.add(karas)
                fishka_list.append(karas)
            if happeness==yaz:
                print('something caught')
                stash_group.add(success_pic)
                # fishki.add(yaz)
                fishka_list.append(yaz)
            if happeness==seeweed:
                print('nothing caught')
                stash_group.add(fail_pic)
                # fishki.add(seeweed)
                fishka_list.append(seeweed)   
        ulov=not(ulov)
        poplavok.pos(1)
        print(poplavok.pos(0))             
    for e in EVENTS:

        if e.type == QUIT:
                run=False          
        if not(start_check):
            if e.type ==MOUSEBUTTONDOWN:
                        if e.button==1:
                            mouse_pos=mouse.get_pos()
                            print(mouse_pos)  
                            if (mouse_pos[1]>=360 and mouse_pos[1]<=400) and (mouse_pos[0]>=50 and mouse_pos[0]<=150):
                                start_check=True
                            if (mouse_pos[1]>=420 and mouse_pos[1]<=460) and (mouse_pos[0]>=50 and mouse_pos[0]<=170):
                                run=False

        if start_check:
            s.remove(zastavka,start_key,exit_key1)

            if pause==True: 
                in_stash=False
                # stash_group.remove(stash)
                # fishki.remove(karas,losos,yaz,seeweed)
                s.add(danik)
                s.add(return_key)
                s.add(exit_key2)
                s.remove(game,q_key,w_key,e_key)
                if e.type == KEYDOWN:
                    if e.key==K_ESCAPE:
                        print(1,s.has(game))
                        pause=False
                if e.type ==MOUSEBUTTONDOWN:
                            if e.button==1:
                                mouse_pos=mouse.get_pos()
                                print(mouse_pos)  
                                if (mouse_pos[1]>=200 and mouse_pos[1]<=240) and (mouse_pos[0]>=50 and mouse_pos[0]<=170):
                                    pause=False
                                if (mouse_pos[1]>=260 and mouse_pos[1]<=300) and (mouse_pos[0]>=50 and mouse_pos[0]<=170):
                                    start_check=False

                    
                
            else:
                
                s.add(game)
                s.remove(danik,return_key,exit_key2)
                if e.type == KEYDOWN:
                    if e.key==K_ESCAPE:
                        print(1111)
                        pause=True
                    if e.key==K_e:
                        ribalka=True
                        print(poplavok.pos(0))
                        print('press e')
                    if e.key==K_w:
                        check_w=True
                        
                        print('press w')
                    if ulov:       
                        if e.key == K_ESCAPE:
                            ulov=False
                            stash_group.remove(success_pic,fail_pic)
                            print(happeness)
                    if e.key == K_q:
                        print(fishka_list)
                        in_stash=not(in_stash)
                        # for i in range(len(fishka_list)):
                        #     fishka_list[i].post(250+i*10,20+i*5)
                        #     print(fishka_list[i])
                        #     fishki.add(fishka_list[i])
                            
                            # for i in ulov_group:
                            #     print(ulov_group[i])

                    



            if s.has(danik):
                
                a.remove(rod,rope,poplavok)
                check_w=False
                ribalka=False
                if e.type ==MOUSEBUTTONDOWN:
                    if e.button==1:
                        mouse_pos=mouse.get_pos()
                        print(mouse_pos)
            if s.has(game):
                s.add(q_key)
                s.add(w_key)
                s.add(e_key)
                
                a.add(rod)
                a.add(rope)
                a.add(poplavok)
                if e.type ==MOUSEBUTTONDOWN:
                    if e.button==1:
                        mouse_pos=mouse.get_pos()
                        print(mouse_pos)    




    if not(check_w):
        toc=time.perf_counter()
        # print(tic,toc)
    if timer_check:

        if (toc-tic)>=1:
            timer_check=False
            stash_group.remove(success_pic,fail_pic)

    stash_group.update()
    fishki.update()
    display.update()

    ###доделать кноку й(complete), вызов стэша, добавить файл и сакцес 
    #### добавить рыб


    ####сделать классы резов и рыб 