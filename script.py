import win32gui
import time
import pytesseract
import cv2
import mss
import numpy
import json
import mypokeweakness


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

isPlaying = ''
isFighting = ''

# get toutes les fenêtres ouvertes
def callback(hwnd, window_list):
    window_list.append((hwnd, win32gui.GetWindowText(hwnd)))

# return la fenêtre Minecraft si elle est ouverte
def find_minecraft_window():
    window_list = []
    win32gui.EnumWindows(callback, window_list)
    for hwnd, window_title in window_list:
        if "Minecraft" in window_title:
            return hwnd
    return None

# return True si Minecraft et la fenêtre principale de l'ordinateur
def is_minecraft_active():
    minecraft_hwnd = find_minecraft_window()
    if not minecraft_hwnd:
        return False
    active_hwnd = win32gui.GetForegroundWindow()
    return minecraft_hwnd == active_hwnd


minecraft_hwnd = find_minecraft_window()

#
# def printIsOpenActive():
#     while True:
#         time.sleep(1)
#         if minecraft_hwnd:
#             print("Minecraft est ouvert")
#         else:
#             print("Minecraft n'est pas ouvert")
#
#         if is_minecraft_active():
#             print("Minecraft est la fenêtre active")
#         else:
#             print("Minecraft n'est pas la fenêtre active")

# bon bah ça parait clair
def isMinecraftOpenAndActive():
    if minecraft_hwnd and is_minecraft_active():
        return True
    else:
        return False

# utilise mss pour record l'écran
def CaptureScreen():
    pokeName = 'None'
    with mss.mss() as sct:
        # dimensions de la capture
        monitor = {'top': 40, 'left': 228, 'width': 250, 'height': 46}


        while 'Screen capturing':
            # last_time = time.time()

            # Get le record en pixel, le stock en Numpy array
            img = numpy.array(sct.grab(monitor))

            # Display le rectangle enregistré
            # cv2.imshow('OpenCV/Numpy normal', img)

            # Display en nuances de gris
            cv2.imshow('OpenCV/Numpy grayscale',
                       cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            # Appelle Tesseract pour convertir l'image analysé en string
            text = pytesseract.image_to_string(img)


            if text != pokeName:

                # print('fps: {0}'.format(1 / (time.time()-last_time)))
                time.sleep(1)
                if text == "":
                    print("l'utilisateur n'est pas en combat")
                    break
                print('Le programme détecte : ' + text)
                # print(mypokeweakness.replaceLetterE(text))

                # j'ouvre le fichier json, si le texte analysé correspond à un pokémon trouvé, le log
                with open('pokedex.json', 'r', encoding="utf8") as json_file:
                    json_object = json.load(json_file)
                    # pokemonListName = []

                    for pokemon in json_object:
                        # print(pokemon['name']['english'])
                        # pokemonListName.append(pokemon['name']['english'])
                        # if pokemon['name']['english'] == text:
                        #     print('Vous affrontez : ' + text + ', Ce pokémon est de type :' + pokemon[type])

                        # print(pokemon['name']['english'])

                        if (pokemon['name']['french']  == text.lstrip().rstrip()) or (mypokeweakness.replaceLetterE(text.lstrip().rstrip()) == pokemon['name']['french']):
                            typeList = mypokeweakness.typeListToString(pokemon['type'])
                            print('Le texte analysé est reconnu en tant que : ' + pokemon['name']['french'] )
                            print('Ce pokémon est de type : ' + typeList + '\n')
                            mypokeweakness.findWeakness(typeList.lower().lstrip().rstrip())
                            print('\n')



                pokeName = text


            # Press "q" to quit
            # if cv2.waitKey(25) & 0xFF == ord('q'):
            #     cv2.destroyAllWindows()
            #     break

while True:
    time.sleep(1)
    if isMinecraftOpenAndActive():
        isPlaying = True
        CaptureScreen()

    elif not isPlaying:
        print("l'utilisateur n'est pas sur le jeu")
        isPlaying = False
        # print(isPlaying)





