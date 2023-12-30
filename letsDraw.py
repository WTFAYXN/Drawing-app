# first let's import tkinter its a python library to construct GUI
import tkinter as tk
from tkinter.colorchooser import askcolor

#First we'll create a function. this will handle the beginning of the drawing 
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
