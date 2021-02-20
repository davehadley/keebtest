from pynput import keyboard

def main():
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
    return

def on_press(key):
    print(f"{key} pressed")

def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    main()
