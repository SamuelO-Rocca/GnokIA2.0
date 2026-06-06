#imports

import tkinter as tk
import queue
from src.interface.AvatarStates import *
from src.message_queue.message_queue import msg_queue, WAITING, LISTENING, THINKING, TALKING
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
        self.current_state = None # inicialização do estado do avatar

        # inicialiação do id do agendador .after() usado nas animações do avatar
        self.after_id = None

        # chama a função que agenda as trocas de estado recebendo mensagens da fila
        self.state_switching()

    # estabelece a exibição do avatar
    def force_state(self, new_state):
        """Esse método 'chama' a mudança de estado do avatar.
        A mudança de imagem ocorre posteriormente a partir de enter_state().
        """
        self.current_state = new_state
        if self.after_id is not None:
            self.label.after_cancel(self.after_id)
        self.current_state.enter_state(self.label, self) 

    # animação de piscar do avatar
    def start_blinking_animation(self):
        """Verifica os estados do avatar para fazer a animação dele piscando"""

        if isinstance(self.current_state, OpenedEyeState):
            self.force_state(ClosedEyeState())
        else:
            self.force_state(OpenedEyeState())

    # animação de fala do avatar
    def start_talking_animation(self):
        """Verifica os estados do avatar para fazer a animação dele falando."""

        if isinstance(self.current_state, OpenMouthState):
            self.force_state(TalkingState())
        else:
            self.force_state(OpenMouthState())

    # providencia a troca de imagem a partir da verificação de mensagens da fila
    def state_switching(self):
        """Verifica na fila de mensagens se há uma troca de imagem agendada para o avatar. Providencia a troca se necessário, e, se não, agenda a execução da função novamente para verificar de novo mais tarde."""

        try:
            msg = msg_queue.get_nowait()
            match msg:
                case "WAITING":
                    self.force_state(OpenedEyeState())
                case "LISTENING":
                    self.force_state(ListeningState())
                case "THINKING":
                    self.force_state(ThinkingState())
                case "TALKING":
                    self.force_state(OpenMouthState())
        except queue.Empty:
            self.after_id = self.root.after(100, lambda: self.state_switching())    

    # roda o programa
    def run(self):
        self.root.mainloop()

# exemplo de execução da interface
interface = InterfaceGnokIA()
interface.force_state(OpenedEyeState())
interface.run()