import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
input('Pressione ENTER para sair')
