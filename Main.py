# Librerias a instalar

# Uso de funciones de teclado, mouse y pantalla
# pip install pyautogui

# Modulo para trabajar con funciones de la pantalla
# pip install Pillow

import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla y tamaño de cada celda
width, height = 400, 400
cell_size = 50

# Definir colores
colors = [
    (255, 0, 0),   # Rojo
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Azul
    (255, 255, 0), # Amarillo
    (255, 0, 255), # Magenta
    (0, 255, 255)  # Cian
]

# Crear la pantalla
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Matriz de Colores')

# Generar matriz de colores aleatorios
matrix = [[random.choice(colors) for _ in range(16)] for _ in range(16)]

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar la matriz de colores en la pantalla
    for row in range(16):
        for col in range(16):
            pygame.draw.rect(screen, matrix[row][col], (col * cell_size, row * cell_size, cell_size, cell_size))

    # Actualizar pantalla
    pygame.display.flip()

# Salir del programa
pygame.quit()
