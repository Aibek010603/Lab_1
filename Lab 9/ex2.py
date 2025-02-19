import pygame
import random
import time

pygame.init()

width, height = 500, 500
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

x, y = 250, 250
delta_x, delta_y = -10, 0

food_x, food_y = random.randrange(0, width) // 10*10, random.randrange(0, height) // 10*10
fps = 10

col_list = [(x, y)]

clock = pygame.time.Clock()
gameover = False

font = pygame.font.SysFont("bahnschrift", 25)
def snake():
    global x, y, food_x, food_y, gameover
    x = (x + delta_x)%width
    y = (y + delta_y)%height
    
    if((x, y) in col_list):
        gameover = True
        return
    col_list.append((x, y))
    if(food_x == x and food_y == y):
        while((food_x, food_y) in col_list):
            food_x, food_y = random.randrange(0, width) // 10*10, random.randrange(0, height) // 10*10
    else:
        del col_list[0]
    game_screen.fill((0, 0, 0))
    score = font.render("Score: " + str(len(col_list)), True, (255, 255, 0))
    game_screen.blit(score, [0, 0 ])
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])
    for(i, j) in col_list:
        pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
        game_screen.blit(gameover_msg, [width//3, height//3])
    pygame.display.update()
while True:
    if(gameover):
        game_screen.fill((0, 0, 0))
        score = font.render("Score: " + str(len(col_list)), True, (255, 255, 0))
        game_screen.blit(score, [0, 0 ])
        gameover_msg = font.render("Game over", True, (255, 255, 255))
        game_screen.blit(gameover_msg, [width//3, height//3])
        pygame.display.update()
        time.sleep(15)
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                if(delta_x != 10):
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if(delta_x != -10):
                    delta = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                if(delta_y != 10):
                    delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                if(delta_y != -10):
                    delta_y = 10
            else:
                continue
            snake()
    if(not events):
        snake()
    clock.tick(fps)