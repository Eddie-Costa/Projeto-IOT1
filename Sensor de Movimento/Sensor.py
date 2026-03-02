from pynput import mouse

with mouse.Listener(on_move=on_move) as listener:
    listener.join()