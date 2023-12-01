import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
 
def smoothing_filter(image):
    # Создаем ядро для сглаживающего фильтра
    kernel = np.ones((5,5), np.float32) / 25  # 5x5 ядро со значениями 1/25
 
    # Применяем фильтр к изображению
    smoothed_image = cv2.filter2D(image, -1, kernel)
 
    return smoothed_image
 
def median_blur(image):
    result = cv2.medianBlur(image, 5)
    return result
 
def gaussian_blur(image):
    result = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    return result
 
def otsu_thresholding(image):
    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # Применение алгоритма Отсу для определения порога
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
 
    return threshold_image
 
def process_image():
    # Открытие диалогового окна для выбора изображения
    file_path = filedialog.askopenfilename()
    if file_path:
        # Загрузка изображения
        image = cv2.imread(file_path)
 
        smoothed_image = smoothing_filter(image)
        gaussed_image = gaussian_blur(image)
        otsu = otsu_thresholding(image)
        # Отображение исходного и обработанного изображений
        cv2.imshow("Original Image", image)
        cv2.imshow("Smoothed Image", smoothed_image)
        cv2.imshow("Otsu Image", otsu)
        cv2.imshow("Gaussed Image", gaussed_image)
        cv2.waitKey(0)
 
# Создание графического интерфейса с кнопкой "Выбрать изображение"
root = tk.Tk()
 
button = tk.Button(root, text="Выбрать изображение", command=process_image)
button.pack()
 
root.mainloop()
