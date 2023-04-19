import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Wolf Asylum - Psyche - Adaption Mix.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): #o loop verifica se o canal da musica ainda esta ativo
    continue

#encerrando o programa
pygame.quit()