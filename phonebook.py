from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("PHONEBOOK")
root.configure(bg="red")
a=Entry(width="20",bg="white",fg="blue",font=("bold",30))
l1=Label(width="20",text="Enter name",font=("bold",30))
b1=Button(text="Find",width="20",bg="black",fg="blue",font=("bold",30))
l2=Label(width="20",text="Enter phone no",font=("bold",30))
b=Entry(width="20",bg="white",fg="blue",font=("bold",30))
b2=Button(text="Save",width="20",bg="black",fg="blue",font=("bold",30))
b3=Button(text="Delete",width="20",bg="black",fg="blue",font=("bold",30))
b4=Button(text="Update",width="20",bg="black",fg="blue",font=("bold",30))
l1.place(x=5,y=30)
a.place(x=5,y=100)
b1.place(x=400,y=100)
l2.place(x=5,y=180)
b.place(x=5,y=240)
b2.place(x=5,y=340)
b3.place(x=400,y=340)
b4.place(x=100,y=420)
root.mainloop()

