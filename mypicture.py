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
        self.button1=tkinter.Button(image=self.image2)
        self.button1["comman"]=self.batsignal
        self.button1.pack()
        self.label1.pack()
    def batsignal(self):
        tkinter.messagebox.showinfo("BATMAN", "PARATING NA SI BATMAN!")
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
