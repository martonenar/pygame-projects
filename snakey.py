import pygame, sys, random, time

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Snake")
running = True
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 70)

score = 0
y_change, x_change = 0, 15
snake_y, snake_x = 350, 500
apple_x, apple_y = 500, 100
part_y = 30
running2 = False
running3 = False

coord_list = [(snake_x, snake_y), (snake_x, snake_y - part_y), (snake_x, snake_y - part_y * 2)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        x_change = 0
        y_change = -15
    elif keys[pygame.K_s]:
        x_change = 0
        y_change = 15
    elif keys[pygame.K_a]:
        x_change = -15
        y_change = 0
    elif keys[pygame.K_d]:
        x_change = 15
        y_change = 0

    current_head_x, current_head_y = coord_list[0]
    new_head_x = current_head_x + x_change
    new_head_y = current_head_y + y_change

    if new_head_x < 0:
        new_head_x = 1000 - 30
    elif new_head_x >= 1000:
        new_head_x = 0

    if new_head_y < 0:
        new_head_y = 700 - 30
    elif new_head_y >= 700:
        new_head_y = 0

    new_head = (new_head_x, new_head_y)
    coord_list.insert(0, new_head)

    if coord_list[0] in coord_list[1:]:
        running = False
        running3 = True
        break
    elif score > 30:
        running = False
        running2 = True
        running3 = True
        break

    snake_head_hitbox = pygame.Rect(coord_list[0][0], coord_list[0][1], 30, 30)
    apple_hitbox = pygame.Rect(apple_x-15, apple_y-15, 30, 30)

    if snake_head_hitbox.colliderect(apple_hitbox):
        score += 1
        apple_x, apple_y = random.randint(15, 985), random.randint(15, 685)
    else:
        coord_list.pop()

    text_surface = font.render(f'{score} apples', True, (255, 255, 255))

    screen.fill((26, 45, 30))
    apple = pygame.draw.circle(screen, (234, 67, 53), (apple_x, apple_y), 15)
    for part in coord_list:
        pygame.draw.rect(screen, (70, 130, 240), pygame.Rect(part[0], part[1], 30, 30))
    screen.blit(text_surface, (350, 0))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)

screen.fill((26, 45, 30))
while running3:
    if not running2:
        text_surface = font.render(f'You lost, {score} apple/s eaten', True, (255, 255, 255))
        screen.blit(text_surface, (75, 0))
        pygame.display.update()
        time.sleep(5)

    if running2:
        text_surface = font.render(f'You won, {score} apple/s eaten', True, (255, 255, 255))
        screen.blit(text_surface, (75, 0))
        pygame.display.update()
        time.sleep(5)

    running3 = False
pygame.quit()
sys.exit()