import mouse, time, keyboard
print("hello world")

time.sleep(3)

print(mouse.get_position())

mouse.release()
mouse.move(511, 62)
mouse.click()
keyboard.write("hello")
keyboard.press('enter')
