import pygame

pygame.init()

WIDTH, HEIGHT = 800,600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Ping-Pong')
font = pygame.font.Font(None,100)

paddle_width, paddle_height = 10,100
ball_radius = 10
score1, score2 = 0,0
max_score = 10
paddle1 = pygame.Rect(30,(HEIGHT-paddle_height)//2,paddle_width,paddle_height)
paddle2 = pygame.Rect(WIDTH - 40,(HEIGHT-paddle_height)//2,paddle_width,paddle_height)

paddle_speed = 7

game_over = False

ball_x,ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x,ball_speed_y = 5,5

def goal(player1):
    global ball_x, ball_y, ball_speed_x,score1,score2
    if player1:
        score1 += 1
    else:
        score2 += 1
    reset_game()


running = True

def finish_game():
    global game_over
    if score1 == max_score:
        winner = 'Player 1'
    elif score2 == max_score:
        winner = 'Player 2'
    else:
        return False
        
    print(winner)
    winner_text = font.render(f'Game Over',True, (255,255,255))
    winner_text2 = font.render(f'{winner} wins!',True, (255,255,255))

    screen.blit(winner_text,(WIDTH//2 - winner_text.get_width() // 2,HEIGHT//2 - winner_text.get_height() // 2 - 60))
    screen.blit(winner_text2,(WIDTH//2 - winner_text.get_width() // 2 - 40,HEIGHT//2 - winner_text.get_height() // 2))
    pygame.display.flip()
    game_over = True
    return True

def reset_game():
    global score1,score2,ball_x,ball_y,ball_speed_x,ball_speed_y,paddle1,paddle2,game_over

    if game_over: 
        score1,score2 = 0,0 
        game_over = False


    ball_x,ball_y = WIDTH // 2, HEIGHT // 2
    paddle1 = pygame.Rect(30,(HEIGHT-paddle_height)//2,paddle_width,paddle_height)
    paddle2 = pygame.Rect(WIDTH - 40,(HEIGHT-paddle_height)//2,paddle_width,paddle_height)


    
def draw_score():
    score_text = font.render(f'{score1}:{score2}',True, (255,255,255))
    screen.blit(score_text,(WIDTH//2 - score_text.get_width() //2,50))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            reset_game()

    if game_over:
        continue

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_w] and paddle1.top > 0):
        paddle1.move_ip(0,-paddle_speed)
    if(keys[pygame.K_s] and paddle1.bottom < HEIGHT):
        paddle1.move_ip(0,paddle_speed)

    if(keys[pygame.K_UP] and paddle2.top > 0):
        paddle2.move_ip(0,-paddle_speed)
    if(keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT):
        paddle2.move_ip(0,paddle_speed)

 
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y *= -1
    
    if ball_x + ball_radius >= WIDTH:
        goal(True)
    if ball_x - ball_radius <= 0:
        goal(False)


    if paddle1.collidepoint(ball_x - ball_radius,ball_y):
        ball_speed_x *= -1
    if paddle2.collidepoint(ball_x + ball_radius,ball_y):
        ball_speed_x *= -1


    # todo доробити логіку гри: таймер
    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,255,255),paddle1)
    pygame.draw.rect(screen,(255,255,255),paddle2)
    pygame.draw.circle(screen,(255,255,255),(ball_x,ball_y),ball_radius)
    draw_score()
    if finish_game(): 
        continue



    pygame.display.flip()

    pygame.time.Clock().tick(60)
