import tkinter as tk
 
 
class RasterizationApp:
    mode = "circle"
    mouse_clicked_x = -1
    mouse_clicked_y = -1
    start_x = -1
    start_y = -1
 
    def __init__(self, root):
        self.root = root
        self.root.title("Растеризация: Отрезки и Окружности")
        self.root.resizable(False, False)  # Запрещаем изменение размера окна
 
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()
 
        self.draw_axes_and_grid()
 
        # Добавляем возможность перемещения графика с помощью мыши
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonPress-1>", self.on_click)
 
        # Кнопки для масштабирования
        plus_button = tk.Button(root, text="Zoom in", command=self.zoom_in)
        plus_button.pack(side=tk.LEFT)
        minus_button = tk.Button(root, text="Zoom out", command=self.zoom_out)
        minus_button.pack(side=tk.LEFT)
 
        circle_button = tk.Button(root, text="Circle", command=self.switch_mode_circle)
        circle_button.pack(side=tk.LEFT)
 
        line_button = tk.Button(root, text="Line", command=self.switch_mode_line)
        line_button.pack(side=tk.LEFT)
 
        line_bresenham = tk.Button(root, text="Bresenham line", command=self.switch_mode_bresenhem_line)
        line_bresenham.pack(side=tk.LEFT)
 
        shift_button = tk.Button(root, text='Shift mode', command=self.switch_mode_shift)
        shift_button.pack(side=tk.LEFT)
 
        # Начальные координаты клика мыши
        self.start_x = 0
        self.start_y = 0
 
    def switch_mode_circle(self):
        self.mode="circle"
 
    def switch_mode_line(self):
        self.mode="line"
 
    def switch_mode_bresenhem_line(self):
        self.mode="bresenham_line"
 
    def switch_mode_shift(self):
        self.mode="shift"
 
    def draw_axes_and_grid(self):
        for i in range(0, 1000, 20):
            self.canvas.create_line(i, 0, i, 1000, fill="lightgray")
            self.canvas.create_line(0, i, 1000, i, fill="lightgray")
 
        self.canvas.create_line(300, 0, 300, 600, width=2)
        self.canvas.create_line(0, 300, 800, 300, width=2)
 
        # Подписываем оси
        self.canvas.create_text(310, 10, text="Y", anchor=tk.W)
        self.canvas.create_text(590, 310, text="X", anchor=tk.W)
 
        # Добавляем метки на осях
        for i in range(-15, 26):
            if i != 0:
                self.canvas.create_text(300 + i * 20, 310, text=str(i), anchor=tk.N)
            if i <= 15:
                self.canvas.create_text(310, 300 - i * 20, text=str(i), anchor=tk.W)
 
    def draw_line(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
 
        x_increment = dx / steps
        y_increment = dy / steps
 
        x, y = x1, y1
        for _ in range(steps + 1):
            print(f"Drawing rectangle at ({x}, {y}) with color {color}")
            self.canvas.create_rectangle(x, y, x + 2, y + 2, fill=color, outline="")
            x += x_increment
            y += y_increment
 
    def draw_line_bresenham(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
 
        points = []
        while True:
            points.append((x0, y0))
 
            if x0 == x1 and y0 == y1:
                break
 
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
 
        for x,y in points:
            self.canvas.create_rectangle(x, y, x + 2, y + 2, fill=color, outline="")
 
    def draw_circle_bresenham(self, xc, yc, r, color):
        x = 0
        y = r
        d = 3 - 2 * r
 
        while x <= y:
            self.draw_circle_points(xc, yc, x, y, color)
            x += 1
            if d > 0:
                y -= 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6
            self.draw_circle_points(xc, yc, x, y, color)
 
    def draw_circle_points(self, xc, yc, x, y, color):
        print(f"Drawing circle point at ({xc + x}, {yc + y}) with color {color}")
        self.canvas.create_rectangle(xc + x, yc + y, xc + x + 2, yc + y + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc - x}, {yc + y}) with color {color}")
        self.canvas.create_rectangle(xc - x, yc + y, xc - x + 2, yc + y + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc + x}, {yc - y}) with color {color}")
        self.canvas.create_rectangle(xc + x, yc - y, xc + x + 2, yc - y + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc - x}, {yc - y}) with color {color}")
        self.canvas.create_rectangle(xc - x, yc - y, xc - x + 2, yc - y + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc + y}, {yc + x}) with color {color}")
        self.canvas.create_rectangle(xc + y, yc + x, xc + y + 2, yc + x + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc - y}, {yc + x}) with color {color}")
        self.canvas.create_rectangle(xc - y, yc + x, xc - y + 2, yc + x + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc + y}, {yc - x}) with color {color}")
        self.canvas.create_rectangle(xc + y, yc - x, xc + y + 2, yc - x + 2, fill=color, outline="")
        print(f"Drawing circle point at ({xc - y}, {yc - x}) with color {color}")
        self.canvas.create_rectangle(xc - y, yc - x, xc - y + 2, yc - x + 2, fill=color, outline="")
 
    def zoom_in(self):
        self.canvas.scale(tk.ALL, 300, 300, 1.1, 1.1)
 
    def zoom_out(self):
        self.canvas.scale(tk.ALL, 300, 300, 0.9, 0.9)
 
    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
 
        if (self.mode == "circle"):
            self.draw_circle_bresenham(self.start_x, self.start_y, 50, "green")
 
        if (self.mode == "line" or self.mode == "bresenham_line"):
            if (self.mouse_clicked_x == -1 and self.mouse_clicked_y == -1):
                self.mouse_clicked_x = event.x
                self.mouse_clicked_y = event.y
            elif(self.mode == "line"):
                self.draw_line(self.mouse_clicked_x, self.mouse_clicked_y, event.x, event.y, "red")
                self.mouse_clicked_x = -1
                self.mouse_clicked_y = -1
            elif(self.mode == "bresenham_line"):
                self.draw_line_bresenham(self.mouse_clicked_x, self.mouse_clicked_y, event.x, event.y, "blue")
                self.mouse_clicked_x = -1
                self.mouse_clicked_y = -1
 
 
    def drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.start_x = event.x
        self.start_y = event.y
        if (self.mode == "shift"):
            self.canvas.move(tk.ALL, dx, dy)
 
if __name__ == "__main__":
    root = tk.Tk()
    app = RasterizationApp(root)
    root.mainloop()
