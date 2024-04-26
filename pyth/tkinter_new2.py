import tkinter as tk

root  = tk.Tk()

stopwatch = tk.Label(root ,
                  text = 'test',
                  font = 'arial 100')

stopwatch.pack()

seconds = 0
minutes = 0

def change_stopwatch():
    global seconds
    global minutes

    if seconds < 59:
        seconds += 1

    elif seconds == 59:
        seconds = 0
        minutes =minutes +1

    time_text = "{:02d}:{:02d}".format(minutes, seconds)
    stopwatch.config(text = time_text)
    root.after(1000, change_stopwatch)

change_stopwatch()
    
