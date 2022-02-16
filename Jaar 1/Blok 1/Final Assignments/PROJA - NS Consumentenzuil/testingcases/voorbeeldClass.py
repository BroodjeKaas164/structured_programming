import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red")
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

class Application2(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.bye_there = tk.Button(self)
        self.bye_there["text"] = "Goodbye World\n(click me)"
        self.bye_there["command"] = self.say_hi
        self.bye_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red")
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("Bye, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

app = Application2(master=root)
app.mainloop()
