import queue

# estados do programa na worker thread (processamentos que ocorrem por trás da interface)

WAITING = "WAITING"
LISTENING = "LISTENING"
THINKING = "THINKING"
TALKING = "TALKING"


msg_queue = queue.Queue()