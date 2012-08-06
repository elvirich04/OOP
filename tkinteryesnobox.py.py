import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()

        self.morningbutton=tkinter.Button()
        self.morningbutton["text"]="morning"
        self.morningbutton["command"]=self.morning
        self.morningbutton.pack()
        
    
        self.afternoonbutton=tkinter.Button()
        self.afternoonbutton["text"]="afternoon"
        self.afternoonbutton["command"]=self.afternoon
        self.afternoonbutton.pack()

        self.eveningbutton=tkinter.Button()
        self.eveningbutton["text"]="evening"
        self.eveningbutton["command"]=self.evening
        self.eveningbutton.pack()

        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]="quit"
        self.quitbutton["command"]=self.exit
        self.quitbutton.pack()

    def morning(self):
            tkinter.messagebox.showinfo("greetings","good morning")

    def afternoon(self):
            tkinter.messagebox.showinfo("greetings","good afternoon!")

    def evening(self):
            tkinter.messagebox.showinfo("greetings","good night!")

    def exit(self):
            response=tkinter.messagebox.askyesno("bye! bye!","Do you want to quit?")

            if (response==True):
                self.quit()
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()


