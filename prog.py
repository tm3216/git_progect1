import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')
    try:
        w = int(input())
        n = int(input())
    except ValueError:
        print("Неправильный формат ввода")
        return -1
    screen = pygame.display.set_mode((n * 2 * w, n * 2 *w))
    draw(screen, w, n)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def draw(screen, w, n):
    color = 'red'
    for i in range(w * n, w, -w):
        pygame.draw.circle(screen, color, (n * w, n * w), i)
        if color == 'red':
            color = 'blue'
        elif color == 'blue':
            color = 'green'
        else:
            color = 'red'


if __name__ == '__main__':
    sys.exit(main())