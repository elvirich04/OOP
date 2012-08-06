import tkinter


class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()

        self.points=0


        self.ask1button=tkinter.Button()
        self.ask1button["text"]="ask1"
        self.ask1button["command"]=self.ask1
        self.ask1button.pack()

        self.ask2button=tkinter.Button()
        self.ask2button["text"]="ask2"
        self.ask2button["command"]=self.ask2
        self.ask2button.pack()

        self.ask3button=tkinter.Button()
        self.ask3button["text"]="ask3"
        self.ask3button["command"]=self.ask3
        self.ask3button.pack()

        self.pointbutton=tkinter.Button()
        self.pointbutton["text"]="points"
        self.pointbutton["command"]=self.point
        self.pointbutton.pack()



    def ask1(self):
            response=tkinter.messagebox.askyesno("Question","Is the sun yellow?")
            if (response==True):
                self.points+=1

    def ask2(self):
            response=tkinter.messagebox.askyesno("Question","Is wood edible?")
            if (response==True):
                self.points+=1


    def ask3(self):
            response=tkinter.messagebox.askyesno("Question","Is fried chicken made of pigs?")
            if (response==True):
                self.points+=1

    def point(self):
            tkinter.messagebox.showinfo("Points","Your total points is: %i"%(self.points))
            
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()



