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
refresh_seconds= 0.001
step_px= 1

# lista de randoms eje Y
rlist= []
random.seed(time.time_ns())

perlin= perlinNoise()
perlin.inicialize([ "103x0.7" , "76x0.1" , "48x0.1" , "26x0.08" , "10x0.02"], ymax)

for _ in range(0, xmax, step_px):
	rlist.append(perlin.nextPerlin())
	#rlist.append(random.randrange(ymax))

#print(rlist)

lastY= perlin.nextPerlin()

while running:

	# creamos las lineas
	line_list= []
	rlistCount= 0
	for x in range(0, xmax, step_px):
		
		auxline= canvas.create_line(x, lastY, x+step_px, rlist[rlistCount], fill= "white", width= 1)

		line_list.append(auxline)

		lastY= rlist[rlistCount]
		rlistCount+= 1

	# refrescamos y esperamos
	window.update()
	print(lastY)
	time.sleep(refresh_seconds)

	# actualizamos lista de randoms eje Y
	lastY= rlist[0]
	rlist.pop(0)
	rlist.append(perlin.nextPerlin())
	#print(rlist[-1])

	# destruimos las lineas
	for lineId in line_list: canvas.delete(lineId)