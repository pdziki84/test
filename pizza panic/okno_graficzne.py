#nowe okno graficzne
#demonstracja okna graficzznego

##from livewires import games
##
##games.init(screen_width = 640, screen_height = 480, fps = 50)
##
##
##games.screen.mainloop()


###obraz tła
###ustawianie obrazu tła
##
##from livewires import games
##
##games.init(screen_width = 640, screen_height = 480, fps = 50)
##
##wall_image = games.load_image("sciana.jpg", transparent = False)
##games.screen.background = wall_image
##
##games.screen.mainloop()



###Duszek pizzy
###tworzenie duszka
##
##from livewires import games
##
##games.init(screen_width = 640, screen_height = 480, fps = 50)
##
##wall_image = games.load_image("sciana.jpg", transparent = False)
##games.screen.background = wall_image
##
##pizza_image = games.load_image("pizza.bmp")
##pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
##games.screen.add(pizza)
##
##games.screen.mainloop()



###wysoki wynik
###wyświetlanie telstu na ekranie gaficznym
##
##from livewires import games, color
##
##games.init(screen_width = 640, screen_height = 480, fps = 50)
##
##wall_image = games.load_image("sciana.jpg", transparent = False)
##games.screen.background = wall_image
##
##score = games.Text(value = 1756521,
##                   size = 60,
##                   color = color.black,
##                   x = 550,
##                   y = 30)
##
##
##games.screen.add(score)
##games.screen.mainloop()




###wygrałeś
###wyświetlanie komunikatu
##
##
##from livewires import games, color
##
##games.init(screen_width = 640, screen_height = 480, fps = 50)
##
##wall_image = games.load_image("sciana.jpg", transparent = False)
##games.screen.background = wall_image
##
##won_message = games.Message(value = "Wygrałeś!",
##                            size = 100,
##                            color = color.red,
##                            x = games.screen.width / 2,
##                            y = games.screen.height / 2,
##                            lifetime = 250,
##                            after_death = games.screen.quit)
##
##
##games.screen.add(won_message)
##
##games.screen.mainloop()



#Pizza w ruchu
#Określenie parametrów ruchu pizzy

from livewires import games


games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("sciana.jpg", transparent = False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")
the_pizza = games.Sprite(image = pizza_image,
                        x = games.screen.width / 2,
                        y = games.screen.height / 2,
                        dx = 1,
                        dy = 1)

games.screen.add(the_pizza)

games.screen.mainloop()
















































