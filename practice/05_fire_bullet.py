import pyxel

BULLET_SPEED = 3

class App:
    def __init__(self):
        # Initialize window size and title
        pyxel.init(160, 120, title="Shooting Game!")
        # Set initial player coordinates
        self.player_x = 80
        self.player_y = 60

        self.aim_x = 0
        self.aim_y = 0

        self.bullet_x = 0
        self.bullet_y = 0
        self.bullet_rad = 0
        # Load player image from resource file
        pyxel.load("assets/my_resource.pyxres")
        # Add a flag to check if the player is moving
        self.player_is_moving = False
        self.player_direction = 1
        # Start game update and draw
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Move player with WASD keys
        if pyxel.btn(pyxel.KEY_W):
            self.player_y = max(self.player_y - 2, 0)
        if pyxel.btn(pyxel.KEY_S):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)
        if pyxel.btn(pyxel.KEY_A):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_D):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bullet_x = self.player_x
            self.bullet_y = self.player_y
            self.bullet_rad = pyxel.atan2(self.aim_y - self.bullet_y, self.aim_x - self.bullet_x)

        # Update the flag in the update method
        self.player_is_moving = pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_D)

        self.aim_x = pyxel.mouse_x
        self.aim_y = pyxel.mouse_y

        # set player with mouse cursor position
        if self.player_x < self.aim_x:
            self.player_direction = 1
        else:
            self.player_direction = -1



        self.bullet_x += BULLET_SPEED * pyxel.cos(self.bullet_rad)
        self.bullet_y += BULLET_SPEED * pyxel.sin(self.bullet_rad)




    def draw(self):
        pyxel.cls(10)
        # Use the flag in the draw method to draw the player with an offset when moving
        if self.player_is_moving:
            pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16 * self.player_direction, 16, colkey=13) # set 13th color as transparent
        else:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16 * self.player_direction, 16, colkey=13) # set 13th color as transparent

        pyxel.blt(self.aim_x, self.aim_y, 0, 32, 0, 16, 16, colkey=13) # set 13th color as transparent

        pyxel.blt(self.bullet_x, self.bullet_y, 0, 48, 0, 16, 16, colkey=13) # set 13th color as transparent

App()
