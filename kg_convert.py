from tkinter import *
import tkinter.font as font
window = Tk()
window.geometry("900x500")
window.title("Kilogram converter")


title1 = Label(window,text="Kilo -> fahrenheit",font=font.Font(size=30),fg="grey")



weight = Label(window,text="Enter weight in Kg : ",font=font.Font(size=10))
weight.grid(row=1,column=0)

kg_weight = Entry(window,width=15,fg="Red")
kg_weight.grid(row=1,column=1)



g = Label(window,text="Grams : ",padx=30).grid(row=3,column=0)
p = Label(window,text="Pounds : ",padx=30).grid(row=3,column=2)
o = Label(window,text="Ounces : ",padx=30).grid(row=3,column=4)

t1 = Text(window,height=1,width=20).grid(row=3,column=1)
t2 = Text(window,height=1,width=20).grid(row=3,column=3)
t3 = Text(window,height=1,width=20).grid(row=3,column=5)


convert_button = Button(window,text="Convert",pady=10,padx=20,font=font.Font(size=10),width=3,height=1,fg="black",bg="grey")
convert_button.grid(row=1,column=2)







window.mainloop()