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

#Tkinter window
window = Tk()
canvas = Canvas(window, width = xmax, height = ymax, bg = "#000000");
canvas.pack()
img = PhotoImage(width = xmax, height = ymax)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)
random.seed(time.time_ns())

clr= []
for i in range(256): clr.append('#%02x%02x%02x' % (i, i, i))

while running:
  
  # create random noise
  imageString= ""
  for y in range(ymax):
    imageString+= "{"
    for x in range(xmax):
      imageString+= clr[random.randrange(255)] + " " 
    imageString+= "} "

  #print(imageString)
  try:
    img.put(imageString)
    window.update()
  except:
    break