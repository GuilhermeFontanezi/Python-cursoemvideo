import pygame
import time
print('O ESTOURO DE FOGOS VAI COMEÇAR EM 10 SEGUNDOS, VAMOS ACOMPANHAR A CONTAGEM REGRESSIVA ')
for c in range(1, 11):
    print('{}...'.format(c))
    time.sleep(1)
pygame.init()
pygame.mixer.music.load('ex46.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
