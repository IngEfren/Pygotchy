import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
width, height = 200, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('UwU')

# Definir colores
white = (255, 255, 255)

# Cargar imagen del pato
duck_image = pygame.image.load('egg.png')  # Asegúrate de tener una imagen llamada 'duck.png' en el mismo directorio

duck_image = pygame.transform.scale(duck_image, (150, 150))

# Obtener el rectángulo de la imagen
duck_rect = duck_image.get_rect()

# Posición inicial del pato en la pantalla
duck_rect.x = width // 2 - duck_rect.width // 2
duck_rect.y = height // 2 - duck_rect.height // 2

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar pantalla
    screen.fill(white)

    # Dibujar el pato en la pantalla
    screen.blit(duck_image, duck_rect)

    # Actualizar pantalla
    pygame.display.flip()

    time.sleep(5)

    # Cargar imagen del pato
    # duck_image = pygame.image.load('egg4.png')  # Asegúrate de tener una imagen llamada 'duck.png' en el mismo directorio

    # duck_image = pygame.transform.scale(duck_image, (150, 150))

# Salir del programa
pygame.quit()
