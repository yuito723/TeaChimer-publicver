"""
TeaChimer-publicver-v3.0.0
(C) 2023 Contributors to the TeaChimer project

This file is part of TeaChimer.
"""

import tkinter as tk
import tkinter.ttk as ttk
import winsound

class Main():
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.attributes("-topmost", True)
        self.master.iconbitmap("./system/logo-1_icon.ico")
        self.master.title(f"TeaChimer-{version}_MAIN")
        self.master.configure(background = "white")
        self.master.focus_force()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background = "white")
        style.configure("TLabel", font = ("Yu Gothic UI", 15), anchor = "center", background = "white")
        style.configure("startup_ver.TLabel", font = ("Yu Gothic UI", 20, "bold"), anchor = "center", background = "white")
        style.configure("logo.TLabel", background = "white")
        style.configure("notice.TLabel", font = ("Yu Gothic UI", 30, "bold"), anchor = "center", background = "white")
        style.configure("TButton", font = ("Yu Gothic UI", 25, "bold"), background = "whitesmoke")
        style.map("TButton", background = [("active", "whitesmoke"), ("disabled", "lightgray")])

        self.startup()

        self.header()
        self.main()

        self.master.bind("<Control-q>", self.exit)

    def startup(self):
        startup = tk.Toplevel()
        startup.attributes("-fullscreen", True)
        startup.attributes("-topmost", True)
        startup.attributes("-alpha", 0.75)
        startup.iconbitmap("./system/logo-1_icon.ico")
        startup.title(f"TeaChimer-{version}_STARTUP")
        startup.configure(background = "whitesmoke")

        startup.after(7000, startup.destroy)

        startup_frame = ttk.Frame(startup, style = "TFrame")
        startup_frame.place(x = (screen_width - 800) / 2, y = (screen_height - 150) / 2, width = 800, height = 150)

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(startup_frame, image = logo, style = "logo.TLabel")
        logo_label.place(x = 0, y = 0, width = 300 + 70, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}"
        ver_label = ttk.Label(startup_frame, text = ver, style = "startup_ver.TLabel")
        ver_label.place(x = 0, y = 100, width = 300 + 70, height = 150 - 100)

        text = "TeaChimerはオープンソースソフトウェアであり、\nGNU General Public License v3.0に基づいて\n再配布したり改変したりできます\n(C) 2023 Contributors to the TeaChimer project\n終了：「Ctrl」キー＋「Q」キー"
        text_label = ttk.Label(startup_frame, text = text, style = "TLabel")
        text_label.place(x = 300 + 70, y = 0, width = 800 - 300 - 70, height = 150)

    def header(self):
        header = ttk.Frame(style = "TFrame")
        header.place(x = 0, y = 0, width = screen_width, height = 100)

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(header, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{school_name}\n{admin_name}"
        ver_label = ttk.Label(header, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = "呼びたい先生のボタンを押してください"
        text_label = ttk.Label(header, text = text, style = "notice.TLabel")
        text_label.place(x = 10 + 300 + 10 + 300, y = 0, width = screen_width - 10 - 300 - 10 - 300, height = 100)

    def main(self):
        main = ttk.Frame(padding = 5, style = "TFrame")
        main.place(x = 0, y = 100, width = screen_width, height = screen_height - 100)

        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 5, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 5, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 5, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main, text = "先生", state = "先生", command = lambda: self.confirm("先生", "./system/sample.wav"), style = "TButton").grid(row = 5, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main.grid_rowconfigure(5, minsize = button_height, weight = 1)
        main.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main.grid_columnconfigure(4, minsize = button_width, weight = 1)

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
        ver_label = ttk.Label(confirm, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = f"{name}を呼びますか？"
        text_label = ttk.Label(confirm, text = text, style = "notice.TLabel")
        text_label.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - 50 - 10 - button_height) / 2), width = (button_width * 2) + 10, height = 50 + 10)

        text = "はい"
        button = ttk.Button(confirm, text = text, command = lambda: self.playsound(confirm, name, path), style = "TButton")
        button.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - 50 - 10 - button_height) / 2) + 50 + 10, width = button_width, height = button_height)

        text = "いいえ"
        button = ttk.Button(confirm, text = text, command = confirm.destroy, style = "TButton")
        button.place(x = ((screen_width - button_width * 2 - 10) / 2) + button_width + 10, y = 100 + ((screen_height - 100 - 50 - 10 - button_height) / 2) + 50 + 10, width = button_width, height = button_height)

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
        ver_label = ttk.Label(playsound, text = ver, style = "TLabel")
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
        ver_label = ttk.Label(exit, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = "TeaChimerを終了しますか？"
        text_label = ttk.Label(exit, text = text, style = "notice.TLabel")
        text_label.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - 50 - 10 - button_height) / 2), width = (button_width * 2) + 10, height = 50 + 10)

        text = "はい"
        button = ttk.Button(exit, text = text, command = self.master.destroy, style = "TButton")
        button.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - 50 - 10 - button_height) / 2) + 50 + 10, width = button_width, height = button_height)

        text = "いいえ"
        button = ttk.Button(exit, text = text, command = exit.destroy, style = "TButton")
        button.place(x = ((screen_width - button_width * 2 - 10) / 2) + button_width + 10, y = 100 + ((screen_height - 100 - 50 - 10 - button_height) / 2) + 50 + 10, width = button_width, height = button_height)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
button_width = (screen_width - 10 * 6) / 5
button_height = (screen_height - 100 - 10 * 7) / 6
version = "publicver-v3.0.0"
school_name = "学校名"
admin_name = "管理者名"
app = Main(root)
root.mainloop()
