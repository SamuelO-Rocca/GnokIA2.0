#imports

import tkinter as tk
from AvatarStates import *  

class InterfaceGnokIA:
    def __init__(self):
        self.root = tk.Tk()
        self.root_bg = "#0A0A0A"

        # calcula medidas da tela da máquina 
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # calcula medidas da janela Tkinter
        self.root_width = int(((self.screen_width * 2) / 3))
        self.root_height = int(((self.screen_height * 2) / 3))

        # calcula centralização da janela
        self.center_width = int((self.screen_width / 2) - (self.root_width / 2))
        self.center_height = int((self.screen_height / 2) - (self.root_height / 2))

        # estabelece as medidas e a cor da janela
        self.root.geometry(f"{self.root_width}x{self.root_height}+{self.center_width}+{self.center_height}")
        self.root.configure(bg=self.root_bg)

        # declara componentes do avatar
        self.label = tk.Label(self.root, bg=self.root_bg)
        self.label.pack(expand=True)
        self.current_state = None # inicialização

    # estabelece a exibição do avatar
    def force_state(self, new_state):
        self.current_state = new_state
        self.current_state.enter_state(self.label) 

    # roda o programa
    def run(self):
        self.root.mainloop()

# exemplo de execução da interface
interfaceGnokIA = InterfaceGnokIA()
interfaceGnokIA.force_state(OpenedEyeState())
interfaceGnokIA.run()