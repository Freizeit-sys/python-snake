import pygame
import random

from pygame import color 

width = 500
height = 500
rows = 20

pygame.init()
pon = pygame.mixer.Sound('python-sname/pon.wav')
dead = pygame.mixer.Sound('python-sname/dead.wav')

##################################################
## クラス
##################################################

class Cube():
    rows = 20
    w = 500
    
    def __init__(self, start, x=1, y=1, color=(255, 0, 0)):
        self.pos = start
        self.x = x
        self.y = y
        self.color = color
    
    def move(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.pos[0] + self.x, self.pos[1] + self.y)
    
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        
        pygame.draw.rect(surface, self.color (i * dis + 1, j * dis + 1, dis - 2))
        if eyes:
            center = dis // 2
            radius = 3
            circleMiddle = (i * dis + center - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

class Snake():
    body = []
    turns = []
    
    def __init__(self, color, pos):
        self.color = color
        self.head - Cube(pos)
        self.body.append(self.head)
        self.x = 0
        self.y = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            
        for key in keys:
            if keys[pygame.K_LEFT]:
                self.x = -1
                self.y = 0
                self.turns = [self.head.pos[:]] = [self.x, self.y]
            elif keys[pygame.K_RIGHT]:
                self.x = 1
                self.y = 0
                self.turns = [self.head.pos[:]] = [self.x, self.y]
            elif keys[pygame.K_UP]:
                self.x = 0
                self.y = -1
                self.turns = [self.head.pos[:]] = [self.x, self.y]
            elif keys[pygame.K_DOWN]:
                self.x = 0
                self.y = 1
                self.turns = [self.head.pos[:]] = [self.x, self.y]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c.x, c.y)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.x = 0
        self.y = 1
    
    def addBody(self):
        tail = self.body[-1]
        dx, dy = tail.x, tail.y
        
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))
        
        self.body[-1].x = dx
        self.body[-1].y = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

##################################################
## 関数
##################################################

def drawGrid(width, rows, surface):
    size = width // rows
    
    x = 0
    y = 0
    
    for i in range(rows):
        x = y + size
        y = y + size
        pygame.draw.line(surface, (128, 128, 128), (x, 0), (x, width))
        pygame.draw.line(surface, (128, 128, 128), (0, y), (width, y))

def randomFood(rows, food):
    positions = food.body
    
    while True:
        x = random.randrange(1, rows - 1)
        y = random.randrange(1, rows - 1)
        
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)

snake = Snake((255, 0, 0), (10, 10))
window = pygame.display.set_mode((width, height))

def reDrawWindow():
    window.fill((0, 0, 0))
    drawGrid(width, rows, window)
    pygame.display.update()

def main():
    global food
    snake.addBody()
    flag = True
    clock = pygame.time.Clock()()
    food = Cube(randomFood(rows, snake), color=(0, 255, 0))
    pygame.init()
    
    while flag:
        clock.tick(5 + (len(snake.body)))
        snake.move()
        headPos = snake.head.pos
        
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] > 0:
            dead.play()
            print('Score:', len(snake.body))
            snake.reset((10, 10))
            break

        reDrawWindow()
        pygame.display.set_caption('Snake Game')

# 実行
main()