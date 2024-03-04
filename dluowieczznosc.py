# Długowieczność
# widgety Text i Entry oraz menager układu Grid

from tkinter import *

class Application(Frame):
    """Aplikacja z GUI, która może ujawnić sekret długowieczności."""
    def __init__(self, master):
        """Inicjalizacja ramki"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworzenie widgetów typu Button, Text, Entry."""
        #etykieta z instrukcją
        self.inst_lbl = Label(self, text = "Wprowadź hasło do sekretu długowiczości: ")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #etykieta do hasła
        self.pw_lbl = Label(self, text = "Hasło: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)

        #widget ENTRY do pzesyłąnia hasła
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        #utwórz przycisk 'Akceptuj'
        self.submit_bttn = Button(self, text = "Akceptuj", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        #utwórz widget TEXT do wyświetlania komunikatu
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        
    def reveal(self):
        """Wyświelr komunikat zalezy od popraawności hasła"""
        contents = self.pw_ent.get()

        if(contents == "sekret"):
            message = "Oto tajemny przepis na dożycie 100 lat: dożyj 99 lat, " \
                      "a potem bądź BARDZO ostrożny."
        else:
            message = "To nie jest poprawne hasło, więc nie mogę się z Tobą " \
                      "podzielić swoim sekretem."

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


#częśc główna
root = Tk()
root.title("Dłgowieczność")
root.geometry("300x150")

app = Application(root)
root.mainloop()
        
        
        
        

        
