class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text="sample", width=25,
                                 )
        self.button1.pack()
        self.frame.pack()