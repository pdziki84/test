#Licznik kliknięć
#Powiązanie zdarzenia z procedurą obsługi zdarzeń

from tkinter import *

class Application(Frame):
    """Aplikacja GUI która zlicza kliknięcia"""
    def __init__(self, master):
        """Inicjalizacja ramki"""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 #liczba kliknięc przycisku
        self.create_widget()

    def create_widget(self):
        """Utwórz przycisk, który wyświetla liczbę kliknięć"""
        self.bttn = Button(self)
        self.bttn["text"] = "Liczba kliknięć: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

        
    def update_count(self):
        """Zwiększ liczik kliknięc i wyświetl jego nową wartość"""
        self.bttn_clicks += 1
        self.bttn["text"] = "Liczba kliknięć: " + str(self.bttn_clicks)



#częśc główna

root = Tk()
root.title("licznik kliknięć")
root.geometry("250x100")

app = Application(root)
root.mainloop()
