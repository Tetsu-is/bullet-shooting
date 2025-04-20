import pyxel

class App:
    def __init__(self):
        # Initialize window size and title
        pyxel.init(160, 120, title="Shooting Game!")
        # Set initial player coordinates
        self.player_x = 80
        self.player_y = 60
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
            self.player_direction = -1
        if pyxel.btn(pyxel.KEY_D):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
            self.player_direction = 1
        # Update the flag in the update method
        self.player_is_moving = pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_D)

    def draw(self):
        pyxel.cls(10)
        # Use the flag in the draw method to draw the player with an offset when moving
        if self.player_is_moving:
            pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16 * self.player_direction, 16)
        else:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16 * self.player_direction, 16)

App()
