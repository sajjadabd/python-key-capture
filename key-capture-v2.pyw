import tkinter as tk
from pynput import keyboard

import math

from win32api import GetMonitorInfo, MonitorFromPoint


monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")

taskbar_height = monitor_area[3]-work_area[3]

#print("The taskbar height is {}.".format())

fade_requests = 0


key_capture_string = ""

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
    try :
        if hasattr(key, 'char'):
            char = key.char 
        else : 
            char = str(key)
        print(char)
        show_key(char)
    except :
        print("error happens!")
        
    
    
    

def on_key_release(key):
    pass

def show_key(char):
    global fade_requests
    global key_capture_string
    root.deiconify()
    
    
    """
    Key.ctrl_l
    Key.ctrl_r
    Key.alt_l
    Key.alt_gr
    Key.space
    Key.alt_gr
    Key.alt_l
    Key.cmd_r
    Key.enter
    Key.num_lock
    Key.num_lock
    Key.caps_lock
    Key.caps_lock
    Key.tab
    Key.shift
    Key.shift_r
    Key.ctrl_l
    Key.ctrl_l
    Key.ctrl_l
    Key.ctrl_l
    Key.ctrl_l
    """
    
    if char == "Key.ctrl_l" or char == "Key.ctrl_r" :
        ctrl.place(relx=0.1, rely=0.5, anchor="center")
        ctrl.config(text="CTRL",relief=tk.SOLID, borderwidth=2)
    else :
        ctrl.place_forget()
        
        
    if char == "Key.alt_l" or char == "Key.alt_gr" :
        alt.place(relx=0.2, rely=0.5, anchor="center")
        alt.config(text="ALT",relief=tk.SOLID, borderwidth=2)
    else :
        alt.place_forget()
    
    
    if char == "Key.shift" or char == "Key.shift_r" :
        shift.place(relx=0.3, rely=0.5, anchor="center")
        shift.config(text="SHIFT",relief=tk.SOLID, borderwidth=2)
    else :
        shift.place_forget()
    
    
    
    
    if char == "Key.space" :
        key_capture_string += " "
    elif char == "Key.backspace" :
        key_capture_string = key_capture_string[0:len(key_capture_string)-1]
    elif char.startswith("Key") :
        pass
    else : 
        try :
            if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) :
                key_capture_string += char
        except :
            pass
        
    
    #,relief=tk. SOLID, borderwidth=2
    if key_capture_string == "" :
        label.config(text=key_capture_string,relief=tk.SOLID, borderwidth=0)
    else :
        label.config(text=key_capture_string,relief=tk.SOLID, borderwidth=2)
        
    
    label.place(relx=0.5, rely=0.5, anchor="center")
    

    fade_requests += 1
    label.after(2000, fade_out)

def fade_out():
    global fade_requests
    global key_capture_string
    #print(fade_requests)
    if fade_requests > 0 :
        fade_requests -= 1
    
    if fade_requests == 0 :
        key_capture_string = ""
        root.withdraw()
        #root.withdraw()
        label.place_forget()
        ctrl.place_forget()
        alt.place_forget()
        shift.place_forget()
    
    return
    

def start_key_capture():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        root.mainloop()

root = tk.Tk()
root.overrideredirect(True)  # Hide window decorations (title bar, etc.)
root.geometry( "{}x{}+{}+{}".format( root.winfo_screenwidth() , 100 , 0 , root.winfo_screenheight() - 100 - taskbar_height  ) )
root.attributes("-alpha", 0.8)  # Set initial transparency level

root.resizable(0 , 0)
#window.maxsize(350, 100)
#window.minsize(350, 100)
#Start the event loop.

#hide the window at first



label = tk.Label(root, text="", font=("Helvetica", 24))

ctrl = tk.Label(root, text="CTRL", font=("Helvetica", 24))
alt = tk.Label(root, text="ALT", font=("Helvetica", 24))
shift = tk.Label(root, text="SHIFT", font=("Helvetica", 24))


label.pack()


#position(root)



root.withdraw()


# make window at top of every program
root.lift()
root.attributes('-topmost',True)
#window.wm_attributes('-fullscreen','true')
root.overrideredirect(True)

# Start capturing keypresses in the background
start_key_capture()
