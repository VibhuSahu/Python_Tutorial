import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("first Game")

x = 50
y = 450
width = 40
height = 60
vel = 5


isJump = False
jumpcount = 10


run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            isJump = False
            jumpcount = 10



    win.fill((0,0,0))

    pygame.draw.rect(win, (255, 0, 0), (x, y ,width, height))
    pygame.display.update()


pygame.quit()