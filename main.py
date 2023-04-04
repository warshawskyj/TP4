import arcade
import random
from math import atan2, pi

NUM_SHAPES = 100
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

LEFT_BUTTON = 1
RIGHT_BUTTON = 4


class Cercle:
    def __init__(self, x, y):
        # la position est determinee par le clic, les autres parametres sont aleatoires
        self.centre_x = x
        self.centre_y = y
        self.change_x = random.randint(-5, 5)
        self.change_y = random.randint(-5, 5)
        self.color = random.choice(COLORS)

        self.rayon = random.randint(10, 30)

    def update(self):
        # deplacer le cercle selon sa vitesse
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        # assurer que le cercle reste dans l'ecran
        # la multiplication part -1 permet de changer la direction du mouvement
        if self.centre_x < self.rayon or self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.centre_y < self.rayon or self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class Rectangle:
    def __init__(self, x, y):
        # la position est determinee par le clic, les autres parametres sont aleatoires
        self.centre_x = x
        self.centre_y = y
        self.largeur = random.randint(10, 60)
        self.hauteur = random.randint(10, 60)
        self.change_x = random.randint(-50, 50)
        self.change_y = random.randint(-50, 50)
        self.angle = 0
        self.color = random.choice(COLORS)

    def update(self):
        # deplacer le rectangle selon sa vitesse
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        # assurer que le rectangle reste dans l'ecran
        if self.centre_x < self.largeur or self.centre_x > SCREEN_WIDTH - self.largeur:
            self.change_x *= -1
        if self.centre_y < self.hauteur or self.centre_y > SCREEN_HEIGHT - self.hauteur:
            self.change_y *= -1
        # tourner le rectangle dans la direction de son mouvement
        self.angle = atan2(self.change_y, self.change_x) + pi / 4

    def draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.largeur, self.hauteur, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")
        self.liste_formes = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(NUM_SHAPES):
            center_x = random.randint(30, SCREEN_WIDTH - 30)
            center_y = random.randint(30, SCREEN_HEIGHT - 30)
            self.liste_formes.append(Cercle(center_x, center_y))
        # remplir la liste avec 20 objets de type Rectangle
        for _ in range(NUM_SHAPES):
            center_x = random.randint(60, SCREEN_WIDTH - 60)
            center_y = random.randint(60, SCREEN_HEIGHT - 60)
            self.liste_formes.append(Rectangle(center_x, center_y))

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # ajouter un nouveau cercle ou rectangle a la liste
        if button == LEFT_BUTTON:
            self.liste_formes.append(Cercle(x, y))
        elif button == RIGHT_BUTTON:
            self.liste_formes.append(Rectangle(x, y))

    def on_draw(self):
        arcade.start_render()
        # dessiner tous les objets de la liste et les faire bouger
        for cercle in self.liste_formes:
            cercle.update()
            cercle.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
