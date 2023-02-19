import Emoji19
import time
import tkinter as tk               
from tkinter import font as tkfont
from PIL import Image, ImageTk
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,bg = 'white', width= 500, height=100)
        
        bg = Image.open("background.jpg")
        test = ImageTk.PhotoImage(bg)
        # Create a label with the image as its background
        label = tk.Label(self, image=test)
        label.image = test
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add other widgets on top of the background
        label1 = tk.Label(self, text="This is the start page", font=controller.title_font, bg="white")
        label1.pack(side="top", pady=150)

        button1 = tk.Button(self, text="Play",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Instructions",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack(side="top")
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="THIS IS AN EMERGENCY! YOUR COMPUTER HAS BEEN HACKED BY THE EMOJI-19 VIRUS.\n IT HAS REPLACED RANDOM WORDS FROM YOUR PC WITH EMOJIS", font=controller.title_font)
        label.pack(side="top")
        inputtxt = tk.Text(self, height = 20, width = 60,)
        inputtxt.pack(side="left", padx= 150)
        lines = open('comprehensive.txt').read().splitlines()
        for line in lines:
            s = Emoji19.encrypt_phrase(line)
            label = tk.Label(self, text= s)
            time.sleep(2)
            label.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
