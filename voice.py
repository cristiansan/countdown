import tkinter as tk
import speech_recognition as sr

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Cuenta regresiva")
        self.master.geometry("250x150")
        self.seconds = 30
        self.label = tk.Label(self.master, text="", font=("Arial", 30), fg="black")
        self.label.pack(pady=30)
        self.countdown()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def countdown(self):
        if self.seconds == 0:
            self.label.configure(text="¡TIEMPO AGOTADO!", fg="red")
        else:
            self.label.configure(text=str(self.seconds))
            self.seconds -= 1
            self.master.after(1000, self.countdown)

    def reset(self, phrase):
        if phrase.lower() == "reiniciar":
            self.seconds = 30
            self.label.configure(text="", fg="black")
            self.countdown()

    def recognize_speech(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            phrase = self.recognizer.recognize_google(audio, language="es-ES")
            self.reset(phrase)
        except sr.UnknownValueError:
            pass
        self.master.after(1000, self.recognize_speech)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    app.recognize_speech()
    root.mainloop()
