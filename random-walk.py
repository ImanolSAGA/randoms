from tkinter import Tk, Canvas, PhotoImage,NW,mainloop 
import random
import time

# funcion para detectar el cierre de la ventana
running= True
def close_window():
  global running
  running = False
  print("Window closed")

#window size
xmax=800
ymax=500
refresh_seconds= 0.01

#Tkinter window
window = Tk()
canvas = Canvas(window, width = xmax, height = ymax, bg = "#000000");
canvas.pack()
img = PhotoImage(width = xmax, height = ymax)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)
random.seed(time.time_ns())

clr= ['#%02x%02x%02x' % (255, 255, 255), '#%02x%02x%02x' % (255, 0, 0)]
position= [int(xmax / 2), int(ymax / 2)]

while running:
  
  moveX= 0
  moveY= 0
  imageString= ""
  randomValue= random.randrange(30)
  if randomValue < 10 and position[0] < xmax: moveX= 1 
  elif randomValue < 20 and position[0] > 0: moveX= -1
    
  randomValue= random.randrange(30)
  if randomValue < 10 and position[1] < ymax: moveY= 1 
  elif randomValue < 20 and position[1] > 0: moveY= -1

  #print(imageString)
  try:
    img.put(clr[0], (position[0], position[1]))
    position= [position[0] + moveX, position[1] + moveY]
    img.put(clr[1], (position[0], position[1]))
    window.update()
    time.sleep(refresh_seconds)

  except:
    break