import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

file_name = tkinter.NONE

def new_file():
    global file_name
    file_name = "Untitled"
    text.delete('1.0', tkinter.END)
    
def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(file_name, 'w')
    out.write(data)
    out.close()
    
def save_as():
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title='Error', message="Saving file error")
        
def open_file():
    global file_name
    inp = askopenfile(mode="r")
    if inp is None:
        return 
    file_name = inp.name
    data = inp.read()
    text.delete("1.0", tkinter.END)
    text.insert("1.0", data)
    
def info():
    tkinter.messagebox.showinfo("Information", "Simple TextEditor\nby SunTeor")


root = tkinter.Tk()
root.title("Simple text editor")
#
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
#
text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = tkinter.Scrollbar(root, orient="vertical", command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
#
text.pack()
#
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)
#
menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Info", command=info)
menuBar.add_cascade(label="Exit", command=root.destroy)
root.configure(menu=menuBar)
root.mainloop()
