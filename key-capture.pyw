import tkinter as tk
from pynput import keyboard

import math


fade_requests = 0

def position(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() - math.floor( win.winfo_width() * 1.4 )
    y = win.winfo_screenheight() - math.floor( win.winfo_height() * 1.8 )
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #win.geometry('{}x{}+{}+{}'.format(width, height, 20, 20))
    #win.deiconify()
    
    

def on_key_press(key):
    try:
        char = key.char
    except AttributeError:
        char = str(key)

    show_key(char)

def on_key_release(key):
    pass

def show_key(char):
    global fade_requests
    root.deiconify()
    label.config(text=char)
    label.place(relx=0.5, rely=0.5, anchor="center")

    fade_requests += 1
    label.after(2000, fade_out)

def fade_out():
    global fade_requests
    print(fade_requests)
    if fade_requests > 0 :
        fade_requests -= 1
    
    if fade_requests == 0 :
        root.withdraw()
        #root.withdraw()
        label.place_forget()
    
    return
    

def start_key_capture():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        root.mainloop()

root = tk.Tk()
root.overrideredirect(True)  # Hide window decorations (title bar, etc.)
root.geometry("200x100")
root.attributes("-alpha", 0.8)  # Set initial transparency level

root.resizable(0 , 0)
#window.maxsize(350, 100)
#window.minsize(350, 100)
#Start the event loop.

#hide the window at first



label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack()


position(root)



root.withdraw()


# make window at top of every program
root.lift()
root.attributes('-topmost',True)
#window.wm_attributes('-fullscreen','true')
root.overrideredirect(True)

# Start capturing keypresses in the background
start_key_capture()
