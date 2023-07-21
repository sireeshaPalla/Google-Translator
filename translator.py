from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator

root=Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background="skyblue")

#icon
image_icon=PhotoImage(file="translatoricon")
root.iconphoto(False,image_icon)
root.mainloop()
