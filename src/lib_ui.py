'''
    Simple User Interface to create image Recognization Application

Author:

V Natarajan (a) Viki
www.viki.design

'''

'''

Dependencies

sudo apt-get install python3-pil.imagetk
sudo apt-get install python3-pil.imagetk
sudo pip3 install Pillow


'''
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk
from lib_logger import *
import sys
log             = logger()


try:
    resample = Image.Resampling.LANCZOS  # Pillow >= 10.0
except AttributeError:
    resample = Image.LANCZOS  # Pillow < 10.0


font_list=['texgyretermes', 'fangsong ti', 'fixed', 'clearlyu alternate glyphs', 'latin modern roman', 'open look glyph', 'texgyrechorus', 'latin modern  typewriter', 'song ti', 'open look cursor', 'newspaper', 'texgyrecursor', 'clearlyu ligature', 'mincho', 'clearlyu devangari extra', 'clearlyu pua',      'texgyreheros', 'texgyrebonum', 'clearlyu', 'texgyreschola', 'latin modern typewriter variable width', 'latin modern sans', 'texgyreadventor', 'clean',   'nil', 'clearlyu arabic', 'clearlyu devanagari', 'texgyrepagella', 'latin modern sansquotation', 'gothic', 'clearlyu arabic extra']


#Compatibility handling
try:
    resample = Image.Resampling.LANCZOS
except AttributeError:
    resample = Image.ANTIALIAS  # For Pillow <10

ctr = 0

__Input_Image_Name__ = ""
__ColorCode__ = 0

__canvas1__ = None
__canvas2__ = None

#expects a function external_callback(file_name)

def set_input_image(name):
    global __Input_Image_Name__
    __Input_Image_Name__ = name

def get_input_image():
    return __Input_Image_Name__

def classify_image_callback(gui, canvas, external_callback):
    global __canvas1__, __canvas2__
    global __ColorCode__
    canvas.delete("all")
    classified_output = "None"
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    fname = get_input_image()

    if __ColorCode__ == 0:
        color = "gray44"
        __ColorCode__=1
    else:
        color = "gray90"
        __ColorCode__=0

    if not external_callback or not fname:
        print("info(): no external callback");
        classified_output = "NO CALLBACK / NO INPUT"
        font_size = 30
    else:
        classified_output = external_callback(fname)
        font_size = 120

    s = str(classified_output)
    canvas.create_text(   canvas_width/2, canvas_height/2, font=(font_list[0], font_size),
                            text=s, fill=color
                            )

    return

from PIL import Image, ImageTk

def browse_image_callback(gui, canvas, fname):
    global __canvas1__, __canvas2__, open_path
    canvas.delete("all")
    __canvas2__.delete("all")

    try:
        fname = filedialog.askopenfilename(initialdir=open_path)
    except:
        print("error(): file browse")
        return

    if not fname:
        print("info(): file name is empty")
        set_input_image(None)
        return

    print("file_name = " + fname)
    set_input_image(fname)

    try:
        image = Image.open(fname)
    except:
        print("error(): fopen")
        return

    # Ensure canvas is rendered
    canvas.update_idletasks()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Fallback if canvas hasn't been fully displayed yet
    if canvas_width < 10 or canvas_height < 10:
        canvas_width = 300
        canvas_height = 300

    # Target size: 70% of canvas
    target_width = int(canvas_width * 0.7)
    target_height = int(canvas_height * 0.7)

    # Maintain aspect ratio
    img_width, img_height = image.size
    img_ratio = img_width / img_height
    target_ratio = target_width / target_height

    if img_ratio > target_ratio:
        new_width = target_width
        new_height = max(1, int(new_width / img_ratio))
    else:
        new_height = target_height
        new_width = max(1, int(new_height * img_ratio))

    # Safe resampling
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS

    resized = image.resize((new_width, new_height), resample)
    photo = ImageTk.PhotoImage(resized)

    # Show image in center of canvas
    canvas.image = photo
    canvas.create_image(
        canvas_width // 2,
        canvas_height // 2,
        image=photo,
        anchor='center'
    )

def browse_image_frame(gui, canvas, fname):
    frame1 = tk.Frame(gui, width=500, height=500, bd=2, background='#2d2d2d')
    frame1.grid(row=1, column=0)
    canvas = tk.Canvas(frame1, height=390, width=490,
                       background="#1e1e1e", bd=4, relief=tk.RAISED,
                       highlightthickness=0)
    canvas.grid(row=1,column=0)
    b_image = tk.Button(master=frame1,
                        text='Browse Image',
                        height=2, width=15,
                        command=lambda: browse_image_callback(gui, canvas, fname),
                        background='#3c3c3c',
                        foreground='#dcdcdc',
                        activebackground='#505050',
                        activeforeground='#ffffff',
                        highlightbackground='#444444',
                        highlightcolor='#aaaaaa'
                        )
    b_image.grid(row=0, column=0, padx=4, pady=4)
    return canvas

def classify_image_frame(gui, canvas, external_callback):
    frame2 = tk.Frame(gui, width=500, height=500, bd=2, background='#2d2d2d')
    frame2.grid(row=1, column=1)
    canvas = tk.Canvas(frame2, height=390, width=490,
                       background="#1e1e1e", bd=4, relief=tk.SUNKEN,
                       highlightthickness=0)
    canvas.grid(row=1,column=1)
    b_classify = tk.Button(master=frame2,
                           text='Classify Image',
                           height=2,
                           width=15,
                           command=lambda: classify_image_callback(gui, canvas, external_callback),
                           background='#3c3c3c',
                           foreground='#dcdcdc',
                           activebackground='#505050',
                           activeforeground='#ffffff',
                           highlightbackground='#444444',
                           highlightcolor='#aaaaaa'
                           )
    b_classify.grid(row=0, column=1, padx=4, pady=4)
    return canvas

def render(external_callback, default_images_path):
    global __canvas1__, __canvas2__, open_path
    fname = ""
    open_path=default_images_path
    canvas_1 = None
    canvas_2 = None
    gui = tk.Tk()
    gui.configure(bg='#1e1e1e')  # main window background
    gui.wm_title("CONVOLUTIONAL NEURAL NETWORK IMAGE CLASSIFIER")

    # Handle close button
    def on_close():
        print(log._if+"Closing UI")
        gui.destroy()
        sys.exit(0)

    gui.protocol("WM_DELETE_WINDOW", on_close)

    # Bind 'q' key to quit
    def on_key_press(event):
        if event.char == 'q':
            print(log._if+"Key press detected ('q') : Closing GUI.")
            gui.destroy()
            sys.exit(0)

    gui.bind("<Key>", on_key_press)

    canvas_1 = browse_image_frame(gui, canvas_1, fname)
    canvas_2 = classify_image_frame(gui, canvas_2, external_callback)
    __canvas1__ = canvas_1
    __canvas2__ = canvas_2
    tk.mainloop()


