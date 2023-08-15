import os
import tkinter
from tkinter import filedialog, colorchooser, font, messagebox
import tkinter.messagebox
import tkinter.filedialog
import json




CONFIG_FOLDER = "config"

def save_settings():
    settings = {
        "font_color": text_area.cget("fg"),
        "bg_color": text_area.cget("bg")
    }

    if not os.path.exists(CONFIG_FOLDER):
        os.makedirs(CONFIG_FOLDER)

    settings_file_path = os.path.join(CONFIG_FOLDER, "editor_settings.json")

    with open(settings_file_path, "w") as settings_file:
        json.dump(settings, settings_file)

def load_settings():
    try:
        settings_file_path = os.path.join(CONFIG_FOLDER, "editor_settings.json")
        with open(settings_file_path, "r") as settings_file:
            settings = json.load(settings_file)
            text_area.config(fg=settings["font_color"])
            text_area.config(fg = settings["font_color"])
            menubar.config(fg=settings["font_color"])
            FileMenu.config(fg=settings["font_color"])
            EditMenu.config(fg=settings["font_color"])
            text_area.config(bg = settings["bg_color"])
            menubar.config(bg=settings["bg_color"])
            FileMenu.config(bg=settings["bg_color"])
            EditMenu.config(bg=settings["bg_color"])
            window.config(bg=settings["bg_color"])
            text_area.config(bg=settings["bg_color"])
    except FileNotFoundError:
        pass


def change_color():
    color = colorchooser.askcolor()
    colorHEX = str(color[1])
    text_area.config(fg = colorHEX)
    menubar.config(fg=colorHEX)
    FileMenu.config(fg=colorHEX)
    EditMenu.config(fg=colorHEX)
    save_settings()


def change_color2():
        color = colorchooser.askcolor()
        colorHEX2 = str(color[1])
        text_area.config(bg = colorHEX2)
        menubar.config(bg=colorHEX2)
        FileMenu.config(bg=colorHEX2)
        EditMenu.config(bg=colorHEX2)
        window.config(bg=colorHEX2)
        save_settings()

    




size_box = None
def fontWindow():
    global size_box
    font_window = tkinter.Toplevel()
    font_window.title("Font Settings")
        
    window_height = 300
    window_width = 300
    screen_width = font_window.winfo_screenwidth()
    screen_height = font_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    font_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))


    font_window.grid_rowconfigure(0, weight=1)
    font_window.grid_columnconfigure(0, weight=1)
    size_box = tkinter.Spinbox(font_window, from_=1, to=100, textvariable=font_size, command=change_font)
    font_box = tkinter.OptionMenu(font_window, font_name, *font.families(), command=change_font)

    tkinter.Label(font_window, text="Font Size : ").pack()
    size_box.pack()
    tkinter.Label(font_window, text="Font Name : ").pack()
    font_box.pack()
        

def change_font(*args):
    global size_box
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled - Merdium Editor")
    text_area.delete(1.0, tkinter.END)

def save_file():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if file is None or file == ():
        return
    else:
        try:
            file = open(file, "w")
            file.write(text_area.get(1.0, tkinter.END))
        except FileNotFoundError:
            pass
            #Mostly Happens When User Presses 'X' Without Choosing File
        except PermissionError:
            messagebox.showerror("Error", "You Don't Have Permission To Acces This File!")
        except Exception as E:
            messagebox.showerror("Unknown error", E)
        else:
            window.title(os.path.basename(file) + " - Merdium Editor")
            file.close()



def save2(event):
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if file is None:
        return
    else:
        try:
            file = open(file, "w")
            file.write(text_area.get(1.0, tkinter.END))
        except FileNotFoundError:
            pass
            #Mostly Happens When User Presses 'X' Without Choosing File
        except PermissionError:
            messagebox.showerror("Error", "You Don't Have Permission To Acces This File!")
        except Exception as E:
            messagebox.showerror("Unknown Error", E)
        else:
            window.title(os.path.basename(file) + " - Merdium Editor")
            file.close()


def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[ ("Text Files", "*.txt"), ("All Files", "*.*")])
    try:
        text_area.delete(1.0, tkinter.END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())
    except FileNotFoundError:
            pass
            #Mostly Happens When User Presses 'X' Without Choosing File
    except PermissionError:
            messagebox.showerror("Error", "You Don't Have Permission To Acces This File!")
    except Exception as E:
            messagebox.showerror("Unknown Error", E)
    else:
        file.close()
        window.title(os.path.basename(file))


def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def select_all(event=None):
    text_area.tag_add("sel", "1.0", "end")

def about():
    messagebox.showinfo("About", "This Is A Program Written In Python Using Tkinter Module To Exercise GUI Skills.")

def quit():
    messagebox.askyesno("Warning", "Are You Sure You Want To Quit?\nAny Unsaved Data Will Be Lost.",icon="warning")
    window.destroy()

def addOne(event=None):
    text_area.event_generate(")");

def addTwo(event=None):
    text_area.event_generate("}");


def addThree(event=None):
    text_area.event_generate("]")




window = tkinter.Tk()
window.title("Merdium Editor")


window_height = 500
window_width = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
file = None



font_name = tkinter.StringVar(window)
font_name.set("Arial")


font_size = tkinter.StringVar(window)
font_size.set("25")

text_area = tkinter.Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = tkinter.Scrollbar(text_area)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

frame = tkinter.Frame(window)
frame.grid()







menubar = tkinter.Menu(window, font=(font_name.get(), font_size.get()))

FileMenu = tkinter.Menu(menubar, tearoff=0)
EditMenu = tkinter.Menu(menubar, tearoff=0)
HelpMenu = tkinter.Menu(menubar, tearoff=0)



window.config(menu=menubar)
menubar.add_cascade(label="File", menu=FileMenu)
menubar.add_cascade(label="Edit", menu=EditMenu)
menubar.add_cascade(label="Help", menu=HelpMenu)

FileMenu.add_command(label="Open File", command=open_file)
FileMenu.add_command(label="Save", command=save_file)
FileMenu.add_command(label="New", command=new_file)
FileMenu.add_separator
FileMenu.add_command(label="Exit", command=quit)

EditMenu.add_command(label="Change Font Color", command=change_color)
EditMenu.add_command(label="Change Background Color", command=change_color2)
EditMenu.add_command(label="Font Settings", command=fontWindow)
EditMenu.add_separator()
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
EditMenu.add_command(label="Select all", command=select_all)



HelpMenu.add_command(label="About", command=about)


scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text_area.config(yscrollcommand=scroll_bar.set)

window.bind('<Control-s>',save2)
window.bind("<Control-a>", select_all)
window.bind("(", addOne)
window.bind("{", addTwo)
window.bind("[", addThree)

load_settings()

window.mainloop()