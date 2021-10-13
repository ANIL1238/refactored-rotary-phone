from tkinter import*
from tkinter import messagebox


anil=Tk()
anil.title("AKS-SOFT")
anil.geometry("500x500")
def red():
  #return messagebox.showinfo('hello','you clid on red button')
  anil.configure(background="red")
  anil.text="anil"
  print("sahoo")

def yellow():
   #return messagebox.showinfo('hello','you clid on yellow button')
   anil.configure(background="yellow")


def green():
   #return messagebox.showinfo('hello','you clid on grenn button')
   anil.configure(background="green")


def orange():
   #return messagebox.showinfo('hello','you clid on orange button')
   anil.configure(background="yellow")


button1=Button(anil,text="red",fg="red",font=('Arial',14),command=red)
button1.pack(side=TOP,pady=20)
button2=Button(anil,text="yellow",fg="yellow",font=('Arial',14),command=yellow)
button2.pack(side=RIGHT,)
button3=Button(anil,text="green",fg="green",font=('Arial',14),command=green)
button3.pack(side=LEFT)
button4=Button(anil,text="orange",fg="orange",font=('Arial',14),command=orange)
button4.pack(side=BOTTOM)
anil.mainloop()


