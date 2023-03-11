import tkinter as tk

# establish root window
root = tk.Tk()

# change window title
root.title("Root window")

# get screen/desktop size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# change window size
# the window will be 800 long, 700 tall, moved 100 to the right and moved 400 downwards.
root.geometry("800x700+100+300")

# sets if the window is allowed to be resized horizontally and/or vertically
# This makes the window have fixed width but variable height
root.resizable(False,True)

# Tkinter allows you to specify the transparency of a window by setting its alpha channel ranging from 0.0 (fully transparent) to 1.0 (fully opaque):
root.attributes('-alpha',0.9)

# To ensure that a window is always at the top of the stacking order, you can use the -topmost attribute like this:
# window.attributes('-topmost', 1)

# To move a window up or down of the stack, you can use the lift() and lower() methods:
# window.lift()
# window.lift(another_window)

# window.lower()
# window.lower(another_window)

# When a window is resizable, you can specify the minimum and maximum sizes using the minsize() and maxsize() methods:
root.minsize(800, 700)
root.maxsize(800, 1000)

# Tkinter window displays a default icon. To change this default icon, you put a .ico file near the program file, and run
# root.iconbitmap('./myicon.ico')


# If on windows things might be blurry. as a precaution you could do:
import sys
if sys.platform.startswith('win'):
  from ctypes import windll
  windll.shcore.SetProcessDpiAwareness(1)


## Using ttk

# packages:
'''
https://www.pythontutorial.net/tkinter/tkinter-button/
https://www.pythontutorial.net/tkinter/tkinter-checkbox/
https://www.pythontutorial.net/tkinter/tkinter-entry/
https://www.pythontutorial.net/tkinter/tkinter-frame/
https://www.pythontutorial.net/tkinter/tkinter-label/
https://www.pythontutorial.net/tkinter/tkinter-labelframe/
https://www.pythontutorial.net/tkinter/tkinter-menubutton/
https://www.pythontutorial.net/tkinter/tkinter-panedwindow/
https://www.pythontutorial.net/tkinter/tkinter-radio-button/
https://www.pythontutorial.net/tkinter/tkinter-slider/
https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
https://www.pythontutorial.net/tkinter/tkinter-spinbox/
https://www.pythontutorial.net/tkinter/tkinter-combobox/
https://www.pythontutorial.net/tkinter/tkinter-notebook/
https://www.pythontutorial.net/tkinter/tkinter-progressbar/
https://www.pythontutorial.net/tkinter/tkinter-separator/
https://www.pythontutorial.net/tkinter/tkinter-sizegrip/
https://www.pythontutorial.net/tkinter/tkinter-treeview/
'''

# I'll do an example that uses the button widget.
from tkinter import ttk

def fUNCTION():
  from tkinter.messagebox import showinfo
  showinfo(
        title='Information',
        message='Goodbye, world'
   )
  # quit a window
  root.quit()

# exit button
exit_button = ttk.Button(root,text='Exit',command=fUNCTION)
exit_button.pack()

# set the disabled flag
exit_button.state(['disabled'])

# remove the disabled flag
exit_button.state(['!disabled'])



## Event binding

# for more event binging, see https://www.pythontutorial.net/tkinter/tkinter-event-binding/


def binding1(event):
    print('Return key pressed.')
    print('Binding function 1 called.')


def binding2(event):
    print('Binding function 2 called.')


btn = ttk.Button(root, text='Activate my function with the enter key')
btn.bind('<Return>', binding1)
# use add='+' when creating additional bindings
btn.bind('<Return>', binding2, add='+')
btn.pack()
# make the button be focused
btn.focus()

# Tkinter also allows you to bind an event to the top-level window.
root.bind_class('Button', '<Alt-V>', binding2)



# Tkinter Label widget is used to display a text or image on the screen. To use a Label widget, you use the following general syntax:
# label = ttk.Label(container, **options)
from tkinter.ttk import Label

# font
font=("Helvetica", 24)


label = Label(root, font=font, text='Hello world!')
label.pack(ipadx=5, ipady=5, expand=True)

## Displayin images
try:
  photo = tk.PhotoImage(file='./myimage.png')

  # use Label() to create an image
  image = ttk.Label(root,image=photo, padding=5)
  # .pack to shoe image
  # image.pack()


  '''
  The compound option specifies the position of the image relative to the text. Its valid values are:

  Compound Effect
  'top'    Display the image above the text.
  'bottom' Display the image below the text.
  'left'   Display the image to the left of the text.
  'right'  Display the image to the right of the text.
  'none'   Display the image if there’s one, otherwise display the text. The compound option defaults to 'none'.
  'text'   Display the text, not the image
  'image'  Display the image, not the text.
  '''
  imagewithtext = ttk.Label(root,image=photo,text='HYPIXEL',padding=5,compound='left')
  imagewithtext.pack()
except:
  pass

# keep the window displaying
root.mainloop()


# That's about it for a brief preview.
# See the tutorials for ttk modules to learn more about creating usefyl UI interfaces with tkinter.

# tkinter.colorchooser — Color choosing dialog
# tkinter.font — Tkinter font wrapper
# tkinter.messagebox — Tkinter message prompts
# tkinter.scrolledtext — Scrolled Text Widget
# tkinter.dnd — Drag and drop support
# tkinter.ttk — Tk themed widgets
# tkinter.tix — Extension widgets for Tk