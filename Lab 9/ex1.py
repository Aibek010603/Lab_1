import pygame
import random

# set up game window
pygame.init()
WIDTH = 500
HEIGHT = 500
screen_size = (WIDTH, HEIGHT)
win = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Racer")

# Colors
red = (200, 0, 0)
green = (75, 210, 54)
gray = (100, 100, 100)
white = (255, 255, 255)
yellow = (255, 232, 0)
# load images

car_img = pygame.image.load("img/car.png")
coin_img = pygame.image.load("img/coin.png").convert_alpha()

# coing image load and fitting to game

image_coinNames = ['coin.png', 'coin2.png']
coin_images = []
for coin_name in image_coinNames:
    img_coin = pygame.image.load("img/" + coin_name)
    coin_images.append(img_coin)
# enemy image load and fitting to the game
image_names = ['enemy_car.png', 'enemy_car2.png', 'enemy_car3.png']
vehicle_images = []
for image_name in image_names:
    image = pygame.image.load("img/" + image_name)
    vehicle_images.append(image)
# coin sprite
coin_group = pygame.sprite.Group()
# enemy sprite
vehicle_group = pygame.sprite.Group()
# Settings & rules
speed = 3
car_speed = 1
coin_speed = 1
coin_count = 1
score = 0
coin_x = WIDTH // 2 - coin_img.get_width() // 2
coin_y = HEIGHT - coin_img.get_height() - 10
car_x = WIDTH // 2 - car_img.get_width() // 2
car_y = HEIGHT - car_img.get_height() - 10
coin_list = []
gameover = False

# markers size
marker_width = 10
marker_height = 50

# road and edge of the markers
road = (100, 0, 300, HEIGHT)
left_edge_marker = (95, 0, marker_width, HEIGHT)
right_edge_marker = (395, 0, marker_width, HEIGHT)

# x coords. of lanes
left_lane = 150
right_lane = 350
center_lane = 250
lanes = [left_lane, center_lane, right_lane]

# for road animation with lane markers
lane_marker_move_y = 0


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        # scaling image down for fitting to lane
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
class Coin(Vehicle):
    def __init__(self, image, x, y):
        image = pygame.image.load("img/coin.png")
        super().__init__(image, x, y)
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load("img/car.png")
        super().__init__(image, x, y)

# player's first starting point
player_x = 250
player_y = 400

# player's car 
player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)
# game loop
clock = pygame.time.Clock()
fps = 60
run = True

while run:
    clock.tick(fps)
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            gameover = False
            running = False
            # quit the game
            pygame.quit()
            

        # move the player's car using the left and right key arrows
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == pygame.K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

            # check if there is a side collision between cars
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True
            # check if there is a collision between player's car and a coin
            for coin in coin_group:
                if pygame.sprite.collide_rect(player, coin):
                    score += 1
                    coin.kill()

    # background
    win.fill(green)

    # road draw
    pygame.draw.rect(win, gray, road)
    
    # markers edge draw
    pygame.draw.rect(win, yellow, left_edge_marker)
    pygame.draw.rect(win, yellow, right_edge_marker)
    
    # marker lane draw
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, HEIGHT, marker_height * 2):
        pygame.draw.rect(win, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(win, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
    # enemy car draw
    player_group.draw(win)
    # enemy car's spawn
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        
        if add_vehicle:
            # random selection of a lane
            lane = random.choice(lanes)

            # random selection
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, HEIGHT / -2)
            vehicle_group.add(vehicle)

    # making the vehicles move to y coords
    for vehicle in vehicle_group:
        vehicle.rect.y += speed 

        # remove vehicle after it goes off screen
        if vehicle.rect.top >= HEIGHT:
            vehicle.kill()

           
    vehicle_group.draw(win)
    # add coins randomly
    if len(coin_group) < 2:
        add_coin = True
        for coin in coin_group:
            if coin.rect.top < coin.rect.height * 1.5:
                add_coin = False
            
        if add_coin:
            # random selection of a lane
            lane = random.choice(lanes)

            # random selection of a coin image
            image = random.choice(coin_images)

            # create the coin object and add it to the group
            coin = Coin(image, lane, -50)
            coin_group.add(coin)

            

           
    coin_group.draw(win)
            
            

    # update coin positions and remove coins that go off screen
    for coin in coin_group:
        coin.rect.y += speed 

        # remove coin after it goes off screen
        if coin.rect.top >= HEIGHT:
            coin.kill() 

    # update coin positions and remove coins that go off screen
    
    # display the score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    win.blit(text, text_rect)
    
    # check if there is a head on collision
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True

    # check if there is a head on collision on a coin
    if pygame.sprite.spritecollide(player, coin_group, True):
        score +=1
        if score > 0 and score % 5 == 0:
                speed += 1
    # player's card draw
    player_group.draw(win)
    # game over text
    if gameover:
        pygame.draw.rect(win, red, (0, 50, WIDTH, 150))

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text1 = font.render("Game over. Do you want to play again?", True, white)
        text1_rect = text1.get_rect()
        text1_rect.center = (WIDTH / 2, 75)
        win.blit(text1, text1_rect)

        text2 = font.render("Press \"Y\" for Yes, or \"N\" for No", True, white)
        text2_rect = text2.get_rect()
        text2_rect.center = (WIDTH / 2, 125)
        win.blit(text2, text2_rect)
    

    
    


    pygame.display.update()
    

    # check if player lose and stop the screen
    while gameover:
        
        clock.tick(fps)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameover = False
                run = False
                
            # get the user's input (y or n)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    # reset the game
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == pygame.K_n:
                    # exit the loops
                    gameover = False
                    run = False
                

        
# quit game
pygame.quit()