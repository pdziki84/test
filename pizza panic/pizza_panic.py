#Pizza panic
#graczz musi złapac lecące w dół pizze zanim spadną na ziemie

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)



class Pan(games.Sprite):
    """Patelnia sterowana przez gracza służąca do łapania spadających pizz."""
    image = games.load_image("patelnia.bmp")

    def __init__(self):
        """Initialize Pan object and create Text object for score."""
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)

        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """zmien pozycje na wyznaczona przez wspolzedne x myszy"""

        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        """Sprawdz czy nie zostały złapane jakieś pizze"""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()

    
class Pizza(games.Sprite):
    """Pizza, która spada na ziemie"""
    image = games.load_image("pizza.bmp")
    speed = 1

    def __init__(self, x, y = 90):
        """Inicialize Pizza object"""
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x,
                                    y = y,
                                    dy = Pizza.speed)

    def update(self):
        """Sprawdz czy dolny brze pizzty dosięgnął dłu ekranu"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """Destroy self if caught"""
        self.destroy()

    def end_game(self):
        """Zakończ grę"""
        end_message = games.Message(value = "koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width / 2,
                                    y = games.screen.height / 2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
                                  
    
class Chef(games.Sprite):
    """Szef kuchni, który porusza się w lewo i w prawo, zrzucając pizze."""
    image = games.load_image("kucharz.bmp")

    def __init__(self, y = 55, speed = 2, odds_change = 200):
        """Iniialize the Chef object"""
        super(Chef, self).__init__(image = Chef.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """ Ustal, czy kierunek ruchu musi zostać zmieniony na przeciwny. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = - self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = - self.dx

        self.check_drop()


    def check_drop(self):
        """Zmniejsz licznik odliczający czas lub zrzuc pizze i zresetuj odliczzanie"""
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            #ustaw margines na mniej więcej 30% wysokości pizzy, niezależnie od prędkości pizzy
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1



def main():
    """uruchom gre"""
    wall_image = games.load_image("sciana.jpg", transparent = False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()



main()


































    
