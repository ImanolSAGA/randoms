import tkinter
import time

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

ball= canvas.create_oval(398, 248, 402, 252, fill="white")
xinc, yinc= 2, 2
refresh_seconds= 0.01


while running:

	canvas.move(ball,xinc,yinc)
	window.update()
	time.sleep(refresh_seconds)
	ball_pos= canvas.coords(ball)

	# unpack array to variables
	xl,yl,xr,yr= ball_pos
	if xl < 1 or xr > xmax-abs(xinc):
	  xinc= -xinc
	if yl < 1 or yr > ymax-abs(yinc):
	  yinc= -yinc