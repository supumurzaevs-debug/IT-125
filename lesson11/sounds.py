import tkinter as tk
import pygame
import os
from PIL import Image, ImageTk

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def show_image(path, label):
    img = Image.open(path)
    img = img.resize((200, 150))
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img


def create_app():
    root = tk.Tk()
    root.title("Animal Sounds")
    root.geometry('300x550')
    root.resizable(False, False)

    # Место для картинки
    image_label = tk.Label(root)
    image_label.pack(pady=10)

    tk.Button(
        root, text="Cow", font=("Arial", 14),
        command=lambda: (
            play_sound(abs_path("sounds/farm-ambience.mp3")),
            show_image(abs_path("image/pexels-pixabay-458991.jpg"), image_label)
        )
    ).pack(pady=10)

    tk.Button(
        root, text="Birds", font=("Arial", 14),
        command=lambda: (
            play_sound(abs_path("sounds/morning-meadow-birdsongs-looping_zyb7nhnu.mp3")),
            show_image(abs_path("image/d7fa231cac3026b44e583002fabe8b92.jpg"), image_label)
        )
    ).pack(pady=10)

    tk.Button(
        root, text="Leo", font=("Arial", 14),
        command=lambda: (
            play_sound(abs_path("sounds/dalnevostochnyj-leopard-1.mp3")),
            show_image(abs_path("image/images.jpg"), image_label)
        )
    ).pack(pady=10)

    tk.Button(
        root, text="Rain", font=("Arial", 14),
        command=lambda: (
            play_sound(abs_path("sounds/15-rainroof.mp3")),
            show_image(abs_path("image/189.jpg"), image_label)
        )
    ).pack(pady=10)

    tk.Button(
        root, text="Wondering", font=("Arial", 14),
        command=lambda: (
            play_sound(abs_path("sounds/huh-cat-meme.mp3")),
            show_image(abs_path("image/images (1).jpg"), image_label)
        )
    ).pack(pady=10)

    root.mainloop()


create_app()