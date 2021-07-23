from tkinter import *
from tkinter.font import Font
import time
def todo():
    root = Tk()
    root.title('MoonStone~ To-Do List')
    root.geometry("400x500")
    root.resizable(0, 0)
    root.config(bg='black')

    my_font = Font(
            family="Fira Sans Compressed",
            size=50,
            weight="normal")

    my_frame = Frame(root)
    my_frame.pack(pady=10)

    my_list = Listbox(my_frame,
            font=my_font,
            width=40,
            height=15,
            bg="black",
            bd=0,
            fg="white",
            highlightthickness=0,
            selectbackground="#a6a6a6",
            activestyle="none")

    my_list.pack(side=LEFT, fill=BOTH)

    # Create scrollbar
    my_scrollbar = Scrollbar(my_frame)
    my_scrollbar.pack(side=RIGHT, fill=BOTH)

    # Add scrollbar
    my_list.config(yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=my_list.yview)

    # create entry box to add items to the list
    my_entry = Entry(root, font=("Fira Sans Compressed ",15,'italic'),width=35)
    my_entry.pack(side=BOTTOM,pady=20)

    # Create a button frame
    button_frame = Frame(root)
    button_frame.pack(pady=20)

    # FUNCTIONS
    def delete_item(arghs):
            my_list.delete(ANCHOR)

    def add_item(arghs):
            my_list.insert(END, my_entry.get())
            my_entry.delete(0, END)

    def cross_off_item(arghs):
            # Cross off item
            my_list.itemconfig(
                    my_list.curselection(),
                    fg="red")
            my_list.selection_clear(0, END)

    def uncross_item(arghs):
            # Cross off item
            my_list.itemconfig(
                    my_list.curselection(),
                    fg="white")
            my_list.selection_clear(0, END)

    def delete_crossed(arghs):
            count = 0
            while count < my_list.size():
                    if my_list.itemcget(count, "fg") == "#dedede":
                            my_list.delete(my_list.index(count))

                    count += 1
    root.bind('<Return>',add_item)
    root.bind('<Double-Button>',delete_item)
    root.bind('<Button-3>',cross_off_item)
    root.bind('<Button-2>',uncross_item)
    root.bind('<Control-D>',delete_crossed)


    root.mainloop()
def task():
      
    class Table:
          
        def __init__(self,root):
              
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                      
                    self.e = Entry(root, fg='blue',
                                   font=('Arial',16,'bold'))
                      
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
    lst = [('Day','Time','Task'),
           ('','',''),
           ('','',''),
           ('','',''),
           ('','',''),
           ('','',''),
           ('','',''),
           ('','','')]
       
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
       
    # create root window
    root = Tk()
    root.title('MoonStone~ Routine Scheduler')
    root.resizable(0,0)
    t = Table(root)
    root.mainloop()
def pomo():
    import countdown

root = Tk()
root.title("")
root.geometry("400x500")
root.resizable(0, 0)
root.config(bg='black')

Label(root,text="MoonStone~",font=("Fira Sans Compressed",20,'italic'),bg='black',fg='white').pack(side=TOP,pady=10)
Label(root,text="To-Do | Schedule | Pomodoro",font=("Fira Sans Compressed",11),bg='black',fg='white').pack(side=TOP,pady=15)
Label(root,text="(C) Avranil Bhattacharyya",font=("Fira Sans Compressed",8),bg='black',fg='white').pack(side=BOTTOM,pady=5)
btn1 = Button(root,text="To-Do List",font=("Fira Sans Compressed",12),bg='black',fg='white',bd=0 ,width=30,command=todo)
btn1.place(rely=0.3,relx=0.175)

btn2 = Button(root,text="Schedule Task",font=("Fira Sans Compressed",12),bg='black',fg='white',bd=0 ,width=30,command=task)
btn2.place(rely=0.4,relx=0.175)

btn3 = Button(root,text="Pomodoro Clock",font=("Fira Sans Compressed",12),bg='black',fg='white',bd=0 ,width=30,command=pomo)
btn3.place(rely=0.5,relx=0.175)

btn4 = Button(root,text="Exit",font=("Fira Sans Compressed",12),bg='black',fg='white',bd=0 ,width=30,command=root.destroy)
btn4.place(rely=0.6,relx=0.175)


root.mainloop()

