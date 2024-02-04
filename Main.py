# Librerias a instalar

# Uso de funciones de teclado, mouse y pantalla
# pip install pyautogui

# Modulo para trabajar con funciones de la pantalla
# pip install Pillow

# Importamos modulo para trabajar con funciones del sistema
#import pyautogui

# Tomamos una captura de pantalla almacenada en la ruta dada
#pyautogui.screenshot(r"C:\Users\edgar\Downloads\screenshot1.png")

import pyautogui
import time

def mostrar_pato_8bit():
    # Definir la representación del pato en 8 bits
    patito_8bit = """

  ╱|、
(˚ˎ 。7  
 |、˜〵          
じしˍ,)ノ

    """

    # Esperar unos segundos antes de mostrar el pato
    time.sleep(3)

    # Crear una imagen temporal del pato
    # pyautogui.screenshot('pato_8bit.png')

    # Abrir la imagen con PyAutoGUI
    pyautogui.alert(text=patito_8bit, title='Pato en 8 bits', button='UWU')

    # Eliminar la imagen temporal
    # pyautogui.screenshot('pato_8bit.png').close()

# Esperar unos segundos antes de mostrar el pato
time.sleep(3)

# Mostrar el pato en 8 bits utilizando PyAutoGUI
mostrar_pato_8bit()
