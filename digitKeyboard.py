from tkinter import *

def chageText(num):
    lab["text"] = lab["text"] + num

window= Tk()
window.title("Digital Keyboard")
window.geometry("300x400+200+100") 
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

lab=Label(window, text="0", justify=RIGHT, anchor=E, font=("Monaco", 26, "bold"), bg="#ccddee")
lab.grid(row=0, column=0, columnspan=3, sticky=EW)

btn7 = Button(window, text="7", font=("Monaco", 30, "bold"), command=lambda:chageText('7'))
btn7.grid(row=1, column=0, sticky=NSEW) 
btn8 = Button(window, text="8", font=("Monaco", 30, "bold"), command=lambda:chageText('8'))
btn8.grid(row=1, column=1, sticky=NSEW)
btn9 = Button(window, text="9", font=("Monaco", 30, "bold"), command=lambda:chageText('8'))
btn9.grid(row=1, column=2, sticky=NSEW)

btn4 = Button(window, text="4", font=("Monaco", 30, "bold"), command=lambda:chageText('4'))
btn4.grid(row=2, column=0, sticky=NSEW)
btn5 = Button(window, text="5", font=("Monaco", 30, "bold"), command=lambda:chageText('5'))
btn5.grid(row=2, column=1, sticky=NSEW)
btn6 = Button(window, text="6", font=("Monaco", 30, "bold"), command=lambda:chageText('6'))
btn6.grid(row=2, column=2, sticky=NSEW)

btn1 = Button(window, text="1", font=("Monaco", 30, "bold"), command=lambda:chageText('1'))
btn1.grid(row=3, column=0, sticky=NSEW)
btn2 = Button(window, text="2", font=("Monaco", 30, "bold"), command=lambda:chageText('2'))
btn2.grid(row=3, column=1, sticky=NSEW)
btn3 = Button(window, text="3", font=("Monaco", 30, "bold"), command=lambda:chageText('3'))
btn3.grid(row=3, column=2, sticky=NSEW)
window.mainloop()