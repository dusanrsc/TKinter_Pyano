# creating main app function
def main():
	# importing modules
	import tkinter
	import winsound

	# importing sub-modules (classes, functions etc...)
	from tkinter import Tk, Button

	# app classes
	class Note(tkinter.Tk):
		def __init__(self, x_pos=0, y_pos=0, height=20, width=5, color="#FFFFFF", frequency=2000, duration=300):
			self.button = Button(root, height=height, width=width, command=lambda: winsound.Beep(frequency, duration))
			self.button.configure(bg=color)
			self.button.place(x=x_pos, y=y_pos)

	# app variables
	__version__ = "v1.2.1-Alpha"

	# app list
	x_coordinates_big = [0, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 550, 495, 540, 585]
	x_coordinates_small = [28, 74, 120, 209, 255, 344, 389, 434, 524, 570]

	# app constants
	TITLE = "Pyano"
	SCREEN_WIDTH = str(x_coordinates_big[-1] + 45 - 1)
	SCREEN_HEIGHT = "310"

	# rgb color tuples
	RED = "#FF0000"
	GREEN = "#00FF00"
	BLUE = "#0000FF"

	BLACK = "#000000"
	WHITE = "#FFFFFF"

	ALPHA = GREEN
	
	# creating main window
	# app settings
	root = Tk()
	root.title(f"{TITLE} {__version__}")
	root.config(bg=WHITE)
	root.resizable(False, False)
	root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

	# drawing buttons on the screen
	# big ones
	for item in x_coordinates_big:
		note_big = Note(x_pos=item, color=WHITE)

	# small ones
	for item in x_coordinates_small:
		note_small = Note(x_pos=item, height=10, width=3, color=BLACK)

	# starting app mainloop
	root.mainloop()

# triggering main function (starting app)
if __name__ == "__main__":
	main()