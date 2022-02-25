
# デーリー 2.0

import tkinter as tk
  
window = tk.Tk()
window.title('ルーレット')
window.geometry('800x500')

nameList = ["山中","神","伊藤","立石"]

labelframe = tk.Frame(window)
labelframe.pack(expand=True, fill="both")

def create_labels():
  for widgets in labelframe.winfo_children():
    widgets.destroy()
    
  #nameListをループしながらlabelと削除ボトンを作る
  for i in range(len(nameList)):
    tk.Label(labelframe, font = ("fantasy",20) ,text=nameList[i]).place(x = 100,y = 200+len(nameList)*40)
    tk.Button(labelframe, text='X',command=lambda:on_delete(i)).place(x=150, y = 200+len(nameList)*40)
    
def on_enter(event):
  new_name = event.widget.get()
  if(new_name == ""):
    return
  nameList.append(new_name)
  print(nameList)
  create_labels()
  event.widget.delete(0, "end")
    
def on_delete(index):
  # print(nameList)
  #削除したい名前をリストから削除する
  del nameList[index]
  create_labels()
  
Entry1 = tk.Entry()
Entry1.bind('<Return>', on_enter)               
# Entry1.insert(tk.END, u'追加メンバー')
Entry1.focus()     
Entry1.pack()

window.mainloop()

# make the window scroll