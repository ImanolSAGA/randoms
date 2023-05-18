from tkinter import Tk, Canvas, PhotoImage,NW,mainloop 
import random
import time

# funcion para detectar el cierre de la ventana
running= True
def close_window():
  global running
  running = False
  print("Window closed")

class perlinNoise:

  def inicialize(self, _info, _range):
    # _info = [ "10x0.8", "4x0.15", "1x0.05" ] format "int x float"
    # el int son los pasos cada cuanto se refresca el valor
    # el float es la fuerza con la que movera el valor, la suma de todos los floats debe ser cerca de 1.0
    # el _range es el rango en el que devolvera los valores, del 0 al valor _range
    self.steps= []
    self.increment= []
    self.currentDest= []
    self.currentVector= []
    self.myRange= _range
    self.lastValue= random.randrange(self.myRange)
    self.stepCount= 1
    for i in range(len(_info)):
      aux= _info[i].split("x")
      self.steps.append(int(aux[0]))
      self.increment.append(float(aux[1]) / float(aux[0]))
      self.currentDest.append(random.randrange(self.myRange))
      self.currentVector.append(self.currentDest[i] - self.lastValue)
      
  def nextPerlin(self):
    newIncrement= 0.0
    for i in range(len(self.steps)):
      newIncrement+= self.increment[i] * self.currentVector[i]

      if self.stepCount % self.steps[i] == 0:
        nextDest= random.randrange(self.myRange)
        self.currentVector[i]= nextDest - self.currentDest[i]
        self.currentDest[i]= nextDest
        
    self.lastValue+= newIncrement #/ len(self.steps)
    self.stepCount+= 1
    return(self.lastValue)

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

perlin0, perlin1= perlinNoise(), perlinNoise()
perlin0.inicialize(["16x0.4","24x0.3","5x0.3"], 300)
perlin1.inicialize(["16x0.4","24x0.3","5x0.3"], 300)

while running:
  
  moveX= 0
  moveY= 0
  imageString= ""
  perlinValue= [int(perlin0.nextPerlin()), int(perlin1.nextPerlin())]

  if perlinValue[0] > 80 and perlinValue[0] < 220:
    if perlinValue[0] < 150 and position[0] < xmax: moveX= 1 
    elif position[0] > 1: moveX= -1
    
  
  if perlinValue[1] > 80 and perlinValue[1] < 220:
    if perlinValue[1] < 150 and position[1] < ymax: moveY= 1 
    elif position[1] > 1: moveY= -1

  #print(imageString)
  try:
    img.put(clr[0], (position[0], position[1]))
    position= [position[0] + moveX, position[1] + moveY]
    img.put(clr[1], (position[0], position[1]))
    window.update()
    print(perlinValue)
    time.sleep(refresh_seconds)

  except:
    break