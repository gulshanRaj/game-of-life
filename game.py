import os
from glob import glob
import pygame, sys, math, copy, random
from pygame.locals import *
import numpy, pygame.sndarray



class GameOfLife:
    def __init__(self):
        pass
        pygame.mixer.init()
        pygame.init()
        self.width=400
        self.height=400
        self.screen = pygame.display.set_mode((self.width, self.height+10),0,32)
        pygame.display.set_caption("Game of Life")
        self.board=[[0 for x in range(self.width/16)] for y in range(self.height/16)]
        self.clock=pygame.time.Clock()
        self.screen.fill((255,255,255))
        self.State=0
        self._songs=[]
        PATH='/home/gulshan/Projects/gameOfLife/Loopmasters_Producer_Essentials/Keys/'
        #self._songs = ['a.wav', 'b.wav', 'bb.wav', 'c.wav', 'cc.wav', 'd.wav', 'e.wav', 'eb.wav', 'f.wav', 'g.wav', 'ff.wav', 'gg.wav']
        self._songs.append( [y for x in os.walk(PATH+'Rhodes_hard') for y in glob(os.path.join(x[0], '*.wav'))] )
        self._songs.append( [y for x in os.walk(PATH+'Rhodes_Soft') for y in glob(os.path.join(x[0], '*.wav'))] )
        self._songs.append( [y for x in os.walk(PATH+'Piano') for y in glob(os.path.join(x[0], '*.wav'))] )
        self._songs.append( [y for x in os.walk(PATH+'Hammond') for y in glob(os.path.join(x[0], '*.wav'))] )        
        print self._songs[0]
        self.num_of_channels=pygame.mixer.get_num_channels()
        self.ticker=0

        
    def drawBoard(self):
        black=(0,0,0)
        gray=(100,100,100)
        white=(255,255,255)
        red=(100,0,0)
        green=(0,100,0)
        for x in range(self.width/16):
            for y in range(self.height/16):
                if self.board[x][y]:
                    pygame.draw.rect(self.screen, white, (x*16,y*16,15,15))
                else:
                    pygame.draw.rect(self.screen, black, (x*16,y*16,15,15))
            for x in range(self.width/16):
                pygame.draw.rect(self.screen, gray, (x*16+15, 0, 1, self.height))
            for y in range(self.height/16):
                pygame.draw.rect(self.screen, gray, (0, y*16+15, self.width, 1))
        if self.State==0:
            pygame.draw.rect(self.screen, green, (0, self.height, self.width, 10))
        else:
            pygame.draw.rect(self.screen, red, (0, self.height, self.width, 10))
        
    def update(self):
        self.clock.tick(30)
        self.ticker = self.ticker+1
        if self.ticker==30:
            self.ticker=0

        # clear the screen
        self.screen.fill((255,255,255))

        self.drawBoard()

        for event in pygame.event.get():
            if event.type==QUIT:
                exit()

        #input
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()

            #2
            xpos = int(math.floor((mouse[0])/16.0))
            ypos = int(math.floor((mouse[1])/16.0))

            self.board[xpos][ypos] = not self.board[xpos][ypos]

        if pygame.mouse.get_pressed()[2]:
            self.State=1-self.State

        if self.ticker==0 and self.State==1:
            num=400//16
            ar = [[0 for x in range(self.width/16)] for y in range(self.height/16)]
            for x in range(self.width/16):
                for y in range(self.height/16):
                    ar[x][y] = self.board[x][y]

            for x in range(self.width/16):
                for y in range(self.height/16):
                    total = ar[(x-1)%num][(y-1)%num]+ar[(x-1)%num][y]+ar[(x-1)%num][(y+1)%num]
                    total = total + ar[x][(y-1)%num]+ar[x][(y+1)%num]
                    total = total + ar[(x+1)%num][(y-1)%num]+ar[(x+1)%num][y]+ar[(x+1)%num][(y+1)%num]
                    if ar[x][y]:
                        if total<2 or total>3:
                            self.board[x][y]=False
                    else:
                        if total==3:
                            self.board[x][y]=True
        pygame.display.update()

        if self.ticker==0 and self.State==1 : #and random.choice([True, False]):
            #address = 'piano-notes/'
            nchannels = self.num_of_channels
            snd=[None for x in range(4)]
            print snd
            for x in range(self.width/16):
                for y in range(self.height/16):
                    if nchannels<=0:
                        break
                    if self.board[x][y]:
                        #nchannels=nchannels-1
                        
                        if x >=0 and x < 7 and snd[0] is None :
                            snd[0]=(pygame.mixer.Sound(random.choice(self._songs[0])))
                        if x >=7 and x < 13 and snd[1] is None :
                            snd[1]=(pygame.mixer.Sound(random.choice(self._songs[1])))
                        if x >=13 and x < 19 and snd[2] is None :
                            snd[2]=(pygame.mixer.Sound(random.choice(self._songs[2])))
                        if x >=19 and x < 25 and snd[3] is None :
                            snd[3]=(pygame.mixer.Sound(random.choice(self._songs[3])))        
                        #snd.set_volume(0.5+(x+y)/100)
            for z in range(4) :
                tmp = pygame.mixer.find_channel(True)
                if snd[z] is not None :
                    tmp.play(snd[z])


lg=GameOfLife() #__init__ is called right here
while 1:
    lg.update()
