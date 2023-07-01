import pyautogui

def find_image(image_path, confidence=0.7):
    while True:
        position = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if position is not None:
            x, y, width, height = position
            center_x = x + width / 2
            center_y = y + height / 2
            return int(center_x), int(center_y)

# Exemplo de uso
while True:
    try:
        x, y = find_image('fearow.png')
        print(f'Imagem encontrada nas coordenadas: ({x}, {y})')
    except TypeError:
        print('Imagem não encontrada na tela.')
        continue
    break
