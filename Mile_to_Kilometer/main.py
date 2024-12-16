from ttkbootstrap import *


def showoutput():
    a = int(txt.get()) * 1.60934
    showL.config(text=f'{round(a,2)} km')


window = Window(themename='pulse')
window.title('Miles to Kilometers')
window.geometry('300x200')
window.resizable(False,False)

titleLabel = Label(window,text='Miles to Kilometers',font='Calibri 25 bold')
titleLabel.pack()

fullLbl = Label(window)
fullLbl.pack(pady=16)
txt = Entry(fullLbl)
txt.pack(side=LEFT)
inLineL = Button(fullLbl, text='Convert',command=showoutput)
inLineL.pack(side=LEFT)

showL =Label(window, text='', font='Calibri 20')
showL.place(x=100,y=100)

window.mainloop()

