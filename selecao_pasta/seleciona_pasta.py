#!.\.env python3

from tkinter import Tk, filedialog
def seleciona_pasta():
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.

    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    open_file = filedialog.askdirectory() # Returns opened path as str
    return open_file