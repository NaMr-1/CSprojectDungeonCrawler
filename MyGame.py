import pygame as py
from random import randint
from Playing import Player, Obstacle
py.mixer.init()
#stone img: https://publicdomainvectors.org/en/free-clipart/Pile-of-rocks/74332.html
#portal img: https://publicdomainvectors.org/en/free-clipart/Pixel-orange-gem/40472.html
#crystal img: https://publicdomainvectors.org/en/free-clipart/Blue-rock/40875.html
#bg img : https://media.easy-peasy.ai/92095ba3-b100-486f-81bb-376973e32d8c/d204c906-1a2b-4078-8cc5-c5ed74cf48af.
#pix1 img: https://publicdomainvectors.org/en/free-clipart/Vector-illustration-of-colorful-blurry-pixel-character/29224.html
#pix2 img: https://publicdomainvectors.org/en/free-clipart/Colorful-blurry-pixel-kid-vector-drawing/29223.html
#dig sound: https://minecraft.fandom.com/wiki/Category:Armor_stand_sounds
#gem sound: https://minecraft.fandom.com/wiki/Category:Firework_sounds
 
#in this script we will generate n x n grid on the screen
#our player can only move within these cells in the grid
cell_w, cell_h = 60, 60
row, col = 9, 9
screen_w, screen_h = col * cell_w, row*cell_h
panel_w = 3*cell_w
sixes = 0
digs = 0
minus = 0
gems_all = 0
gem_total = 0
index = 0


#generating random value of 0 and 1 in the grid list
#which decides where we draw obstacles
#we choose our probabilities to be 80 - 20 against obstacle.
clock = py.time.Clock()
py.init()
screen = py.display.set_mode((screen_w + panel_w,screen_h))
py.display.set_caption("Generating random grid")

green = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\char.svg")
green = py.transform.scale(green, (60, 60))
blue = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Pix1.svg")
blue = py.transform.scale(blue, (60, 60))
red = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Pix2.svg")
red = py.transform.scale(red, (60, 60))
stones = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\stones.svg")
stones = py.transform.scale(stones, (60, 60))
zero = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\bg.png")
zero = py.transform.scale(zero, (screen_w, screen_h))
one = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\bg.png")
one = py.transform.scale(zero, (screen_w, screen_h))
two = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\bg.png")
two = py.transform.scale(zero, (screen_w, screen_h))
three =  py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\bg.png")
three = py.transform.scale(zero, (screen_w, screen_h))
gems = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Crystal.svg")
gems = py.transform.scale(gems, (60, 60))
portal = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Orange-Gem.svg")
portal = py.transform.scale(portal, (60, 60))
dirt = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\dirt.svg")
dirt = py.transform.scale(dirt, (60, 60))
dig = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Firework_blast.ogg")
gem_sound = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Armor_Stand_break1.ogg")

charIndex = 0
charList = [green, blue, red]
char = charList[charIndex]

p1 = Player(0, 0, 60, 60, char)

bgList = [zero, one, two, three]

def characterChoose(event, charIndex):
    if event.type == py.KEYDOWN:
        if event.key == py.K_y:
            charIndex = 0
        elif event.key == py.K_u:
            charIndex = 1
        elif event.key == py.K_i:
            charIndex = 2
    return charIndex

def gridChange():
    grid = [[randint(0, 4) for _ in range(col)] for _ in range(row)]

    # ensure starting area is free
    grid[0][0], grid[0][1], grid[1][0] = 1, 1, 1

    obstacleList = []
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                obstacleList.append(Obstacle(c * cell_w, r * cell_h, stones))
            elif grid[r][c] == 3:
                grid[r][c] = 6

    return grid, obstacleList

grid, obstacleList = gridChange()


for r in range(row):
    for c in range(col):
        if grid[r][c] == 0:
            obstacleList.append(Obstacle(c*cell_w, r*cell_h, stones))#we append the obstacles based on grid
        elif grid[r][c] == 3:
            grid[r][c] = 6
            
