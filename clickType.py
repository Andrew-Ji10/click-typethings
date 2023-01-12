import mouse, time, keyboard
print("hello world")

webbar = (511, 62)
pageLoc = (793, 170)
chromeloc = (446, 1049)
defaultProfileLoc = (735, 434)
fullscreenLoc = (1842, 17)

#goes to a website in a chrome tab
def goToWebsite(website):
    mouse.release()
    mouse.move(webbar[0], webbar[1])
    mouse.click()
    keyboard.write(website)
    #time.sleep(3)
    keyboard.press('enter')

#creates a new tab in an already opened chrome window
def newTab():
    mouse.release()
    mouse.move(pageLoc[0], pageLoc[1])
    mouse.click()
    print("creating tab")
    #time.sleep(2)
    keyboard.press_and_release('ctrl+t')

def newWindow():
    mouse.release()
    mouse.move(chromeloc[0], chromeloc[1])
    mouse.click()
    print("creating window")
    time.sleep(0.5)
    mouse.move(defaultProfileLoc[0], defaultProfileLoc[1])
    mouse.click()
    print("going fullscreen")
    time.sleep(0.5)
    mouse.move(fullscreenLoc[0], fullscreenLoc[1])
    mouse.click()
