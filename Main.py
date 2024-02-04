# Librerias a instalar

# Uso de funciones de teclado, mouse y pantalla
# pip install pyautogui

# Modulo para trabajar con funciones de la pantalla
# pip install Pillow

import pygame
import sys
import random

draw1 = (
    (0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0),
    (0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0),
    (0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0),
    (0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0),
    (0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0),
    (0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0),
    (0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0),
    (0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0),
    (0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0),
    (0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0),
    (0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0),
    (0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0),
    (0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0),
    (0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0),
    (0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0),
    (0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0),
    (0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0)
)

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla y tamaño de cada celda
width, height = 320, 340
cell_size = 20

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
# Titulo de la pestaña
pygame.display.set_caption('Thamhaghotchii UwU')

# Generar matriz de colores aleatorios
#color = [[random.choice(colors) for _ in range(16)] for _ in range(16)]

# Generamos un color
color1 = (0, 0, 255)
color2 = (0, 255, 0)

# Creamos una funcio para dibujar con pixeles
def drawPixel(draw):
    # Recorremos el arreglo de lineas de valores del dibujo
    for i in range(len(draw)):
        # Recorremos el arreglo de columnas de valores del dibujo
        for j in range(len(draw[i])):
            # Si tenemos un valor de 1...
            if  ((draw[i][j]) == 1):
                # Dibujamos un rectangulo
                pygame.draw.rect(screen, color2, (j*cell_size, i*cell_size, cell_size, cell_size))

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    drawPixel(draw1)

    #pygame.draw.rect(screen, color1, (cell_size*0, cell_size*1, cell_size, cell_size))
    #pygame.draw.rect(screen, color2, (cell_size, cell_size, cell_size, cell_size))

    # Dibujar la matriz de colores en la pantalla
    #for row in range(16):
    #    for col in range(16):
    #        pygame.draw.rect(screen, color[row][col], (col * cell_size, row * cell_size, cell_size, cell_size))

    # Actualizar pantalla
    pygame.display.flip()

# Salir del programa
pygame.quit()
