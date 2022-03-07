import tkinter as tk

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800
CANVAS_BG = "#0d1a2b"
CANVAS_FG = 'yellow'
CANVAS_FONT = 'Arial'
CANVAS_FONT_SIZE = 18
DLT_BTN_FG = 'red'

window = tk.Tk()
window.title('営業チームのデーリー')
window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
window.resizable(False, False)

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)

nameList = []

def on_delete(index):
  if(index >= len(nameList)):
    return
  nameList.pop(index)
  
  for widget in canvas.winfo_children():
    widget.destroy()
    
  create_labels(0)
  

def create_labels(index):
  if(index == len(nameList)):
    return
    
  tk.Label(
    canvas,
    text=nameList[index],
    bg=CANVAS_BG,
    fg=CANVAS_FG,
    font=(CANVAS_FONT, CANVAS_FONT_SIZE)
  ).place(x=150, y=(index+1)*40)
  tk.Button(
    canvas,
    text='X',
    fg=DLT_BTN_FG,
    command=lambda:on_delete(index)
  ).place(x=290, y=(index+1)*40)
  
  create_labels(index + 1)


def on_enter(event):
  new_name = event.widget.get()
  if(new_name == ""):
    return
  nameList.append(new_name)
  index = len(nameList) - 1
  tk.Label(
    canvas,
    text=new_name,
    bg=CANVAS_BG,
    fg=CANVAS_FG,
    font=(CANVAS_FONT, CANVAS_FONT_SIZE)
  ).place(x=150, y=len(nameList)*40)
  tk.Button(
    canvas,
    text='X',
    fg=DLT_BTN_FG,
    command=lambda:on_delete(index)
  ).place(x=290, y=len(nameList)*40)
  
  event.widget.delete(0, "end")
  
  
  
labelframe = tk.LabelFrame(window, text="名前")
labelframe.grid(row = 0, column = 0, pady=10)
canvas = tk.Canvas(
  labelframe,
  bg = CANVAS_BG,
  height=WINDOW_HEIGHT-50,
)
canvas.pack(fill="both")

# text overflow bug
# add reset button
# scroll feature

input_container = tk.Frame(window)
input_container.grid(row = 0, column = 1, sticky="w")

tk.Label(input_container, text="名前入力：").grid(
  ipady=5,
  sticky="w"
)

Entry1 = tk.Entry(input_container)
Entry1.bind('<Return>', on_enter)
Entry1.focus()  
Entry1.grid() 

window.mainloop()