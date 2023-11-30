import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Projeto computacao grafica")
        
        self.pen_color = "black"
        self.eraser_color = "white"
        self.pen_size = 2
        self.eraser_mode = False

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.create_navbar()
        
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def create_navbar(self):
        navbar_frame = tk.Frame(self.root, bd=5, relief=tk.RAISED)
        navbar_frame.pack(side=tk.TOP, fill=tk.X)
        
        color_btn = tk.Button(navbar_frame, text="Cores", command=self.choose_color)
        color_btn.pack(side=tk.LEFT, padx=5)

        eraser_btn = tk.Button(navbar_frame, text="Borracha", command=self.toggle_eraser)
        eraser_btn.pack(side=tk.LEFT, padx=5)
        
        size_scale = tk.Scale(navbar_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Tamanho", command=self.set_size)
        size_scale.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.pen_color = color
            self.eraser_mode = False

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.pen_color = self.eraser_color
        else:
            self.pen_color = colorchooser.askcolor()[1] 

    def set_size(self, val):
        self.pen_size = int(val)

    def paint(self, event):
        x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
        x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color)

    def reset(self, event):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
