import tkinter
import time
import random

# funcion para detectar el cierre de la ventana
running= True
def close_window():
  global running
  running = False
  print("Window closed")


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

values= [0 for _ in range(10)]
rectangles= []
for i in range(10):
	x0, x1= i*80, (i+1)*80
	y0, y1= 500, 495
	rectangles.append(canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="blue", width=5))


refresh_seconds= 0.005


while running:

	newValue= random.randrange(0,10)
	values[newValue]+= 1

	x0, x1= newValue*80, (newValue+1)*80
	y0, y1= 500, 495 - values[newValue]

	if y1 <= 0: break

	canvas.delete(rectangles[newValue])
	
	rectangles[newValue]= canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="blue", width=5)

	window.update()
	time.sleep(refresh_seconds)

while running: # animation finished and stop
	window.update()
	time.sleep(refresh_seconds)