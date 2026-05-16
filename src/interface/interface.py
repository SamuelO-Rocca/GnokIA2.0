#imports

import tkinter as tk 
from PIL import Image, ImageTk 
import os

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_width = int(((screen_width * 2) / 3))
root_height = int(((screen_height * 2) / 3))

center_width = int((screen_width / 2) - (root_width / 2))
center_height = int((screen_height / 2) - (root_height / 2))

root.geometry(f"{root_width}x{root_height}+{center_width}+{center_height}")
root_bg = "#0A0A0A"
root.configure(bg=root_bg)


img_state_gorilla = {
    "eyes_opened": "eyes_opened.png",
    "eyes_closed": "eyes_closed.png",
    "listening": "listening.png",
    "thinking": "thinking.png",
    "talking_1": "talking_1.png",
    "talking_2": "talking_2.png"
}

def returns_img_path(state):
    """Retorna o respectivo caminho da imagem de cada estado do avatar."""

    IMG_FOLDER = r"..\services\image"

    try:
        img_path = os.path.join(IMG_FOLDER, img_state_gorilla[state])

    except KeyError:
        print("Unable to return image path! The program will be terminated.")
        raise SystemExit
    
    return img_path


def display_gorilla(img_path, root, root_bg):
    """Retorna imagem do avatar exibida na janela da interface Tkinter."""

    try:
        gorilla_img = Image.open(img_path).resize((500, 500), Image.Resampling.LANCZOS)
        gorilla_img = ImageTk.PhotoImage(gorilla_img)
        label = tk.Label(root, image=gorilla_img, bg=root_bg)
        label.image = gorilla_img

    except FileNotFoundError:
        print("Unable to open image file! The program will be terminated.")
        raise SystemExit

    return label.pack(expand=True) 

#exemplo de chamado da função: 
display_gorilla(returns_img_path("eyes_opened"), root, root_bg)

root.mainloop()