import tkinter as tk

class MyWin(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        e = tk.Label(self, text = "hi")
        e.pack()

        self.pack()

class MyWin2:

    def __init__(self):
        self.root = tk.Tk()

        e = tk.Label(self.root, text = "hi")
        e.pack()
        self.root.mainloop()



if __name__ == "__main__":
    MyWin2()
