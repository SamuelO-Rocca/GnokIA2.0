#imports

from src.message_queue.message_queue import msg_queue, WAITING, LISTENING, THINKING, TALKING
from src.interface.InterfaceGnokIA import InterfaceGnokIA
from src.interface.AvatarStates import *
from src.services.audio.STT import capture_audio, processing_audio_to_text
from src.mcp.central.brain import process_user_input
from src.services.audio.TTS import TTS
import threading


#instancia a classe TTS
tts = TTS()

# envia mensagem nova pela fila de mensagens
def send_msg(msg):
    """Insere uma nova mensagem para ser enviada na pela fila (msg_queue)."""

    msg_queue.put(msg)

# orquestra o loop de funcionamento do programa
def orchestrate():   
    """Executa o fluxo do orquestrador do programa, colocando em sintonia as ações do módulo de serviço com a mudança de imagens da interface, através da fila de mensagens."""

    while True:

        input("Pressione Enter para falar...") 
        #o enter desbloqueia a execução do restante da função

        send_msg(LISTENING)
        question_audio = capture_audio()
        if question_audio is None:
            send_msg(WAITING)
            continue

        question_text = processing_audio_to_text(question_audio)
        if question_text is None:
            send_msg(WAITING)
            continue

        send_msg(THINKING)
        response_text = process_user_input(question_text)
        if response_text is None:
            send_msg(WAITING)
            continue

        send_msg(TALKING)
        tts.synthesize_text_to_speech(response_text)

        send_msg(WAITING)


def run():
    interface = InterfaceGnokIA()
    interface.force_state(OpenedEyeState())
    thread = threading.Thread(target=orchestrate)
    thread.start()
    interface.run()