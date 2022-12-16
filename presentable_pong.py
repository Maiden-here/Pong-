import pygame, sys, random
from button import Button

#initializing pygame and creatinf fps clock
pygame.init()
clock = pygame.time.Clock()


#The Screen
screenWidth = 1000
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pong -- By Rudra")
icon_img = pygame.image.load("E:\Projects\pong/assests/bitmap.png")
pygame.display.set_icon(icon_img)

#Global Vars
game_state = "paused"
ball_speed_x = 7 * random.choice((-1,1))
ball_speed_y = 7 * random.choice((-1,1))
player_speed_y = 0
player_speed_y2 = 0
timer = 180
score1 = 0
score2 = 0
winner = "No One"
font = pygame.font.SysFont('broadway',50)
ball = pygame.Rect((screenWidth/2)-15,(screenHeight/2-15),30,30)
paddle1 = pygame.Rect((screenWidth/2-10)-480,(screenHeight/2-60),10,140)
play_button = Button(screen,200,100,(400,250),text = "PLAY",top_color=(255,255,255))
hit_sound = pygame.mixer.Sound("E:\Projects\pong/assests/hit.mp3")
#scored_sound = pygame.mixer.Sound("Assests/scored.mp3")
paddle2 = pygame.Rect((screenWidth/2-10)+490,(screenHeight/2-60),10,140)
rect_color = (200,200,200)
screen_color = (50,50,50)

#funcs
def bounceX():
    global ball,ball_speed_x,ball_speed_y,timer,screenWidth,screenHeight,score1,score2
    if ball.right >= screenWidth:
        ball.center = ((screenWidth/2),(screenHeight/2))
        timer = 180
        ball_speed_y = 7 * random.choice((-1,1))
        score1 += 1
        #scored_sound.play()
    if ball.left <= 0:
        ball.center = ((screenWidth/2),(screenHeight/2))
        ball_speed_x = 7 * random.choice((-1,1))
        ball_speed_y = 7 * random.choice((-1,1))
        timer = 180
        #scored_sound.play()
        score2 += 1

    return score2,score1
def bounceY():
    global ball,ball_speed_y
    if ball.bottom >= screenHeight or ball.top <= 0:
        ball_speed_y *= -1
        hit_sound.play()
def welcomeScreen():
    global screen,rect_color,font,game_state
    if game_state == "paused":
        welcomeScreenPNG = pygame.image.load("E:\Projects\pong/assests/welcomescre.png")
        play_button.draw_button()
        if play_button.button_pressed == True:
            game_state = "playing"

        #drawing on screen
        screen.blit(welcomeScreenPNG,(0,0))
def bouncePaddle():
    if paddle1.bottom >= screenHeight-5:
        paddle1.bottom = screenHeight-5
    if paddle1.top<= 5:
        paddle1.top = 5
    if paddle2.bottom >= screenHeight-5:
        paddle2.bottom = screenHeight-5
    if paddle2.top <= 5:
        paddle2.top = 5
def checkCollision():
    global ball, paddle1,paddle2,ball_speed_x
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
        hit_sound.play()
def playingGame():
    global ball,screen,font,game_state

    if game_state == "playing":       
        bounceX()
        bounceY()    
        bouncePaddle()
        checkCollision() 

        text = f"Score: {score1}:{score2}"     
        score_dis = font.render(text,True,rect_color)
        dis_rect = score_dis.get_rect(center = (screenWidth/2,50))
                  
        #drawing on screen
        pygame.draw.rect(screen,rect_color,paddle1)
        pygame.draw.rect(screen,rect_color,paddle2)
        pygame.draw.ellipse(screen,rect_color,ball)
        pygame.draw.aaline(screen,rect_color,(screenWidth/2,0),(screenWidth/2,screenHeight))
        screen.blit(score_dis,dis_rect)

        if score2 == 10:
            game_state = "gameOver"
        if score1 == 10:
            game_state = "gameOver"       
def gameOver():
    global screen,game_state,winner
    if game_state == "gameOver":
        if score1 == 10:
            winner = "Player 1"
            return winner
        if score2 == 10:
            winner = "Player 2"
            return winner
        text = f"{winner} Has Won The Match!"
        a = font.render(text,True,(255,255,255))
        a_rect = a.get_rect(center = (screenWidth/2,screenHeight/2))
        
        screen.blit(a,a_rect)
def resetEverything():
    global score1,score2,paddle2,paddle1
    score1 = 0 
    score2 = 0
    paddle1 = pygame.Rect((screenWidth/2-10)-480,(screenHeight/2-60),10,140)
    paddle2 = pygame.Rect((screenWidth/2-10)+490,(screenHeight/2-60),10,140)
#Game Loop
if __name__ == "__main__":
    while True:

        screen.fill(screen_color)

        #key inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = "playing"
                if event.key == pygame.K_BACKSPACE:
                    game_state = "paused"
                    resetEverything()
                if event.key == pygame.K_s:
                        player_speed_y = 7
                if event.key == pygame.K_w:
                    player_speed_y = -7
                if event.key == pygame.K_PAGEDOWN:
                    player_speed_y2 = 7
                if event.key == pygame.K_PAGEUP:
                    player_speed_y2 = -7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    player_speed_y = 0
                if event.key == pygame.K_w:
                    player_speed_y = 0
                if event.key == pygame.K_PAGEDOWN:
                    player_speed_y2 = 0
                if event.key == pygame.K_PAGEUP:
                    player_speed_y2 = 0
                
        if game_state == "playing":
            paddle1.y += player_speed_y
            paddle2.y += player_speed_y2
            timer -= 1
        if timer <= 0:
            timer = 0
        if game_state == "playing" and timer == 0:
            ball.x += ball_speed_x
            ball.y += ball_speed_y
        if game_state == "gameOver":
            if score1 == 10:
                winner = "Player 1"
                
            if score2 == 10:
                winner = "Player 2"
            
            text = f"{winner} Has Won The Match!"
            a = font.render(text,True,(255,255,255))
            a_rect = a.get_rect(center = (screenWidth/2,screenHeight/2))
            game_over_screen = pygame.image.load("E:\Projects\pong/assests/GAME_OVER.png")
            screen.blit(game_over_screen,(0,0))
            screen.blit(a,a_rect)
            

        #Calling Funcs
        welcomeScreen()
        playingGame()
        gameOver()
        play_button.draw_button()
        
        #updating display
        pygame.display.flip()
        clock.tick(60)