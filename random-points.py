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
refresh_seconds= 0.01
step_px= 1

# lista de randoms eje Y
rlist= []
random.seed(time.time_ns())
for _ in range(0, xmax, step_px):
	rlist.append(random.randrange(ymax))

lastY= random.randrange(ymax)

while running:

	# creamos las lineas
	line_list= []
	rlistCount= 0
	for x in range(0, xmax, step_px):
		
		auxline= canvas.create_line(x+step_px-1, rlist[rlistCount]-1, x+step_px, rlist[rlistCount], fill= "white", width= 1)

		line_list.append(auxline)

		lastY= rlist[rlistCount]
		rlistCount+= 1

	# refrescamos y esperamos
	window.update()
	time.sleep(refresh_seconds)

	# actualizamos lista de randoms eje Y
	lastY= rlist[0]
	rlist.pop(0)
	rlist.append(random.randrange(ymax))

	# destruimos las lineas
	for lineId in line_list: canvas.delete(lineId)