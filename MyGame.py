import pygame as py
from random import randint
from Playing import Player, Obstacle
py.mixer.init()
#stone img: https://publicdomainvectors.org/en/free-clipart/Pile-of-rocks/74332.html
#portal img: https://publicdomainvectors.org/en/free-clipart/Pixel-orange-gem/40472.html
#crystal img: https://publicdomainvectors.org/en/free-clipart/Blue-rock/40875.html
#bg1 img : https://media.easy-peasy.ai/92095ba3-b100-486f-81bb-376973e32d8c/d204c906-1a2b-4078-8cc5-c5ed74cf48af.
#pix1 img: https://publicdomainvectors.org/en/free-clipart/Vector-illustration-of-colorful-blurry-pixel-character/29224.html
#pix2 img: https://publicdomainvectors.org/en/free-clipart/Colorful-blurry-pixel-kid-vector-drawing/29223.html
#dig sound: https://minecraft.fandom.com/wiki/Category:Armor_stand_sounds
#gem sound: https://minecraft.fandom.com/wiki/Category:Firework_sounds
#portal sound: https://minecraft.fandom.com/wiki/Category:Boat_sounds
#cat img: https://publicdomainvectors.org/en/free-clipart/Cat-vector-illustration/37579.html
#hotdog img: https://publicdomainvectors.org/en/free-clipart/Hot-dog-vector-image/10696.html
 
#in this script we will generate n x n grid on the screen
#our player can only move within these cells in the grid
cell_w, cell_h = 60, 60
row, col = 9, 9
screen_w, screen_h = col * cell_w, row*cell_h
panel_w = 3*cell_w
total_w = screen_w + panel_w
nines = 0
minus = 0
gems_all = 0
index = 0
answer_on = 0
question_on = 0


questionList = ["How many planets are there in our solar system?", "Hom many days does a week have?"]
answerList = ["8", "7"]

#generating random value of 0 and 1 in the grid list
#which decides where we draw obstacles
#we choose our probabilities to be 80 - 20 against obstacle.
clock = py.time.Clock()
py.init()
screen = py.display.set_mode((screen_w + panel_w,screen_h))
py.display.set_caption("Dungeon Crawler")

green = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\char.svg")
green = py.transform.scale(green, (60, 60))
blue = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Pix2.svg")
blue = py.transform.scale(blue, (60, 60))
red = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Pix1.svg")
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
laptop = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Laptop.svg")
laptop = py.transform.scale(laptop, (60, 60))
catNPC = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\CatNPC.svg")
catNPC = py.transform.scale(catNPC, (60, 60)
hotdog = py.image.load("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Hotdog.svg")
hotdog = py.transform.scale(hotdog, (60, 60)
dig = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Firework_blast.ogg")
gem_sound = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Armor_Stand_break1.ogg")
portal_sound = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\Boat_paddle_water3.ogg")
bg_sound = py.mixer.Sound("C:\\Users\\06Solec\\Documents\\NataliaM\\GameProject\\kodPana\\Gra\\CSprojectDungeonCrawler\\13.oga")


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
    grid = [[randint(0, 7) for _ in range(col)] for _ in range(row)]

    # ensure starting area is free
    grid[0][0], grid[0][1], grid[1][0] = 1, 1, 1

   
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 3:
                grid[r][c] = 9
            elif grid[r][c] == 4:
                grid[r][c] = 11
            elif grid[r][c] == 5:
                grid[r][c] = 15
            elif grid[r][c] == 6:
                grid[r][c] = 16
    return grid

grid = gridChange()
            
def nineIs(nines):
    nines = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 9:
                nines += 1
    return nines
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



def drawGrid(grid:list[list] ):
    index_obstacle = 0
    #index_coin = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                screen.blit(stones, (c*cell_w, r*cell_h)
             
            elif grid[r][c] == 9:
                screen.blit(gems, (c*cell_w, r*cell_h))

            elif grid[r][c] == 8:
                screen.blit(portal, (c*cell_w, r*cell_h))
            
            elif grid[r][c] == 10:
                screen.blit(dirt, (c*cell_w, r*cell_h))

            elif grid[r][c] == 11:
                screen.blit(laptop, (c*cell_w, r*cell_h))

            elif grid[r][c] == 15:
                screen.blit(catNPC, (c*cell_w, r*cell_h))

            elif grid[r][c] == 16:
                screen.blit(hotdog, (c*cell_w, r*cell_h))
             
            
            '''
            if grid[r][c] == 2:
                coinList[index_coin].draw(screen)
                index_coin += 1
            '''
            
def drawInstructions(screen):
    py.draw.rect(screen, "#222255", (0, 0, total_w, screen_h))
    sans_font = py.font.SysFont("dejavusans", 20)
    moveText = sans_font.render(f"Move around using ARROWS", True, "#cccccc")
    crystalsText = sans_font.render(f"Collect crystals by clicking SPACE", True, "#cccccc")
    portalText = sans_font.render(f"Go through portals using SPACE", True, "#cccccc")
    interactText = sans_font.render(f"Interact with obstacles using WASD", True, "#cccccc")
    charText = sans_font.render(f"Change the character to:", True, "#cccccc")
    greenText = sans_font.render(f"green using Y", True, "#cccccc")
    blueText = sans_font.render(f"blue using U", True, "#cccccc")
    redText = sans_font.render(f"red using I", True, "#cccccc")
    
    screen.blit(moveText, (60, 50))
    screen.blit(crystalsText, (50, 80))
    screen.blit(portalText, (50, 110))
    screen.blit(interactText, (50, 140))
    screen.blit(charText, (50, 170))
    screen.blit(greenText, (70, 200))
    screen.blit(blueText, (70, 230))
    screen.blit(redText, (70, 260))


def drawTitleScreen(screen):
    py.draw.rect(screen, "#222255", (0, 0, total_w, screen_h))
    sans_font = py.font.SysFont("dejavusans", 30)
    titleText = sans_font.render(f"Dungeon Crawler", True, "#cccccc")
    contText = sans_font.render(f"To continue, press ENTER", True, "#cccccc")

    screen.blit(titleText, (170, 100))
    screen.blit(contText, (160, 200))

def drawEndScreen(screen, gems_all, question_on, minus):
    py.draw.rect(screen, "#222255", (0, 0, total_w, screen_h))
    sans_font = py.font.SysFont("dejavusans", 30)
    endText = sans_font.render(f"The End", True, "#cccccc")
    gemText = sans_font.render(f"You collected {gems_all} crystals", True, "#cccccc")
    jumpText = sans_font.render(f"You answered {question_on} questions correctly", True, "#cccccc")
    scoreText = sans_font.render(f"Your total score is: {gems_all + question_on - minus}", True, "#cccccc")


    screen.blit(endText, (170, 90))
    screen.blit(gemText, (140, 130))
    screen.blit(jumpText, (140, 170))
    screen.blit(scoreText, (120, 210))

portal_passes = 0
def draw_panel(screen, gems_all, portal_passes):
    font = py.font.SysFont(None, 30)
    py.draw.rect(screen, "#333333", (screen_w, 0, panel_w, screen_h))
    textSurface1 = font.render(f"Gems: {gems_all}", True, "#cccccc")
    textSurface2 = font.render(f"Portals: {portal_passes}", True, "#cccccc")
    screen.blit(textSurface1, (screen_w + 20, 40))
    screen.blit(textSurface2, (screen_w + 20, 65))

def find(event, gems_all):
    r = p1.y // 60
    c = p1.x // 60
    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE and grid[r][c] == 9:
            gems_all += 1
            grid[r][c] = 3
            gem_sound.play()
    return gems_all

def get_question(event, questionList, answerList, answer_on):
    r = p1.y // 60
    c = p1.x // 60
    n = randint(0, len(questionList)-1)
    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE and grid[r][c] == 11:
            user_text = input(questionList[n])
    if user_text == answerList[n]:
        grid[r][c] = 4
        gem_sound.play()
        answer_on += 1
    return answer_on


def digging(grid, event, minus):
   r = p1.y // cell_h
   c = p1.x // cell_w
 
   if event.type == py.KEYDOWN:
        if event.key == py.K_a and grid[r][c-1] == 0 and c - 1 >= 0:
            grid[r][c-1] = 10
            minus +=2
            dig.play()
        elif event.key == py.K_d and grid[r][c+1] == 0 and c + 1 < len(grid[0]):
            grid[r][c+1] = 10
            minus += 2
            dig.play()
        elif event.key == py.K_w and grid[r-1][c] == 0 and r - 1 >= 0:
            grid[r-1][c] = 10
            minus += 2
            dig.play()
        elif event.key == py.K_s and grid[r+1][c] == 0 and r + 1 < len(grid):
            grid[r+1][c] = 10
            minus += 2
            dig.play()
    return grid, minus

def catChoice(event, grid, minus, gems_all):
        q = radint(0,2)
        r = p1.y // cell_h
        c = p1.x // cell_w
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE and grid[r][c] == 15:
                 if q == 0:
                     print("The cat scratched you.")
                     minus += 3
                     grid[r][c] = 5
                     gem_sound.play()
                 elif q == 1:
                     print("The cat hid from you.")
                     grid[r][c] = 5
                     gem_sound.play()
                 elif q == 2:
                     print("The cat gave you gems!")
                     gems_all += 3
                     grid[r][c] = 5
                     gem_sound.play()
        return grid, minus, gems_all   
            
def isHotdog(event, grid, minus, gems_all):
        r = p1.y // cell_h
        c = p1.x // cell_w
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE and grid[r][c] == 16:
                 o = input("Am I a sandwich? yes or no: ")
        if o == "no":
            print("You got it right! Have some gems.")
            gems_all += 5
            grid[r][c] = 6
            gem_sound.play()
        else:
            print("What are you talking about!? Minus points!")
            minus += 5
            grid[r][c] = 4
            gem_sound.play()
        return grid, minus, gems_all    

def check(nines, answer_on):
    if nines == 0 and answer_on > 0:
        grid[0][0] = 8



def portalCheck(event, portal_passes, grid, index, answer_on, question_on):
    r = p1.y // cell_h
    c = p1.x // cell_w

    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE and grid[r][c] == 8:
            portal_sound.play()
            grid, obstacleList = gridChange()
            question_on += answer_on
            answer_on = 0
            portal_passes += 1
            index += 1
            if index > 3:
                index -= 4

    return portal_passes, grid, index, answer_on, question_on
            
            
start = True
intro = False
run = False
ending = False

while start:
    for event in py.event.get():
        if event.type == py.QUIT:
            start = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_RETURN:
                start = False
                intro = True
    drawTitleScreen(screen)
    py.display.flip()


while intro:
    for event in py.event.get():
        if event.type == py.QUIT:
            intro = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_RETURN:
                intro = False
                run = True

    drawInstructions(screen)
    py.display.flip()

bg_sound.play(-1)
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        p1.move(screen, grid, event)
        grid, minus = digging(grid, event, minus)
        grid, minus, gems_all = catChoice(event, grid, minus, gems_all)
        grid, minus, gems_all = isHotdog(event, grid, minus, gems_all)
        nines = nineIs(nines)
        check(nines, answer_on)
        portal_passes, grid, index, answer_on, question_on = portalCheck(event, portal_passes, grid, index ,answer_on, question_on)
        gems_all = find(event, gems_all)
        answer_on = get_question(event, questionList, answerList, answer_on)
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
    draw_panel(screen, gems_all, portal_passes)
    #then draw the player
    p1.draw(screen)
    #then move the player
    #p1.move(screen)
    #for enemy in obstacleList:
        #p1.collision(enemy)
    #update the sreen
    py.display.flip()

    if portal_passes == 5:
        run = False
        ending = True

while ending:
    for event in py.event.get():
        if event.type == py.QUIT:
            ending = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_RETURN:
                ending = False
    drawEndScreen(screen, gems_all, question_on, minus)
    py.display.flip()
py.quit()