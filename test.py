import pygame

pygame.init()

# Screen size
screen = pygame.display.set_mode((900,400))
# Player
player1 = pygame.image.load('pygame/newcar1.png')
X1, Y1 = 50, 50
player2 = pygame.image.load('pygame/newcar2.png')
X2, Y2 = 50, 150


def player(player, point):
    screen.blit(player, point)

running = True
while running:

    # RGB = R,G,B
    screen.fill((255,0,0))

    # X1 +=0.1
    # print()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                # X1 += 5
                print('Left press')
            if event.type == pygame.K_RIGHT:
                print('Right press')
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                print('Key release')

    player(player1, (X1,Y1))
    player(player2, (X2,Y2))
    pygame.display.update()