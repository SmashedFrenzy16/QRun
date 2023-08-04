import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
S_WIDTH = 450
S_HEIGHT = 300

score = 0

# Player variables
square_x = 50
square_y = 230
change_x = 0
change_y = 0

# Spikes variables
spikes = [300, 450, 600]
spikes_speed = 3
on = True

# World vairables
gravity = 1

screen = pygame.display.set_mode([S_WIDTH, S_HEIGHT])
pygame.display.set_caption("QRun")
backg = BLACK

fps = 60
font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()

game_run = True

while game_run:

    timer.tick(fps)

    screen.fill(backg)

    if not on:

        welcome_txt = font.render("Welcome to QRun! (Made by @SmashedFrenzy16)", True, WHITE, BLACK)
        screen.blit(welcome_txt, ((S_WIDTH / 2) - 200, 50))

        instruct_txt = font.render("Press `SPACE` to start!", True, WHITE, BLACK)
        screen.blit(instruct_txt, ((S_WIDTH / 2) - 200, 70))

        instruct_txt2 = font.render("CONTROLS:", True, WHITE, BLACK)
        screen.blit(instruct_txt2, ((S_WIDTH / 2) - 200, 90))

        instruct_txt2 = font.render("`SPACE`: Jump", True, WHITE, BLACK)
        screen.blit(instruct_txt2, ((S_WIDTH / 2) - 200, 110))

        instruct_txt2 = font.render("`LEFT`/`RIGHT`: Move left/right", True, WHITE, BLACK)
        screen.blit(instruct_txt2, ((S_WIDTH / 2) - 200, 130))

    score_txt = font.render(f"Score: {score}", True, WHITE, BLACK)
    screen.blit(score_txt, ((S_WIDTH / 2) - 25, 10))

    floor = pygame.draw.rect(screen, WHITE, [0, 250, S_WIDTH, 50])

    square = pygame.draw.rect(screen, [0, 240, 254], [square_x, square_y, 20, 20])

    spike1 = pygame.draw.rect(screen, RED, [spikes[0], 230, 20, 20])
    spike2 = pygame.draw.rect(screen, GREEN, [spikes[1], 230, 20, 20])
    spike3 = pygame.draw.rect(screen, BLUE, [spikes[2], 230, 20, 20])

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_run = False

        if event.type == pygame.KEYDOWN and not on:

            if event.key == pygame.K_SPACE:

                spikes = [300, 450, 600]

                square_x = 50

                score = 0

                on = True

        if event.type == pygame.KEYDOWN and on == True:

            if event.key == pygame.K_SPACE and change_y == 0:

                change_y = 14

            if event.key == pygame.K_RIGHT:

                change_x = 3

            if event.key == pygame.K_LEFT:

                change_x = -3

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:

                change_x = 0

            if event.key == pygame.K_LEFT:

                change_x = 0

    for i in range(len(spikes)):

        if on:

            spikes[i] -= spikes_speed

            if spikes[i] <= -20:

                spikes[i] = random.randint(480, 570)

                score += 2

            if square.colliderect(spike1) or square.colliderect(spike2) or square.colliderect(spike3):

                on = False

    if 0 <= square_x <= 430:

        square_x += change_x
    
    if square_x < 0:

        square_x = 0

    if square_x > 430:

        square_x = 430

    if change_y > 0 or square_y < 230:

        square_y -= change_y

        change_y -= gravity

    if square_y > 230:

        square_y = 230

    if square_y == 230 and change_y < 0:

        change_y = 0

    pygame.display.flip()

pygame.quit()


