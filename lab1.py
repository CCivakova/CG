import tkinter as tk
from tkinter import colorchooser
import colorsys
 
class ColorConverterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Converter")
 
        self.rgb_labels = []
        self.rgb_sliders = []
        self.rgb_values = [0, 0, 0]
        self.rgbs = [0, 0, 0]
 
        self.cmyk_labels = []
        self.cmyk_values = [0, 0, 0, 0]
 
        self.hsv_labels = []
        self.hsv_values = [0, 0, 0]
 
        self.create_rgb_section()
        self.create_cmyk_section()
        self.create_hsv_section()
        self.create_color_picker_button()
 
    def create_rgb_section(self):
        rgb_frame = tk.Frame(self.root, padx=10, pady=10)
        rgb_frame.pack()
 
        rgb_label = tk.Label(rgb_frame, text="RGB", font=("Helvetica", 16, "bold"))
        rgb_label.pack()
 
        for i, color in enumerate(["Red", "Green", "Blue"]):
            label = tk.Label(rgb_frame, text=color)
            label.pack()
            self.rgb_labels.append(label)
 
            value_label = tk.Label(rgb_frame, text="0")
            value_label.pack()
            self.rgbs[i] = value_label
 
            slider = tk.Scale(rgb_frame, from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_rgb, sliderlength=20, length=200, showvalue=0)
            slider.pack()
            self.rgb_sliders.append(slider)
 
 
        for i, value in enumerate(self.rgb_values):
            slider = self.rgb_sliders[i]
            slider.set(value)
 
 
    def create_cmyk_section(self):
        cmyk_frame = tk.Frame(self.root, padx=10, pady=10)
        cmyk_frame.pack()
 
        cmyk_label = tk.Label(cmyk_frame, text="CMYK", font=("Helvetica", 16, "bold"))
        cmyk_label.pack()
 
        for i, color in enumerate(["Cyan", "Magenta", "Yellow", "Black"]):
            label = tk.Label(cmyk_frame, text=color)
            label.pack()
            self.cmyk_labels.append(label)
 
            value_label = tk.Label(cmyk_frame, text="0")
            value_label.pack()
            self.cmyk_values[i] = value_label
 
    def create_hsv_section(self):
        hsv_frame = tk.Frame(self.root, padx=10, pady=10)
        hsv_frame.pack()
 
        hsv_label = tk.Label(hsv_frame, text="HSV", font=("Helvetica", 16, "bold"))
        hsv_label.pack()
 
        for i, color in enumerate(["Hue", "Saturation", "Value"]):
            label = tk.Label(hsv_frame, text=color)
            label.pack()
            self.hsv_labels.append(label)
 
            value_label = tk.Label(hsv_frame, text="0")
            value_label.pack()
            self.hsv_values[i] = value_label
 
    def create_color_picker_button(self):
        color_picker_frame = tk.Frame(self.root, padx=10, pady=10)
        color_picker_frame.pack()
 
        color_picker_button = tk.Button(color_picker_frame, text="Pick Color", command=self.pick_color)
        color_picker_button.pack()
 
    def update_rgb(self, event):
        r = self.rgb_sliders[0].get()
        g = self.rgb_sliders[1].get()
        b = self.rgb_sliders[2].get()
 
        self.rgbs[0]['text'] = str(r)
        self.rgbs[1]['text'] = str(g)
        self.rgbs[2]['text'] = str(b)
 
        self.rgb_values = [r, g, b]
 
        c, m, y, k = self.rgb_to_cmyk(r, g, b)
        self.update_cmyk_values(c, m, y, k)
 
        h, s, v = self.rgb_to_hsv(r, g, b)
        self.update_hsv_values(h, s, v)
 
    def pick_color(self):
        color = colorchooser.askcolor()
        if color[1] is not None:
            r, g, b = color[0]
            self.rgb_sliders[0].set(int(r))
            self.rgb_sliders[1].set(int(g))
            self.rgb_sliders[2].set(int(b))
 
    def update_cmyk_values(self, c, m, y, k):
        self.cmyk_values[0]['text'] = str(c)
        self.cmyk_values[1]['text'] = str(m)
        self.cmyk_values[2]['text'] = str(y)
        self.cmyk_values[3]['text'] = str(k)
 
    def update_hsv_values(self, h, s, v):
        self.hsv_values[0]['text'] = str(h)
        self.hsv_values[1]['text'] = str(s)
        self.hsv_values[2]['text'] = str(v)
 
    def rgb_to_cmyk(self, r, g, b):
        r = r / 255.0
        g = g / 255.0
        b = b / 255.0
 
        k = 1 - max(r, g, b)
        c = (1 - r - k) / (1 - k) if (1 - k) != 0 else 0
        m = (1 - g - k) / (1 - k) if (1 - k) != 0 else 0
        y = (1 - b - k) / (1 - k) if (1 - k) != 0 else 0
 
        return c, m, y, k
 
    def rgb_to_hsv(self, r, g, b):
        r = r / 255.0
        g = g / 255.0
        b = b / 255.0
 
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
 
        h = round(h * 360)
        s = round(s * 100)
        v = round(v * 100)
 
        return h, s, v
 
    def run(self):
        self.root.mainloop()
 
if __name__ == "__main__":
    app = ColorConverterApp()
    app.run()
