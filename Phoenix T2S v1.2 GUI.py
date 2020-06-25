from tkinter import *
import win32com.client
e = win32com.client.Dispatch("SAPI.SpVoice")

def speak():
    cmdget=cmd.get()
    out.delete(0.0, END)
    text = cmdget
    out.insert(END, text)
def kill():
    e.Speak('uh. i died')
    main.quit()

main = Tk()

newline1 = Label(main, text='\n', bg='red')
newline2 = Label(main, text='\n', bg='red')
newline3 = Label(main, text='\n', bg='red')
newline1.grid(row=2, column=0)
newline2.grid(row=4, column=0)
newline3.grid(row=6, column=0)

main.resizable(0, 0)

main.title('Phoenix T2S v1.2 GUI')

main.config(bg='red')

updating = Label(main, text=' Phoenix T2S v1.2 GUI \nfeat Mr.Johnson\n', width=0 ,bg='red',  fg='white', font='consolas 18 bold')
updating.grid(row=0, column=0)

cmd = Entry(main, bg='white', width=50) 
cmd.grid(row=1, column=0)

butt = Button(main, text='Speak', command=speak, width=50, height=2)
butt.grid(row=3, column=0)

out = Text(main, width=75, height=3)
out.grid(row=5, column=0)

exitprog = Button(main, text='Kill Mr.J', command=kill, width=25)
exitprog.grid(row=7, column=0)


main.mainloop()
