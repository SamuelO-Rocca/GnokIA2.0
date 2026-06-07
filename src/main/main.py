from src.message_queue.message_queue import msg_queue, WAITING, LISTENING, THINKING, TALKING
from src.interface.InterfaceGnokIA import InterfaceGnokIA
from src.interface.AvatarStates import *

def run():
    interface = InterfaceGnokIA()
    interface.root.after(0, lambda: interface.force_state(OpenedEyeState()))
    interface.run()
