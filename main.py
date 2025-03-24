import pygame

pygame.init()

WIDTH, HEIGHT = 800,600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Ping-Pong')

paddle_width, paddle_height = 10,100
ball_radius = 10

paddle1 = pygame.Rect(30,(HEIGHT-paddle_height)//2,paddle_width,paddle_height)
paddle2 = pygame.Rect(WIDTH - 40,(HEIGHT-paddle_height)//2,paddle_width,paddle_height)

paddle_speed = 7

ball_x,ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x,ball_speed_y = 5,5


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_w] and paddle1.top > 0):
        paddle1.move_ip(0,-paddle_speed)
    if(keys[pygame.K_s] and paddle1.bottom < HEIGHT):
        paddle1.move_ip(0,paddle_speed)

    # Todo доробити другу палетку

    
    ball_x -= ball_speed_x
    ball_y -= ball_speed_y

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y *= -1


      # Todo доробити другу палетку
    if paddle1.collidepoint(ball_x - ball_radius,ball_y):
        ball_speed_x *= -1


    # todo доробити логіку гри: разхунок, холи, можливо таймер
    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,255,255),paddle1)
    pygame.draw.rect(screen,(255,255,255),paddle2)
    pygame.draw.circle(screen,(255,255,255),(ball_x,ball_y),ball_radius)



    pygame.display.flip()

    pygame.time.Clock().tick(60)
