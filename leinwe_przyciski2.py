# Leniwe przyciski 2
# Demonstacja użycia klasy w programie wykorzystującym Tkinter

from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI z tzrema przyciskami"""
    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utwórz trzy przyciski, które nic nie robia"""
        #pierwszy przycisk
        self.bttn1 = Button(self, text = "Nic nie robię!")
        self.bttn1.grid()

        #drugi przycisk
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Ja również")

        #trzeci przycisk
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "To samo mnie dotycczy!"

#czesc główna
root = Tk()
root.title("Leniwe przciski 2")
root.geometry("210x85")

root.mainloop()
