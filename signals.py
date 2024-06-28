import signal
import time

# define handler
def interrupt_handler(signum, frame):
    print("\nInterrupción capturada. Señal:", signum)
    print("Realizando tareas de limpieza...")
    exit(0)


def set_error():
    raise Exception("This is an exception")

# Regist interruption SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, interrupt_handler)

print("Presiona Ctrl+C para generar una interrupción.")
print("Esperando interrupciones...")

# Emulate large process
while True:
    try:
        time.sleep(1)
        print("Trabajando...")
        set_error()
    except Exception as err:
        print("Error:", err)
        break
    finally:
        print("Limpieza final")


