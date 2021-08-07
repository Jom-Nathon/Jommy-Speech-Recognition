from tkinter import filedialog
from tkinter.constants import BOTH
from speech import fileAudio, micAudio
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox

def main():
    window = tkinter.Tk()
    window.title('Jommy Speech Regonition')

    pane = Frame(window)
    pane.pack(fill = BOTH, expand = True)

    button1 = tkinter.Button(window, text='แปลไฟล์!', command=fromFile)
    button1.pack(expand = True, fill = BOTH)

    button2 = tkinter.Button(window, text='แปลพูด!', command=fromMic)
    button2.pack(expand = True, fill = BOTH)

    window.mainloop()
    
def fromFile():

    folder_path = filedialog.askopenfilename()
    tkinter.Tk().withdraw()

    tkinter.messagebox.showinfo('แปลได้', fileAudio(folder_path))

def fromMic():
    tkinter.messagebox.showinfo('แปลได้', micAudio())

if __name__ == '__main__':
    main()