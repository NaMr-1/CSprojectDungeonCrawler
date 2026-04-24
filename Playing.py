import pygame as py
from random import randint
py.mixer.init()

class Player:
    '''
    Player is a rectangle object of pygame
    So it must take x, y, width and height
    '''
    #the following variables are known as static or class variables
    speedX, speedY = randint(3, 6), randint(1, 4)
    dig = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Firework_blast.ogg")
    # bark = py.mixer.Sound()


    def __init__(self, x:int, y:int, w:int, h:int, img):
        #the following variables are called instance variables
        #because they are specific to a given object
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (self.x, self.y, self.w, self.h)
        self.collide = False
        self.img = img
    
    def draw(self, screen):
        # py.draw.rect(screen, "#f8f6f9", self.rect)
        screen.blit(self.img, (self.x, self.y))
    
    def move(self, screen, grid, event):
        r = self.y // 60
        c = self.x // 60
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT and c - 1 >= 0 and grid[r][c-1] != 0:
                self.x -= 60
                Player.dig.play()
            if event.key == py.K_RIGHT and c + 1 < len(grid[0]) and grid[r][c+1] != 0:
                self.x += 60
                Player.dig.play()
            if event.key == py.K_UP and r - 1 >= 0 and grid[r-1][c] != 0:
                self.y -= 60
                Player.dig.play()
            if event.key == py.K_DOWN and r + 1 < len(grid) and grid[r+1][c] != 0:
                self.y += 60
                Player.dig.play()
            '''
            if event.key == py.K_SPACE and grid[r][c] == 2:
                grid[r][c] = 1
                Player.coin += 1
            '''
            
        '''
        keys = py.key.get_pressed() #checks of a key is pressed
        if keys[py.K_a] and self.x > 0:
            self.x -= Player.speedX
        if keys[py.K_d] and self.x < 600 - self.w:
            self.x += Player.speedX
        if keys[py.K_w] and self.y > 0:
            self.y -= Player.speedY
        if keys[py.K_s] and self.y < 600 - self.h:
            self.y += Player.speedY
        #once the (x,y) are updated then we must update rect object
        self.rect = (self.x, self.y, self.w, self.h)
        '''
        
    def mine(self, screen, grid, event):
        r = self.y // 60
        c = self.x // 60
        if event.type == py.KEYDOWN:
            if event.key == py.K_a and c - 1 >= 0 and grid[r][c-1] == 0:
                grid[r][c-1] = 7
                Player.dig.play()
            elif event.key == py.K_d and c + 1 < len(grid[0]) and grid[r][c+1] == 0:
                grid[r][c+1] = 7
                Player.dig.play()
            elif event.key == py.K_w and r - 1 >= 0 and grid[r-1][c] == 0:
                grid[r-1][c] = 7
                Player.dig.play()
            elif event.key == py.K_s and r + 1 < len(grid) and grid[r+1][c] == 0:
                grid[r+1][c] = 7
                
                Player.dig.play()
        return grid

    def collision(self,enemy):
        #enemy is also a player object
        #the collision happens if the difference between x cord and y cord is
        #less than width and height respectively
        if abs(self.x-enemy.x) <= self.w and abs(self.y - enemy.y) <= self.h:
            if self.collide == False:#so if the collision happens first time
                #then we print the collision
                print("collision")
                #then we set it's value to True
                self.collide = True
        elif self.collide == True:
            self.collide = False
                

class Obstacle:
    '''
    This is an obstacle which will have fixed size for now
    and we only need to store (x, y) coordinates.
    '''

    def __init__(self, x:int, y:int, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        # return py.draw.rect(screen, "#000000", (self.x, self.y, 60, 60))

"""
class Coin:
    '''
    This is an obstacle which will have fixed size for now
    and we only need to store (x, y) coordinates.
    '''

    def __init__(self, x:int, y:int, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        # return py.draw.rect(screen, "#000000", (self.x, self.y, 60, 60))
"""