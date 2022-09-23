import pygame
from random import randint
import pickle

pygame.init()

WIDTH = 600
HEIGHT = 400
FPS = 15

# setting windows
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Click Bait')
pygame.display.set_icon(pygame.image.load("assets/raj games icon.png"))

# setting counter
counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('digital', 30)

# setting color
win_color = 'grey'
trap_color = 'yellow'
bait_color = 'red'

# bait variables
bait_radius = 15
trap_radius = 20
trap_width = 2
margin = 20
score = 0


# getting high score
try:
    with open('HighScore.pkl', 'rb') as f:
        high_score = pickle.load(f)
except :
    high_score = 0

# game variables
quited = False
playing = True
bait = [randint(margin, WIDTH - margin), randint(margin, HEIGHT - margin)]


def draw_circle(at):
    pygame.draw.circle(win, trap_color, at, trap_radius)
    pygame.draw.circle(win, win_color, at, trap_radius - trap_width)


def draw_baits(at):
    pygame.draw.circle(win, bait_color, at, bait_radius)


# game loop
while not quited:
    win.fill(pygame.Color(win_color))
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quited = True
        elif event.type == pygame.USEREVENT:
            counter -= 1
            if counter >= 1:
                text = str(counter).rjust(3)
            else:
                text = 'Game Over'
                playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            if playing:
                for i in range(bait[0] - bait_radius, bait[0] + bait_radius):
                    for j in range(bait[1] - bait_radius, bait[1] + bait_radius):
                        if i == click[0] and j == click[1]:
                            bait = [randint(margin, WIDTH - margin), randint(margin, HEIGHT - margin)]
                            score += 1
                draw_circle(click)
    if playing:
        draw_baits(bait)
    else:
        if score > high_score:
            win.blit(font.render("High Score " + str(score), True, (0, 125, 0)), (WIDTH // 2, HEIGHT // 2))
            high_score = score
        else:
            win.blit(font.render(f"score: {str(score)}  High Score {high_score}", True, (0, 125, 0)),
                     (WIDTH // 2, HEIGHT // 2))
    win.blit(font.render(text, True, (0, 0, 0)), (WIDTH // 2, 20))
    clock.tick(FPS)
    pygame.display.flip()

# saving high score
try:
    with open('HighScore.pkl', 'wb') as f:
        pickle.dump(high_score, f)
except :
    pass

pygame.quit()
