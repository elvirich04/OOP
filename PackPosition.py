import tkinter
class Application(tkinter.Frame):
    def __init__ (self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()
    def CreateWidgets(self):
        self.image=tkinter.PhotoImage(file="mypixx.gif")
        self.label1=tkinter.Label(image=self.image)
        self.image2=tkinter.PhotoImage(file="batman_logo.gif")
        self.pack()
        self.button1=tkinter.Button(image=self.image2)
        self.button1["comman"]=self.batsignal
        self.button1.pack(side=tkinter.LEFT)
        self.label1.pack(side=tkinter.RIGHT)
#        self.label1.place(x=0, y=0)
#        self.button1.place(x=0, y=300)
    def batsignal(self):
        tkinter.messagebox.showinfo("BATMAN", "PARATING NA SI BATMAN!")
root=tkinter.Tk()
root.geometry("1024x768")
app=Application(master=root)
app.mainloop()
root.destroy()
