from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import textblob
from googletrans import  LANGUAGES,Translator
import time

window = Tk()

window.title("Language Translator")
window.minsize(800, 900)
window.maxsize(800, 900)

def translate():
    global language 
    try:
        txt = text1.get(1.0, END)
        c1 = combo1.get()
        c2 = combo2.get()
        print(f"Text: {txt}")
        print(f"Source Language: {c1}")
        print(f"Target Language: {c2}")
        
        if txt and c1 != "choose a language" and c2 != "choose a language":
            text2.delete(0)
            text2.insert(END,"INSERT")
        else:
            messagebox.showwarning("Warning", "Please choose both source and target languages.")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Translation failed. Please try again.")

language = {name: code for code, name in LANGUAGES.items()}

lang_value = list(language.keys())

combo1 = ttk.Combobox(window, values=lang_value, state='r')
combo1.place(x=100, y=20)
combo1.set("choose a language 1 ")

f1 = Frame(window, bg='red', bd=4)
f1.place(x=100, y=100, width=150, height=150)

text1 = Text(f1, font="Roboto 14", bg='light green', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

combo2 = ttk.Combobox(window, values=lang_value, state='r')
combo2.place(x=300, y=20)
combo2.set("choose a language 2 ")

f2 = Frame(window, bg='red', bd=4)
f2.place(x=300, y=100, width=150, height=150)

text2 = Text(f2, font="Roboto 14", bg='purple', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)
text2.insert(END,"THIS")

result = StringVar()

result_label = Label(f2, textvariable=result, font="Roboto 14", bg='white', relief=GROOVE)
result_label.place(x=0, y=0, width=140, height=140)

button = Button(window, text='Translate', font=('fantasy', 15), bg='maroon', command=translate)
button.place(x=230, y=300)

window.mainloop()





