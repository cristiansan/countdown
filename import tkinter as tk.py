import tkinter as tk

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Cuenta regresiva")
        self.master.geometry("250x150")
        self.seconds = 10
        self.label = tk.Label(self.master, text="", font=("Arial", 40), fg="black")
        self.label.pack(pady=30)
        self.countdown()

    def countdown(self):
        if self.seconds == 0:
            self.label.configure(text="¡TIEMPO AGOTADO!", fg="red")
        else:
            self.label.configure(text=str(self.seconds))
            self.seconds -= 1
            self.master.after(1000, self.countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
