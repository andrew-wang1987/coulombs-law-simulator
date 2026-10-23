# for the animations
# dependency
import tkinter as tk

class Sprite:
    def __init__(self, canvas, frames, x, y, delay):
        self.canvas = canvas
        self.delay = delay
        self.current_frame = 0
        self.frames = [tk.PhotoImage(file=path) for path in frames]
        self.id = self.canvas.create_image(x, y, image=self.frames[self.current_frame])
        self.running = False
        
    def start(self):
         if not self.running:
            self.running = True
            self.run()
    
    def stop(self):
        self.running = False
    
    def run(self):
        if not self.running:
            return
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canvas.itemconfig(self.id, image=self.frames[self.current_frame])
        self.canvas.after(self.delay, self.run)
    
    def moveX(self, x):
        self.canvas.move(self.id, x, 0)

    def setX(self, x):
        self.canvas.coords(self.id, x, self.canvas.coords(self.id)[1])
