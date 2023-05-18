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
        
    self.lastValue+= newIncrement
    self.stepCount+= 1
    return(self.lastValue)

  def getPerlin2D(self, _info, _height, _width):

    # inicializo un array de arrays con los colores de cada linea 
    # el contenido final sera algo asi: [[256, 0, 0, 0, 0, 0], [256, 0, 0, 0, 0, 0]]
    finalGrid= [] 
    for y in range(_height):
      finalGrid.append([])
      for x in range(_width):
        finalGrid[y].append(0)

    # sumamos las grids de cada frecuencia del perlin
    for model in range(len(_info)):
      phasePerlin= perlinNoise()
      aux= _info[model].split("x")
      modelStep= int(aux[0])
      phasePerlin.inicialize([_info[model]], int(256 * float(aux[1])))

      perlinYSteps= int(round((_height / modelStep) + 0.5)) # el + 0.5 es para redondear al alza
      gridY= []

      for y in range(perlinYSteps + 1):
        gridY.append([])
        for x in range(_width):
          gridY[y].append(int(phasePerlin.nextPerlin()))

      gridYIndex= 0

      for y in range(_height):
        if y % modelStep == 0:
          for x in range(_width):
            finalGrid[y][x]+= gridY[gridYIndex][x]

            valueFrom, valueTo= gridY[gridYIndex][x], gridY[gridYIndex + 1][x]
            increase= (valueTo - valueFrom) / modelStep

            for ms in range(modelStep - 1):
              if y + ms + 1 < len(finalGrid):
                finalGrid[y + ms + 1][x]+= (valueFrom + (increase * (ms + 1)))

              else: break

          gridYIndex+= 1
            
    return(finalGrid)


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
  
  perlinImage= perlinNoise()
  compressedImage= perlinImage.getPerlin2D(["60x0.5","34x0.35","5x0.15"], ymax, xmax)
  # print(len(compressedImage), len(compressedImage[-1]))
  # create random noise
  imageString= ""
  for y in range(ymax):
    imageString+= "{"
    for x in range(xmax):
      imageString+= clr[int(compressedImage[y][x])] + " " 
    imageString+= "} "

  #print(imageString)
  try:
    img.put(imageString)
    window.update()
  except:
    break