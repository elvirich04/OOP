import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()

        self.morningbutton=tkinter.Button()
        self.morningbutton["text"]="Morning"
        self.morningbutton["command"]=self.morning
        self.morningbutton.pack()
        
    
        self.afternoonbutton=tkinter.Button()
        self.afternoonbutton["text"]="Afternoon"
        self.afternoonbutton["command"]=self.afternoon
        self.afternoonbutton.pack()

        self.eveningbutton=tkinter.Button()
        self.eveningbutton["text"]="Evening"
        self.eveningbutton["command"]=self.evening
        self.eveningbutton.pack()

        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]="Quit"
        self.quitbutton["command"]=self.quit
        self.quitbutton.pack()

    def morning(self):
            print("Good Morning!")

    def afternoon(self):
            print("Good Afternoon!")

    def evening(self):
            print("Hello World!")

    def quit(self):
            print("Good Bye!")
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()



