################################################
# ©️ 2023 Contributors to the TeaChimer project #
################################################

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
import pygame

class SoundBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("TeaChimer-pulicver-1.00")
        self.master.attributes("-fullscreen", True)
        self.master.configure(background="white")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure('Custom.TNotebook.Tab', color="red", padding=(30,10), font=('Noto Sans JP', 25))
        style.configure('Custom.TNotebook', background="white")
        self.notebook.configure(style='Custom.TNotebook')

        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()
        self.create_page5()
        self.create_page6()
        self.create_page7()
        self.create_page8()
        self.create_page9()
        self.create_page10()

        self.create_navigation_frame()
