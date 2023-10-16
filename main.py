import pygame, sys, random
from liikuvad_värgendused import *
pygame.init()

# EKRAANI SEADISTUS
ekraan = pygame.display.set_mode([1300, 900])
pygame.display.set_caption("Ping Pong 2.0")



# MÄNGIJATE SEADISTUS
mängija1 = player1(20, ekraan.get_height() / 2 - 45)
mängija2 = player2(ekraan.get_width() - 40, ekraan.get_height() / 2 - 45)

def mängijad():
    pygame.draw.rect(ekraan, [255, 255, 255], [mängija1.x, mängija1.y, 20, 100], 0)
    pygame.draw.rect(ekraan, [180, 180, 180], [mängija1.x - 2, mängija1.y - 2, 22, 102], 3)

    pygame.draw.rect(ekraan, [255, 255, 255], [mängija2.x, mängija2.y, 20, 100], 0)
    pygame.draw.rect(ekraan, [180, 180, 180], [mängija2.x - 2, mängija2.y - 2, 22, 102], 3)

def main():
    pall = ball(ekraan.get_width() / 2 - 7, ekraan.get_height() / 2, 1.5)
    pall_x_suurendus = random.randint(-10, 10) / 10 * pall.kiirus
    pall_y_suurendus = random.randint(-10, 10) / 10 * pall.kiirus
    p2y = 0
    p1y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    p1y = -1
                if event.key == pygame.K_s:
                    p1y = 1
                if event.key == pygame.K_UP:
                    p2y = -1
                if event.key == pygame.K_DOWN:
                    p2y = 1
            elif event.type == pygame.KEYUP:
                p2y = 0
                p1y = 0
        if 2 <= mängija2.y <= 799:
            mängija2.y += p2y
        else:
            if mängija2.y > 500:
                mängija2.y -= 1
            else:
                mängija2.y += 1

        if 2 <= mängija1.y <= 799:
            mängija1.y += p1y
        else:
            if mängija1.y > 500:
                mängija1.y -= 1
            else:
                mängija1.y += 1
        ekraan.fill([0, 0, 0])
        for i in range(ekraan.get_height()):
            if i % 137 == 0 or i == 0:
                pygame.draw.rect(ekraan, [255, 255, 255], [ekraan.get_width() / 2, i, 30, 75], 0)
                pygame.draw.rect(ekraan, [160, 160, 160], [ekraan.get_width() / 2, i, 30, 75], 3)

        mängijad()
        pygame.draw.circle(ekraan, [255, 255, 255], [pall.x, pall.y], 14, 0)
        pygame.draw.circle(ekraan, [180, 180, 180], [pall.x, pall.y], 14, 3)
        pall.x += pall_x_suurendus
        pall.y += pall_y_suurendus
        if pall.y <= 1 or pall.y >= 895:
            pall_y_suurendus *= -1
        if (int(pall.x) in range(int(mängija1.x), int(mängija1.x + 30)) and int(pall.y) in range(int(mängija1.y), int(mängija1.y) + 100)) or (int(pall.x) in range(int(mängija2.x), int(mängija2.x + 40)) and int(pall.y) in range(int(mängija2.y), int(mängija2.y) + 100)):
            pall_x_suurendus *= -1
        pygame.display.flip()
        print(pall.kiirus)
main()
