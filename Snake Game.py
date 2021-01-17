import pygame
import random
import time

pygame.init()

width = 20
height = 20
length = 30

x = random.randint(2, width - 1)
y = random.randint(2, height - 1)
direction = random.randint(1, 4)
position = []
position.insert(0, [x, y])
u = random.randint(2, width - 1)
v = random.randint(2, height - 1)

score = 0
speed = 0.4

window = pygame.display.set_mode((length * width, height * length))
pygame.display.set_caption("Snake Game")

done = False
while not done:
    touch = False
    if (x == u) and (y == v):
        u = random.randint(2, width - 1)
        v = random.randint(2, height - 1)
        touch = True
        score += 1
        if (score == 5):
            score = 0
            speed -= 0.1
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                if (direction != 1):
                    direction = 2
            elif (event.key == pygame.K_RIGHT):
                if (direction != 2):
                    direction = 1
            elif (event.key == pygame.K_UP):
                if (direction != 4):
                    direction = 3
            elif (event.key == pygame.K_DOWN):
                if (direction != 3):
                    direction = 4
    if (direction == 1):
        x += 1
    elif (direction == 2):
        x -= 1
    elif (direction == 3):
        y -= 1
    elif (direction == 4):
        y += 1
    if (x < 1) or (x > width) or (y < 1) or (y > height):
        done = True
    for i in range(len(position)):
        if (x == position[i][0]) and (y == position[i][1]):
            done = True
    position.insert(0, [x, y])
    if not touch:
        position.pop()
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, 0, length * width, length * height))
    for i in range(len(position)):
        e = position[i][0]
        f = position[i][1]
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(length * (e - 1), length * (f - 1), length, length))
    pygame.draw.rect(window, (0, 255, 255), pygame.Rect(length * (u - 1), length * (v - 1), length, length))
    pygame.display.update()
    time.sleep(speed)
pygame.display.quit()
pygame.quit()
