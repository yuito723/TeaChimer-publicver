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
