import pygame, sys, math, copy
from pygame.locals import *

class GameOfLife:
    def __init__(self):
        pass
        pygame.init()
        self.width=400
        self.height=400
        self.screen = pygame.display.set_mode((self.width, self.height+10),0,32)
        pygame.display.set_caption("Game of Life")
        self.board=[[0 for x in range(self.width/16)] for y in range(self.height/16)]
        self.clock=pygame.time.Clock()
        self.screen.fill((255,255,255))
        self.State=0

        
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
        self.clock.tick(10)
        
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

        if self.State==1:
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


lg=GameOfLife() #__init__ is called right here
while 1:
    lg.update()
# def main():
#     pygame.init()

#     DISPLAY=pygame.display.set_mode((400,400),0,32)

#     WHITE=(255,255,255)
#     blue=(0,0,255)

#     DISPLAY.fill(WHITE)

#     pygame.draw.rect(DISPLAY,blue,(200,150,100,50))

#     while True:
#         for event in pygame.event.get():
#             if event.type==QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# main()