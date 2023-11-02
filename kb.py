import keyboard

def on_key_event(event):
    print("LISTENING ON THE KEYBOARD")
    if event.event_type == keyboard.KEY_DOWN and event.name == '2':
        print("2 PRESSED")
    elif event.event_type == keyboard.KEY_UP and event.name == '2':
        print("2 RELEASED")

# Hook the keyboard event
keyboard.hook(on_key_event)

# Keep the script running
keyboard.wait()
