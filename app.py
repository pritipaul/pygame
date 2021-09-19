import pygame
import random 
import os

pygame.mixer.init()
x = pygame.init()

# game screen display
screen_width = 1000
screen_hight = 500
gameWindow = pygame.display.set_mode((screen_width,screen_hight))

pygame.display.set_caption("Snakegame made by Priti Paul")
pygame.display.update()
# clock for game window loading
clock = pygame.time.Clock()
# color
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
light_blue = (168,288,238)
# image 
welcome_img = pygame.image.load("welcom.jpg")
welcome_img = pygame.transform.scale(welcome_img,(screen_width,screen_hight)).convert_alpha()
back_img = pygame.image.load("background.jpg")
back_img = pygame.transform.scale(back_img,(screen_width,screen_hight)).convert_alpha()
over_img = pygame.image.load("over.jpg")
over_img = pygame.transform.scale(over_img,(screen_width,screen_hight)).convert_alpha()

# score 
font = pygame.font.SysFont(None,55)
def score_text(text,color,x,y):
    screen_text =  font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

# for snake height width
snake_size = 10
def snake_plot(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow , green , [x,y,snake_size,snake_size])
    

# welcome page 
def welcome():
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()   
    exit_game = False
    game_over = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(welcome_img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play() 
                    game_loop()    

        pygame.display.update()
        clock.tick(60)


# gaming loop
def game_loop():
    exit_game = False
    game_over = False
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_hight/2)
    food_a = random.randint(20,screen_width/2)
    food_b = random.randint(20,screen_hight/2)
    snake_x = 45
    snake_y = 55
    snake_size = 30
    snake_list = []
    snake_length = 1
    velocity_x = 0
    velocity_y = 0
    fps = 60
    score = 0
    init_velocity = 5
    # when highsore file is not exist so it is create a new file
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        # highest scoreing 
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            # create a background
            gameWindow.blit(over_img,(0,0))
            score_text("score: "+ str(score) , red,5,5)
        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("welcome.mp3")
                        pygame.mixer.music.play()
                        welcome()    

        else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = + init_velocity
                            velocity_y = 0  
                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0  
                        if event.key == pygame.K_UP:
                            velocity_y = -init_velocity
                            velocity_x = 0   
                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0   
                        # cheating code    
                        if event.key == pygame.K_q:
                            score += 3                
                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y
                if abs(snake_x - food_x)<25 and abs(snake_y - food_y)<25:
                    score +=10
                    food_x = random.randint(20,screen_width/2)
                    food_y = random.randint(20,screen_hight/2)
                    snake_length += 2
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play() 
                gameWindow.fill(white)
                gameWindow.blit(back_img,(0,0))
                score_text("score: "+ str(score), red,5,5)
                pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snake_list.append(head)
                if len(snake_list)>snake_length:
                    del snake_list[0]
                if head in snake_list[:-1]:
                    game_over = True 
                    pygame.mixer.music.load("over.mp3")
                    pygame.mixer.music.play() 
                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hight:
                    game_over = True   
                    pygame.mixer.music.load("over.mp3")
                    pygame.mixer.music.play()    
                snake_plot(gameWindow,green,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
 
