import mouse, time, keyboard
print("hello world")

time.sleep(3)

#mouse.release()
#mouse.move(511, 62)
#mouse.click()
#keyboard.write("hello")
#keyboard.press('enter')

def goToWebsite(website):
    mouse.release()
    mouse.move(511, 62)
    mouse.click()
    keyboard.write(website)
    time.sleep(3)
    keyboard.press('enter')

def newTab():
    mouse.release()
    mouse.move(793, 170)
    mouse.click()
    print("here")
    time.sleep(2)
    keyboard.press_and_release('ctrl+t')

newTab()