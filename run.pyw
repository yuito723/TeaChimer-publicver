"""
TeaChimer-publicver-v3.0.0
(C) 2023 Contributors to the TeaChimer project


This file is part of TeaChimer.

TeaChimer is free software: you can redistribute it and/or modify it under the terms of
the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

TeaChimer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with TeaChimer.
If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
import tkinter.ttk as ttk
import winsound

class Main():
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.iconbitmap("./system/logo-1_icon.ico")
        self.master.title(f"TeaChimer-{version}_MAIN")
        self.master.configure(background = "white")
        self.master.focus_force()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background = "white")
        style.configure("TLabel", font = ("Yu Gothic UI", 15), anchor = "center", background = "white")
        style.configure("startup_ver.TLabel", font = ("Yu Gothic UI", 25, "bold"), anchor = "center", background = "white")
        style.configure("startup_notice.TLabel", font = ("Yu Gothic UI", 15), anchor = "center", background = "white")
        style.configure("logo.TLabel", background = "white")
        style.configure("ver.TLabel", font = ("Yu Gothic UI", 15), anchor = "center", background = "white")
        style.configure("notice.TLabel", font = ("Yu Gothic UI", 30, "bold"), anchor = "center", background = "white")
        style.configure("TButton", font = ("Yu Gothic UI", 20, "bold"), background = "whitesmoke")
        style.configure("yesno.TButton", font = ("Yu Gothic UI", 30, "bold"), background = "whitesmoke")
        style.map("TNotebook.Tab", background = [("selected", "white")])
        style.map("TButton", background = [("active", "whitesmoke"), ("disabled", "lightgray")])

        self.startup()

        self.header()
        self.main()

        self.master.bind("<Control-q>", self.exit)
        self.master.bind("<Control-h>", self.open_help)

    def startup(self):
        startup = tk.Toplevel()
        startup.attributes("-fullscreen", True)
        startup.attributes("-topmost", True)
        startup.attributes("-alpha", 0.75)
        startup.iconbitmap("./system/logo-1_icon.ico")
        startup.title(f"TeaChimer-{version}_STARTUP")
        startup.configure(background = "whitesmoke")

        startup.after(3000, startup.destroy)

        startup_frame = ttk.Frame(startup, style = "TFrame")
        startup_frame.place(x = (screen_width - 700) / 2, y = (screen_height - 150) / 2, width = 700, height = 150)

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(startup_frame, image = logo, style = "logo.TLabel")
        logo_label.place(x = 0, y = 0, width = 300 + 20, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}"
        ver_label = ttk.Label(startup_frame, text = ver, style = "startup_ver.TLabel")
        ver_label.place(x = 0, y = 100, width = 300 + 20, height = 150 - 100)

        text = "TeaChimerはオープンソースソフトウェアであり、\nGNU General Public License v3.0に基づいて\n再配布したり改変したりできます\n(C) 2023 Contributors to the TeaChimer project\nヘルプ画面：「Ctrl」キー＋「H」キー"
        text_label = ttk.Label(startup_frame, text = text, style = "startup_notice.TLabel")
        text_label.place(x = 300 + 20, y = 0, width = 700 - 300 - 20, height = 150)

    def header(self):
        header = ttk.Frame(style = "TFrame")
        header.place(x = 0, y = 0, width = screen_width, height = 100)

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(header, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{school_name}\n{admin_name}"
        ver_label = ttk.Label(header, text = ver, style = "ver.TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = "呼びたい先生のボタンを押してください"
        text_label = ttk.Label(header, text = text, style = "notice.TLabel")
        text_label.place(x = 10 + 300 + 10 + 300, y = 0, width = screen_width - 10 - 300 - 10 - 300, height = 100)

    def main(self):
        main = ttk.Frame(main, padding = 5, style = "TFrame")
        main.place(x = 0, y = 100, width = screen_width, height = screen_height - 100)

        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "", state = "", command = lambda: self.confirm("", ""), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main.grid_rowconfigure(0, minsize = (screen_height - 100 - 30 - 10 * 6) / 5, weight = 1)
        main.grid_rowconfigure(1, minsize = (screen_height - 100 - 30 - 10 * 6) / 5, weight = 1)
        main.grid_rowconfigure(2, minsize = (screen_height - 100 - 30 - 10 * 6) / 5, weight = 1)
        main.grid_rowconfigure(3, minsize = (screen_height - 100 - 30 - 10 * 6) / 5, weight = 1)
        main.grid_rowconfigure(4, minsize = (screen_height - 100 - 30 - 10 * 6) / 5, weight = 1)
        main.grid_columnconfigure(0, minsize = (screen_width - 10 * 6) / 5, weight = 1)
        main.grid_columnconfigure(1, minsize = (screen_width - 10 * 6) / 5, weight = 1)
        main.grid_columnconfigure(2, minsize = (screen_width - 10 * 6) / 5, weight = 1)
        main.grid_columnconfigure(3, minsize = (screen_width - 10 * 6) / 5, weight = 1)
        main.grid_columnconfigure(4, minsize = (screen_width - 10 * 6) / 5, weight = 1)

    def confirm(self, name, path):
        confirm = tk.Toplevel()
        confirm.overrideredirect(True)
        confirm.attributes("-topmost", True)
        confirm.iconbitmap("./system/logo-1_icon.ico")
        confirm.title(f"TeaChimer-{version}_CONFIRM")
        confirm.geometry(f"{screen_width}x{screen_height}")
        confirm.configure(background = "white")
        confirm.focus_force()

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(confirm, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{school_name}\n{admin_name}"
        ver_label = ttk.Label(confirm, text = ver, style = "ver.TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = f"{name}を呼びますか？"
        text_label = ttk.Label(confirm, text = text, style = "notice.TLabel")
        text_label.place(x = (screen_width - 700) / 2, y = 100 + (screen_height - 100 - 300) / 2, width = 700, height = 100)

        text = "はい"
        button = ttk.Button(confirm, text = text, command = lambda: self.playsound(confirm, name, path), style = "yesno.TButton")
        button.place(x = (screen_width - 700) / 2, y = 100 + (screen_height - 100 - 300) / 2 + 100, width = (700 - 10) / 2, height = 300 - 100)

        text = "いいえ"
        button = ttk.Button(confirm, text = text, command = confirm.destroy, style = "yesno.TButton")
        button.place(x = (screen_width - 700) / 2 + 10 + (700 - 10 * 3) / 2 + 10, y = 100 + (screen_height - 100 - 300) / 2 + 100, width = (700 - 10) / 2, height = 300 - 100)

    def playsound(self, confirm, name, path):
        playsound = tk.Toplevel()
        playsound.overrideredirect(True)
        playsound.attributes("-topmost", True)
        playsound.iconbitmap("./system/logo-1_icon.ico")
        playsound.title(f"TeaChimer-{version}_PLAYSOUND")
        playsound.geometry(f"{screen_width}x{screen_height}")
        playsound.configure(background = "white")
        playsound.focus_force()

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(playsound, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{school_name}\n{admin_name}"
        ver_label = ttk.Label(playsound, text = ver, style = "ver.TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = f"{name}を呼んでいます"
        text_label = ttk.Label(playsound, text = text, style = "notice.TLabel")
        text_label.place(x = 0, y = 100, width = screen_width, height = screen_height - 100)

        for i in range(2):
            playsound.update()
            winsound.PlaySound(f"{path}", winsound.SND_FILENAME)
            playsound.update()

        confirm.destroy()
        playsound.destroy()

    def exit(self, event):
        exit = tk.Toplevel()
        exit.overrideredirect(True)
        exit.attributes("-topmost", True)
        exit.iconbitmap("./system/logo-1_icon.ico")
        exit.title(f"TeaChimer-{version}_EXIT")
        exit.geometry(f"{screen_width}x{screen_height}")
        exit.configure(background = "white")
        exit.focus_force()

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(exit, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{school_name}\n{admin_name}"
        ver_label = ttk.Label(exit, text = ver, style = "ver.TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = "TeaChimerを終了しますか？"
        text_label = ttk.Label(exit, text = text, style = "notice.TLabel")
        text_label.place(x = (screen_width - 700) / 2, y = 100 + (screen_height - 100 - 300) / 2, width = 700, height = 100)

        text = "はい"
        button = ttk.Button(exit, text = text, command = self.master.destroy, style = "yesno.TButton")
        button.place(x = (screen_width - 700) / 2, y = 100 + (screen_height - 100 - 300) / 2 + 100, width = (700 - 10) / 2, height = 300 - 100)

        text = "いいえ"
        button = ttk.Button(exit, text = text, command = exit.destroy, style = "yesno.TButton")
        button.place(x = (screen_width - 700) / 2 + 10 + (700 - 10 * 3) / 2 + 10, y = 100 + (screen_height - 100 - 300) / 2 + 100, width = (700 - 10) / 2, height = 300 - 100)

    def open_help(self, event):
        self.help()

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
version = "publicver-v3.0.0"
school_name = ""
admin_name = ""
app = Main(root)
root.mainloop()