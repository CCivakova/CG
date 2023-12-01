import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

def apply_blur(image):
    result = cv2.blur(image, (3, 3))
    return result

def gaussian_blur(image):
    result = cv2.GaussianBlur(image, (5, 5), 0)
    return result

def otsu_thresholding(image):
    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Применение алгоритма Отсу для определения порога
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return threshold_image


def global_threshold(image):
    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Выбор порогового значения
    threshold_value = 128  # Задайте пороговое значение здесь

    # Применение порогового значения для бинаризации изображения
    _, threshold = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    return threshold

def threshold_mean(image):
    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Вычисляем среднее значение яркости всех пикселей на изображении
    mean_value = gray_image.mean()

    # Применяем пороговое значение к изображению
    _, thresholded_image = cv2.threshold(gray_image, mean_value, 255, cv2.THRESH_BINARY)

    return thresholded_image

def process_image():
    # Открытие диалогового окна для выбора изображения
    file_path = filedialog.askopenfilename()
    if file_path:
        # Загрузка изображения
        image = cv2.imread(file_path)
        gaussed_image = gaussian_blur(image)
        otsu = otsu_thresholding(image)
        blured = apply_blur(image)
        gl = global_threshold(image)
        # Отображение исходного и обработанного изображений
        cv2.imshow("Original Image", image)
        cv2.imshow("Otsu Image", otsu)
        cv2.imshow("Gaussed Image", gaussed_image)
        cv2.imshow("Global thresholded Image", gl)
        cv2.imshow("Blured image", blured)
        cv2.waitKey(0)

# Создание графического интерфейса с кнопкой "Выбрать изображение"
root = tk.Tk()

button = tk.Button(root, text="Выбрать изображение", command=process_image)
button.pack()

root.mainloop()
