import pyxel

BULLET_SPEED = 5

class Player:
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.is_moving = False
        self.direction = direction

    def update(self):
        self.is_moving = False

        if pyxel.btn(pyxel.KEY_W):
            self.y = max(self.y - 2, 0)
            self.is_moving = True
        if pyxel.btn(pyxel.KEY_S):
            self.y = min(self.y + 2, pyxel.height - 16)
            self.is_moving = True
        if pyxel.btn(pyxel.KEY_A):
            self.x = max(self.x - 2, 0)
            self.is_moving = True
        if pyxel.btn(pyxel.KEY_D):
            self.x = min(self.x + 2, pyxel.width - 16)
            self.is_moving = True

    def draw(self):
        if self.is_moving:
            pyxel.blt(self.x, self.y, 0, 16, 0, 16 * self.direction, 16, colkey=13) # set 13th color as transparent
        else:
            pyxel.blt(self.x, self.y, 0, 0, 0, 16 * self.direction, 16, colkey=13) # set 13th color as transparent


class Bullet:
    def __init__(self, player_x, player_y, mouse_x, mouse_y, speed) -> None:
        self.x = player_x
        self.y = player_y
        self.rad = pyxel.atan2(mouse_y - player_y, mouse_x - player_x)
        self.speed = speed

    def update(self):
        self.x += self.speed * pyxel.cos(self.rad)
        self.y += self.speed * pyxel.sin(self.rad)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 48, 0, 16, 16, colkey=13) # set 13th color as transparent

class App:
    def __init__(self):
        # Initialize window size and title
        pyxel.init(160, 120, title="Shooting Game!")
        # Set initial player coordinates
        self.player = Player(80, 60, 1)

        self.aim_x = 0
        self.aim_y = 0

        pyxel.load("assets/my_resource.pyxres")

        self.bullet_list = []
        # Start game update and draw
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            bullet = Bullet(self.player.x, self.player.y, self.aim_x, self.aim_y, BULLET_SPEED)
            self.bullet_list.append(bullet)
        # Update the flag in the update method
        self.player_is_moving = pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_D)

        self.aim_x = pyxel.mouse_x
        self.aim_y = pyxel.mouse_y

        # set player with mouse cursor position
        if self.player.x < self.aim_x:
            self.player.direction = 1
        else:
            self.player.direction = -1

        self.player.update()

        for bullet in self.bullet_list:
            if bullet.x < 0 or bullet.x > pyxel.width or bullet.y < 0 or bullet.y > pyxel.height:
                self.bullet_list.remove(bullet)
            else:
                bullet.update()

    def draw(self):
        pyxel.cls(10)
        # Use the flag in the draw method to draw the player with an offset when moving
        self.player.draw()

        pyxel.blt(self.aim_x, self.aim_y, 0, 32, 0, 16, 16, colkey=13) # set 13th color as transparent

        for bullet in self.bullet_list:
            bullet.draw()

        # show count of bullets
        pyxel.text(10, 10, f"Bullets: {len(self.bullet_list)}", 7)
App()
