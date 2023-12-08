import keyboard
import time
import pyautogui

maximum = 54 # nombre de fichier à explorer 
time.sleep(5)

for i in range(maximum):
    time.sleep(0.2)
    pyautogui.moveTo (151, 139)
    pyautogui.rightClick()

    time.sleep(0.2)
    pyautogui.moveTo (223, 178)
    pyautogui.click()

    time.sleep(0.2)
    pyautogui.moveTo (111, 109)
    pyautogui.rightClick()

    time.sleep(0.2)
    pyautogui.moveTo (144, 126)
    pyautogui.click()

    time.sleep(2)
    pyautogui.moveTo (640, 100)
    pyautogui.click()
    pyautogui.typewrite('C:\Users\Jean-BaptistePERNEY\Documents\ECHO\DATA\raw_audio_afmt')
    pyautogui.press('enter') 

    time.sleep(2)
    pyautogui.moveTo (435, 230)
    pyautogui.click()

    for j in range(i):
        pyautogui.press('down') 

    time.sleep(2)
    pyautogui.moveTo (435, 230)
    pyautogui.click()
    pyautogui.press('enter') 

    time.sleep(2)
    pyautogui.moveTo (437, 214)
    pyautogui.click()
    pyautogui.press('enter') 

    time.sleep(2)
    pyautogui.moveTo (174, 141)
    pyautogui.click()

    time.sleep(2)
    pyautogui.doubleClick(168, 142)

    pyautogui.typewrite('soleil')

    time.sleep(1)
    pyautogui.moveTo (1011, 498)
    pyautogui.click()

    pyautogui.typewrite('soleil')
    pyautogui.press('enter') 

    time.sleep(1)
    pyautogui.moveTo (1876, 532)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo (839, 777)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo (860, 629)
    pyautogui.click()
    pyautogui.press('enter') 

    time.sleep(1)
    pyautogui.moveTo (828, 738)
    pyautogui.click()

while True:
    print("while true")
    try:
        buttonLocation = pyautogui.locateOnScreen(r'C:\Users\Jean-BaptistePERNEY\Pictures\Screenshots\Capture5.png', confidence=0.7)
        print("buttonlocation")

        if buttonLocation is not None:
            # Centre le clic sur l'image trouvée
            buttonCenter = pyautogui.center(buttonLocation)
            pyautogui.click(buttonCenter)
            break  # Sortir de la boucle une fois cliqué
        else:
            print("Le popup 'OK' n'a pas encore été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    time.sleep(2)  # Attente entre chaque recherche pour éviter une utilisation excessive du CPU

time.sleep(5)

end=False

try:
    buttonLocation = pyautogui.locateOnScreen(r'C:\Users\Jean-BaptistePERNEY\Pictures\Screenshots\Capture6.png', confidence=0.7)
    print("buttonlocation")

    if buttonLocation is not None:
        # Centre le clic sur l'image trouvée
        buttonCenter = pyautogui.center(buttonLocation)
        end=True
    
    else:
        print("Le popup 'OK' n'a pas encore été trouvé.")
        end=False
except Exception as e:
    print(f"Une erreur est survenue : {e}")

time.sleep(2)  

while(end==False):
    # Donner du temps pour placer la souris
    time.sleep(1)

    # Cliquez pour positionner le curseur
    pyautogui.moveTo (735, 387,duration=1) # Coordonnées à ajuster2
    pyautogui.click()
    pyautogui.press('home')

    # Maintenir Shift enfoncé
    pyautogui.hotkey('shiftleft', 'shiftright', 'end')  # Sélectionne le caractère suivant

    # Clic droit pour ouvrir un menu contextuel (ajuster la position si nécessaire)
    time.sleep(1)
    # Bouger la souris et cliquer (ajuster les coordonnées)
    pyautogui.moveTo (735, 387,duration=1) # Coordonnées à ajuster2
    time.sleep(1)
    pyautogui.rightClick()

    time.sleep(1)

    pyautogui.moveTo (954, 423,duration=1) # Coordonnées à ajuster4
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo (991, 461,duration=1) # Coordonnées à ajuster5
    pyautogui.click()

    time.sleep(1)

    pyautogui.moveTo (805, 445,duration=1) # Coordonnées à ajuster6
    pyautogui.click()
    time.sleep(2)

    while True:
        print("while true")
    
        try:
            buttonLocation = pyautogui.locateOnScreen(r'C:\Users\Jean-BaptistePERNEY\Pictures\Screenshots\Capture3.png', confidence=0.7)
            print("buttonlocation")

            if buttonLocation is not None:
                # Centre le clic sur l'image trouvée
                buttonCenter = pyautogui.center(buttonLocation)
                pyautogui.click(buttonCenter)
                break  # Sortir de la boucle une fois cliqué
            else:
                print("Le popup 'OK' n'a pas encore été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

        time.sleep(2)  # Attente entre chaque recherche pour éviter une utilisation excessive du CPU

    time.sleep(1)

    while True:
        print("while true")
    
        try:
            buttonLocation = pyautogui.locateOnScreen(r'C:\Users\Jean-BaptistePERNEY\Pictures\Screenshots\Capture4.png', confidence=0.7)
            print("buttonlocation")

            if buttonLocation is not None:
                # Centre le clic sur l'image trouvée
                buttonCenter = pyautogui.center(buttonLocation)
                pyautogui.click(buttonCenter)
                break  # Sortir de la boucle une fois cliqué
            else:
                print("Le popup 'OK' n'a pas encore été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

        time.sleep(2)  # Attente entre chaque recherche pour éviter une utilisation excessive du CPU

