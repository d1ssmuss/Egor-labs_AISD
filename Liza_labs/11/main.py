import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 1366, 800
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аналоговые часы")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def numbers(number, size, position):
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(number, True, WHITE)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, - (y - HEIGHT / 2)


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        day = current_time.day
        month = current_time.month
        year = current_time.year
        weekday = current_time.today().isoweekday()
        calendar = current_time.today().isocalendar()

        weekdays_abbr = {1: "Пн", 2: "Вт", 3: "Ср", 4: "Чт", 5: "Пт", 6: "Сб", 7: "Вск"}
        weekday_abbr = weekdays_abbr.get(weekday)

        months_abbr = {1: "Янв", 2: "Февр", 3: "Март", 4: "Апр", 5: "Май", 6: "Июнь", 7: "Июль",
                       8: "Авг", 9: "Сент", 10: "Окт", 11: "Нояб", 12: "Дек"}
        month_abbr = months_abbr.get(month)

        if day < 10:
            day = "0" + str(day)

        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, center, clock_radius - 10, 10)
        pygame.draw.circle(screen, WHITE, center, 12)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 260, HEIGHT / 2 - 30, 80, 60], 1)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 180, HEIGHT / 2 - 30, 80, 60], 1)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 100, HEIGHT / 2 - 30, 80, 60], 1)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 180, HEIGHT / 2 - 30, 80, 60], 1)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 50, HEIGHT / 2 - 30 + 160, 100, 60], 1)

        numbers(str(weekday_abbr), 40, (WIDTH / 2 - 220, HEIGHT / 2))
        numbers(str(calendar[1]), 40, (WIDTH / 2 - 140, HEIGHT / 2))
        numbers(str(month_abbr), 40, (WIDTH / 2 + 140, HEIGHT / 2))
        numbers(str(day), 40, (WIDTH / 2 + 220, HEIGHT / 2))
        numbers(str(year), 40, (WIDTH / 2, HEIGHT / 2 + 160))

        for number in range(1, 13):
            numbers(str(number), 80, polar_to_cartesian(clock_radius - 80, number * 30))

        for number in range(0, 360, 6):
            if number % 5:
                pygame.draw.line(screen, WHITE, polar_to_cartesian(clock_radius - 15, number),
                                 polar_to_cartesian(clock_radius - 30, number), 2)
            else:
                pygame.draw.line(screen, WHITE, polar_to_cartesian(clock_radius - 15, number),
                                 polar_to_cartesian(clock_radius - 35, number), 6)

        # Часов
        r = 250
        theta = (hour + minute / 60 + second / 3600) * (360 / 12)
        pygame.draw.line(screen, WHITE, center, polar_to_cartesian(r, theta), 14)

        # Минут
        r = 280
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, WHITE, center, polar_to_cartesian(r, theta), 10)

        # Секунд
        r = 340
        theta = second * (360 / 60)
        pygame.draw.line(screen, RED, center, polar_to_cartesian(r, theta), 4)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
main()
