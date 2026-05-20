#imports

from abc import ABC, abstractmethod
from PIL import Image, ImageTk 
import os

class AvatarState(ABC):
    img_state_avatar = {
        "eyes_opened": "eyes_opened.png",
        "eyes_closed": "eyes_closed.png",
        "listening": "listening.png",
        "thinking": "thinking.png",
        "open_mouth": "open_mouth.png",
        "talking": "talking.png"
    }

    def returns_img_path(self, state):
        """Retorna o respectivo caminho da imagem de cada estado do avatar."""

        try:
            img_path = os.path.join(os.path.dirname(__file__), "..", "..", "services", "image", self.img_state_avatar[state])

        except KeyError:
            print("Unable to return image path! The program will be terminated.")
            raise SystemExit
            
        return img_path

    def display_avatar(self, img_path, label):
        """Retorna imagem do avatar exibida na janela da interface Tkinter."""

        try:
            avatar_img = Image.open(img_path).resize((500, 500), Image.Resampling.LANCZOS)
            avatar_img_tk = ImageTk.PhotoImage(avatar_img)
            label.configure(image=avatar_img_tk)
            label.image = avatar_img_tk

        except FileNotFoundError:
            print("Unable to open image file! The program will be terminated.")
            raise SystemExit

        return label.image
    
    @abstractmethod
    def enter_state(self, label):
        pass