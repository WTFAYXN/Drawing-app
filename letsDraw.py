# first let's import tkinter its a python library to construct GUI
import tkinter as tk
from tkinter.colorchooser import askcolor

#First we'll create all the functions

# this will handle the beginning of the drawing 
def startDrawing(event):
    global isDrawing, prev_x, prev_y
    isDrawing = True
    prev_x, prev_y = event.x, event.y

# function to draw on the whiteboard
def draw(event):
    global isDrawing, prev_x, prev_y
    if isDrawing:
        current_x, current_y = event.x, event.prev_y
        canvas.create_line(prev_x,prev_y, current_x, current_y, fill= drawing_color, width= line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y

#function to stop drawing
def stopDrawing(event):
    global isDrawing
    isDrawing = False

def changePenColor():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

def changeLineWidth(value):
    global lineWidth
    lineWidth = int(value)

# lets start with the GUI
    
# window
    
root = tk.Tk()
root.title("LETS DRAW")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

isDrawing = False
drawing_color = "black"
lineWidth = 2

root.geometry("800x600")

#navbar and controls

controlsFrame = tk.Frame(root)
controlsFrame.pack(side="top", fill="x")

colorButton = tk.Button(controlsFrame, text="Change Color", command= changePenColor)
clearButton = tk.Button(controlsFrame, text="Clear Canvas", command= lambda: canvas.delete("all"))

colorButton.pack(side="left", padx=5, pady=5)
clearButton.pack(side="left", padx=5, pady=5)


lineWidthLabel = tk.Label(controlsFrame, text="Line Width:")
lineWidthLabel.pack(side="left", padx=5, pady=5)

lineWidthSlider = tk.Scale(controlsFrame, from_=1, to=10, orient="horizontal", command=lambda val: changeLineWidth(val))
lineWidthSlider.set(lineWidth)
lineWidthSlider.pack(side="left", padx=5, pady=5)


# Connect features to GUI

canvas.bind ("<Button-1>", startDrawing)
canvas.bind ("<B1-Motion>", draw)
canvas.bind("ButtonRelease-1", stopDrawing)

root.mainloop()