def sixIs(sixes):
    sixes = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 6:
                sixes += 1
    return sixes
'''
coinList = []
for r in range(row):
    for c in range(col):
        if grid[r][c] == 2:
            coinList.append(Coin(c*cell_w, r*cell_h, money))
'''


#set the speedX and speedY to the cell width and cell height so that
#the player moves exactly as the amount of a cell
#Player.speedX = cell_w
#Player.speedY = cell_h
# p2 = Player(500, 500, 50, 50)



def drawGrid(grid:list[list], obstacleList):
    index_obstacle = 0
    #index_coin = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                # py.draw.rect(screen,"#000000", (cell_w*c, cell_h*r, cell_w, cell_h))
                obstacleList[index_obstacle].draw(screen)
                index_obstacle += 1
            
            elif grid[r][c] == 6:
                screen.blit(gems, (c*cell_w, r*cell_h))

            elif grid[r][c] == 5:
                screen.blit(portal, (c*cell_w, r*cell_h))
            
            elif grid[r][c] == 7:
                screen.blit(dirt, (c*cell_w, r*cell_h))
            
            '''
            if grid[r][c] == 2:
                coinList[index_coin].draw(screen)
                index_coin += 1
            '''
            

portal_passes = 0
def draw_panel(screen, gem_total, portal_passes, digs):
    font = py.font.SysFont(None, 30)
    py.draw.rect(screen, "#333333", (screen_w, 0, panel_w, screen_h))
    textSurface1 = font.render(f"Gems: {gem_total}", True, "#cccccc")
    textSurface2 = font.render(f"Portals: {portal_passes}", True, "#cccccc")
    textSurface3 = font.render(f"Digs: {digs}", True, "#cccccc")
    screen.blit(textSurface1, (screen_w + 20, 40))
    screen.blit(textSurface2, (screen_w + 20, 65))
    screen.blit(textSurface3, (screen_w + 20, 90))

def find(event, gems_all):
    r = p1.y // 60
    c = p1.x // 60
    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE and grid[r][c] == 6:
            gems_all += 1
            grid[r][c] = 3
            gem_sound.play()
    return gems_all

def digging(mined, digs, minus):
    if mined == True:
        digs += 1
        minus += 2
    return digs, minus


def check(sixes):
    if sixes == 0:
        grid[0][0] = 5



def portalCheck(event, portal_passes, grid, obstacleList, index):
    r = p1.y // cell_h
    c = p1.x // cell_w

    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE and grid[r][c] == 5:
            grid, obstacleList = gridChange()
            portal_passes += 1
            index += 1
            if index > 3:
                index -= 4

    return portal_passes, grid, obstacleList, index

def gemCount(gems_all, minus, gem_total):
    gem_total = gems_all - minus
    return gem_total
            
            
run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        p1.move(screen, grid, event)
        p1.mine(screen, grid, event)
        digs, minus = digging(event, digs, minus)
        sixes = sixIs(sixes)
        check(sixes)
        portal_passes, grid, obstacleList, index = portalCheck(event, portal_passes, grid, obstacleList, index)
        grid, mined = p1.mine(screen, grid, event)
        gem_total = gemCount(gems_all, minus, gem_total)
        gems_all = find(event, gems_all)
        charIndex = characterChoose(event, charIndex)
        char = charList[charIndex]
        p1.img = char


    #we will need to change the frame rate for this program
    clock.tick(15)
    #clean the previous history of the screen
    # screen.fill("#ffffff")
    screen.blit(bgList[index], (0,0))
    #first draw the grid
    drawGrid(grid, obstacleList)
    draw_panel(screen, gem_total, portal_passes, digs)
    #then draw the player
    p1.draw(screen)
    #then move the player
    #p1.move(screen)
    #for enemy in obstacleList:
        #p1.collision(enemy)
    #update the sreen
    py.display.flip()
py.quit()