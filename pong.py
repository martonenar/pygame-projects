import pygame, sys, time, random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
running = True
player_y = 300
ball_x = 400
ball_y = 300
ball_x_speed = 5
ball_y_speed = 5
player_score = 0
ai_score = 0
ai_y = 0
ai_y_speed = 8
pygame.font.init()
font = pygame.font.Font(None, 74)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.key.get_pressed()[pygame.K_w]:
        if player_y < 0:
            None
        else:
            player_y -= 8
    elif pygame.key.get_pressed()[pygame.K_s]:
        if player_y > 515:
            None
        else:
            player_y += 8

    if ball_x >= 788:
        ball_x_speed = 5
        ball_x, ball_y = 400, 300
        player_score += 1
    elif ball_x <= 12:
        ball_x_speed = 5
        ball_x, ball_y = 400, 300
        ai_score += 1
    elif ball_y <= 12:
        ball_y_speed = abs(ball_y_speed)
    elif ball_y >= 588:
        ball_y_speed = -abs(ball_y_speed)

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    if ball_y < ai_y:
        ai_y -= ai_y_speed
    elif ball_y > ai_y:
        ai_y += ai_y_speed

    screen.fill(pygame.Color("black"))
    ball = pygame.draw.circle(screen, pygame.Color("white"), (ball_x, ball_y), 12)
    paddle = pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(0, player_y, 15, 85), 10)
    ai_paddle = pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(785, ai_y, 15, 85), 10)
    ball_rect = pygame.Rect(ball_x - 12, ball_y - 12, 24, 24)
    score_surface = font.render(f"{player_score} : {ai_score}", True, pygame.Color("white"))
    screen.blit(score_surface, (400 - score_surface.get_width() // 2, 20))

    previous_ball_y = ball_y
    previous_player_y = player_y
    previous_ai_y = ai_y

    if paddle.colliderect(ball_rect):
        if previous_player_y < ball_y < previous_player_y + 85:
            ball_x_speed = abs(ball_x_speed) + 2
            ball_y_speed += 2
            ball_x = paddle.right + 12
        else:
            ball_x_speed = abs(ball_x_speed)
            ball_x = paddle.right + 12
    elif ai_paddle.colliderect(ball_rect):
        if previous_ai_y < ball_y < previous_ai_y + 85:
            ball_x_speed = -abs(ball_x_speed)
            ball_x = ai_paddle.left - 12
        else:
            ball_x_speed = -abs(ball_x_speed)
            ball_x = ai_paddle.left - 12

    previous_ball_y = ball_y
    previous_player_y = player_y
    previous_ai_y = ai_y
    if player_score == 10:
        running = False
    elif ai_score == 10:
        running = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
if player_score == 10:
    surface = font.render("YOU WON!!!!!", True, pygame.Color("white"))
    screen.fill(pygame.Color("black"))
    screen.blit(surface, (400 - surface.get_width() // 2, 20))
    pygame.display.update()
    pygame.display.flip()
    time.sleep(5)
elif ai_score == 10:
    surface = font.render("YOU LOSE!!!", True, pygame.Color("white"))
    screen.fill(pygame.Color("black"))
    screen.blit(surface, (400 - surface.get_width() // 2, 20))
    pygame.display.update()
    pygame.display.flip()
    time.sleep(5)
pygame.quit()
sys.exit()
