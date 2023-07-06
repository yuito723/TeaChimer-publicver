##################################################
#           TeaChimer-publicver-v2.0.1           #
##################################################
# (C) 2023 Contributors to the TeaChimer project #
##################################################
# TeaChimer is free software:                    #
# you can redistribute it and/or modify it       #
# under the terms of                             #
# the GNU General Public License as published    #
# by the Free Software Foundation,               #
# either version 3 of the License,               #
# or (at your option) any later version.         #
#                                                #
# This program is distributed in the hope        #
# that it will be useful,                        #
# but WITHOUT ANY WARRANTY;                      #
# without even the implied warranty              #
# of MERCHANTABILITY or FITNESS                  #
# FOR A PARTICULAR PURPOSE.                      #
# See the GNU General Public License             #
# for more details.                              #
#                                                #
# You should have received a copy of             #
# the GNU General Public License                 #
# along with this program. If not, see           #
# <https://www.gnu.org/licenses/>.               #
##################################################
# ライセンスについて
##################################################
# TeaChimerはオープンソースソフトウェアであり、
# GNU General Public License v3.0に基づいて
# 再配布したり改変したりできます。
# (C) 2023 Contributors to the TeaChimer project.
# また、このプログラムに付属している音声データは、
# VOICEVOXで作成したずんだもんの音声を使用しています。
##################################################

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
import pygame
import time
import math

class SoundBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("TeaChimer-publicver-v2.0.1")
        self.master.attributes("-fullscreen", True)
        self.master.configure(background="white")
        self.master.iconbitmap(default="./logo/logo3.ico")
        self.master.focus_force()

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure('Custom.TNotebook.Tab', padding=(30,10), font=('Noto Sans JP', 25))
        style.configure('Custom.TNotebook', background="white")
        self.notebook.configure(style='Custom.TNotebook')

        self.info()

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

        self.key_exit()

    def info(self):
        sub = tk.Toplevel(self.master)
        sub.title("TeaChimer-publicver-v2.0.1")
        sub.overrideredirect(True)
        sub.attributes("-topmost", True)
        sub.attributes("-alpha", 0.75)
        sub.configure(background="white")

        window_width = 1000
        window_height = 250
        screen_width = sub.winfo_screenwidth()
        screen_height = sub.winfo_screenheight()
        x = math.ceil((screen_width - window_width) / 2)
        y = math.ceil((screen_height - window_height) / 2)
        sub.geometry(f"{window_width}x{window_height}+{x}+{y}")

        sub.after(7000, sub.destroy)

        image = tk.PhotoImage(file="./logo/s-logo1.png")
        image_label = tk.Label(sub, image=image, background="white")
        image_label.image = image
        image_label.grid(row=0, column=0, padx=5, pady=5)

        text = "TeaChimer-publicver-v2.0.1"
        text_label = tk.Label(sub, text=text, font=("Noto Sans JP", 25, "bold"), background="white")
        text_label.grid(row=1, column=0, padx=5, pady=5)

        text = "TeaChimerはオープンソースソフトウェアであり、\nGNU General Public License v3.0に基づいて\n再配布したり改変したりできます。\n(C) 2023 Contributors to the TeaChimer project.\nまた、このプログラムに付属している音声データは、\nVOICEVOXで作成した\nずんだもんの音声を使用しています。"
        text_label = tk.Label(sub, text=text, font=("Noto Sans JP", 13, "bold"), background="white")
        text_label.grid(row=0, column=1, padx=5, pady=5)

        text = "このプログラムは「Ctrl」キー＋「e」キーで\n終了することができます。"
        text_label = tk.Label(sub, text=text, font=("Noto Sans JP", 13, "italic", "bold"), background="white")
        text_label.grid(row=1, column=1, padx=5, pady=5)

    def create_page1(self):
        page1 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page1, text="あ行")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page1, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page1.grid_rowconfigure(0, weight=1)
        page1.grid_rowconfigure(1, weight=1)
        page1.grid_rowconfigure(2, weight=1)
        page1.grid_rowconfigure(3, weight=1)
        page1.grid_rowconfigure(4, weight=1)
        page1.grid_columnconfigure(0, weight=1)
        page1.grid_columnconfigure(1, weight=1)
        page1.grid_columnconfigure(2, weight=1)
        page1.grid_columnconfigure(3, weight=1)
        page1.grid_columnconfigure(4, weight=1)

    def create_page2(self):
        page2 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page2, text="か行")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page2, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page2.grid_rowconfigure(0, weight=1)
        page2.grid_rowconfigure(1, weight=1)
        page2.grid_rowconfigure(2, weight=1)
        page2.grid_rowconfigure(3, weight=1)
        page2.grid_rowconfigure(4, weight=1)
        page2.grid_columnconfigure(0, weight=1)
        page2.grid_columnconfigure(1, weight=1)
        page2.grid_columnconfigure(2, weight=1)
        page2.grid_columnconfigure(3, weight=1)
        page2.grid_columnconfigure(4, weight=1)

    def create_page3(self):
        page3 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page3, text="さ行")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page3, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page3.grid_rowconfigure(0, weight=1)
        page3.grid_rowconfigure(1, weight=1)
        page3.grid_rowconfigure(2, weight=1)
        page3.grid_rowconfigure(3, weight=1)
        page3.grid_rowconfigure(4, weight=1)
        page3.grid_columnconfigure(0, weight=1)
        page3.grid_columnconfigure(1, weight=1)
        page3.grid_columnconfigure(2, weight=1)
        page3.grid_columnconfigure(3, weight=1)
        page3.grid_columnconfigure(4, weight=1)

    def create_page4(self):
        page4 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page4, text="た行")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page4, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page4.grid_rowconfigure(0, weight=1)
        page4.grid_rowconfigure(1, weight=1)
        page4.grid_rowconfigure(2, weight=1)
        page4.grid_rowconfigure(3, weight=1)
        page4.grid_rowconfigure(4, weight=1)
        page4.grid_columnconfigure(0, weight=1)
        page4.grid_columnconfigure(1, weight=1)
        page4.grid_columnconfigure(2, weight=1)
        page4.grid_columnconfigure(3, weight=1)
        page4.grid_columnconfigure(4, weight=1)

    def create_page5(self):
        page5 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page5, text="な行")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page5, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page5.grid_rowconfigure(0, weight=1)
        page5.grid_rowconfigure(1, weight=1)
        page5.grid_rowconfigure(2, weight=1)
        page5.grid_rowconfigure(3, weight=1)
        page5.grid_rowconfigure(4, weight=1)
        page5.grid_columnconfigure(0, weight=1)
        page5.grid_columnconfigure(1, weight=1)
        page5.grid_columnconfigure(2, weight=1)
        page5.grid_columnconfigure(3, weight=1)
        page5.grid_columnconfigure(4, weight=1)

    def create_page6(self):
        page6 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page6, text="は行")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page6, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page6.grid_rowconfigure(0, weight=1)
        page6.grid_rowconfigure(1, weight=1)
        page6.grid_rowconfigure(2, weight=1)
        page6.grid_rowconfigure(3, weight=1)
        page6.grid_rowconfigure(4, weight=1)
        page6.grid_columnconfigure(0, weight=1)
        page6.grid_columnconfigure(1, weight=1)
        page6.grid_columnconfigure(2, weight=1)
        page6.grid_columnconfigure(3, weight=1)
        page6.grid_columnconfigure(4, weight=1)

    def create_page7(self):
        page7 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page7, text="ま行")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page7, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page7.grid_rowconfigure(0, weight=1)
        page7.grid_rowconfigure(1, weight=1)
        page7.grid_rowconfigure(2, weight=1)
        page7.grid_rowconfigure(3, weight=1)
        page7.grid_rowconfigure(4, weight=1)
        page7.grid_columnconfigure(0, weight=1)
        page7.grid_columnconfigure(1, weight=1)
        page7.grid_columnconfigure(2, weight=1)
        page7.grid_columnconfigure(3, weight=1)
        page7.grid_columnconfigure(4, weight=1)

    def create_page8(self):
        page8 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page8, text="や行")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page8, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page8.grid_rowconfigure(0, weight=1)
        page8.grid_rowconfigure(1, weight=1)
        page8.grid_rowconfigure(2, weight=1)
        page8.grid_rowconfigure(3, weight=1)
        page8.grid_rowconfigure(4, weight=1)
        page8.grid_columnconfigure(0, weight=1)
        page8.grid_columnconfigure(1, weight=1)
        page8.grid_columnconfigure(2, weight=1)
        page8.grid_columnconfigure(3, weight=1)
        page8.grid_columnconfigure(4, weight=1)

    def create_page9(self):
        page9 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page9, text="ら行")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page9, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page9.grid_rowconfigure(0, weight=1)
        page9.grid_rowconfigure(1, weight=1)
        page9.grid_rowconfigure(2, weight=1)
        page9.grid_rowconfigure(3, weight=1)
        page9.grid_rowconfigure(4, weight=1)
        page9.grid_columnconfigure(0, weight=1)
        page9.grid_columnconfigure(1, weight=1)
        page9.grid_columnconfigure(2, weight=1)
        page9.grid_columnconfigure(3, weight=1)
        page9.grid_columnconfigure(4, weight=1)

    def create_page10(self):
        page10 = tk.Frame(self.notebook, background="white")
        self.notebook.add(page10, text="わ行")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        tk.Button(page10, text="先生", font=("Noto Sans JP", 20), width=10, height=3, command=lambda: self.play_sound("./system/sample.wav")).grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        page10.grid_rowconfigure(0, weight=1)
        page10.grid_rowconfigure(1, weight=1)
        page10.grid_rowconfigure(2, weight=1)
        page10.grid_rowconfigure(3, weight=1)
        page10.grid_rowconfigure(4, weight=1)
        page10.grid_columnconfigure(0, weight=1)
        page10.grid_columnconfigure(1, weight=1)
        page10.grid_columnconfigure(2, weight=1)
        page10.grid_columnconfigure(3, weight=1)
        page10.grid_columnconfigure(4, weight=1)

    def create_navigation_frame(self):
        frame = tk.Frame(self.master, background="white")
        frame.pack()
        tk.Message(frame, text="音声が流れている間は他のボタンを押さないでください。", background="white", font=("Noto Sans JP", 20), width="1000").grid(row=0, column=1, padx=5, pady=5)

    def key_exit(self):
        self.master.bind("<Control-e>", self.confirm_exit)

    def confirm_exit(self ,event):
        result = mbox.askyesno("TeaChimer-publicver-v2.0.1", "TeaChimerを終了しますか？")
        if result:
            self.master.destroy()

    def play_sound(self, file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)
        pygame.mixer.music.play()

root = tk.Tk()
app = SoundBoard(root)
root.mainloop()