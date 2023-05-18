import tkinter
import time
import random

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
		newIncrement= 0-0
		for i in range(len(self.steps)):
			newIncrement+= self.increment[i] * self.currentVector[i]

			if self.stepCount % self.steps[i] == 0:
				nextDest= random.randrange(self.myRange)
				self.currentVector[i]= nextDest - self.currentDest[i]
				self.currentDest[i]= nextDest
				
		self.lastValue+= newIncrement #/ len(self.steps)
		self.stepCount+= 1
		return(self.lastValue)

# creamos ventana
window= tkinter.Tk()

xmax, ymax= 800, 500
window.geometry(str(xmax)+"x"+str(ymax))
window.resizable(width=False, height=False)
window.protocol("WM_DELETE_WINDOW", close_window)


# creamos canvas
canvas= tkinter.Canvas(window, bg= "black")
canvas.pack(fill="both", expand=True)



# creamos animacion

random.seed(time.time_ns())
values= [0 for _ in range(10)]
rectangles= []
for i in range(10):
	x0, x1= i*80, (i+1)*80
	y0, y1= 500, 495
	rectangles.append(canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="blue", width=5))


refresh_seconds= 0.005
perlin= perlinNoise()
perlin.inicialize([ "103x0.7" , "76x0.1" , "48x0.1" , "26x0.08" , "10x0.02"], 10)


while running:

	newValue= int(perlin.nextPerlin())
	values[newValue]+= 1

	x0, x1= newValue*80, (newValue+1)*80
	y0, y1= 500, 495 - (values[newValue] / 3)

	if y1 <= 0: break

	canvas.delete(rectangles[newValue])
	
	rectangles[newValue]= canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="blue", width=5)

	window.update()
	time.sleep(refresh_seconds)

while running: # animation finished and stop
	window.update()
	time.sleep(refresh_seconds)