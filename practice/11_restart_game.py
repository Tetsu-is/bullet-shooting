import pyxel

BULLET_SPEED = 5

IMAGE_OFFSET_PLAYER_DEFAULT_X = 0
IMAGE_OFFSET_PLAYER_DEFAULT_Y = 0
IMAGE_OFFSET_PLAYER_MOVING_X = 16
IMAGE_OFFSET_PLAYER_MOVING_Y = 0
IMAGE_OFFSET_AIM_X = 32
IMAGE_OFFSET_AIM_Y = 0
IMAGE_OFFSET_BULLET_X = 48
IMAGE_OFFSET_BULLET_Y = 0
IMAGE_OFFSET_ENEMY_X = 0
IMAGE_OFFSET_ENEMY_Y = 16

WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120

ENEMY_SPEED = 0.8
ENEMY_SIZE = 7
BULLET_SIZE = 5

COLLISION_DISTANCE = BULLET_SIZE / 2 + ENEMY_SIZE / 2


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
            pyxel.blt(
                self.x,
                self.y,
                0,
                IMAGE_OFFSET_PLAYER_MOVING_X,
                IMAGE_OFFSET_PLAYER_MOVING_Y,
                16 * self.direction,
                16,
                colkey=13,
            )  # set 13th color as transparent
        else:
            pyxel.blt(
                self.x,
                self.y,
                0,
                IMAGE_OFFSET_PLAYER_DEFAULT_X,
                IMAGE_OFFSET_PLAYER_DEFAULT_Y,
                16 * self.direction,
                16,
                colkey=13,
            )  # set 13th color as transparent


class Enemy:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.direction = pyxel.rndi(0, 1) * 2 - 1
        self.speed = ENEMY_SPEED
        self.rad = 0

    def update(self, player_x, player_y):
        self.x += self.speed * pyxel.cos(self.rad)
        self.y += self.speed * pyxel.sin(self.rad)

        diff_x = player_x - self.x
        diff_y = player_y - self.y
        self.rad = pyxel.atan2(diff_y, diff_x)

        if self.x < player_x:
            self.direction = -1
        else:
            self.direction = 1

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            0,
            IMAGE_OFFSET_ENEMY_X,
            IMAGE_OFFSET_ENEMY_Y,
            16 * self.direction,
            16,
            colkey=13,
        )


class Aim:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def update(self, mouse_x, mouse_y):
        self.x = mouse_x
        self.y = mouse_y

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            0,
            IMAGE_OFFSET_AIM_X,
            IMAGE_OFFSET_AIM_Y,
            16,
            16,
            colkey=13,
        )  # set 13th color as transparent


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
        pyxel.blt(
            self.x,
            self.y,
            0,
            IMAGE_OFFSET_BULLET_X,
            IMAGE_OFFSET_BULLET_Y,
            16,
            16,
            colkey=13,
        )  # set 13th color as transparent


class App:
    def __init__(self):
        # Initialize window size and title
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Shooting Game!")
        # Set initial player coordinates
        self.player = Player(80, 60, 1)

        self.kill_count = 0
        self.health = 2
        self.game_over = False

        self.enemy_list = []
        new_enemy = Enemy(100, 100)
        new_enemy2 = Enemy(50, 50)
        self.enemy_list.append(new_enemy)
        self.enemy_list.append(new_enemy2)

        self.aim = Aim(0, 0)

        pyxel.load("assets/my_resource.pyxres")

        self.bullet_list = []
        # Start game update and draw
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_over == True:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

            if pyxel.btnp(pyxel.KEY_R):
                self.game_over = False
                self.kill_count = 0
                self.health = 2
                self.enemy_list = []
                new_enemy = Enemy(100, 100)
                new_enemy2 = Enemy(50, 50)
                self.enemy_list.append(new_enemy)
                self.enemy_list.append(new_enemy2)

        if self.game_over == False:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                bullet = Bullet(
                    self.player.x, self.player.y, self.aim.x, self.aim.y, BULLET_SPEED
                )
                self.bullet_list.append(bullet)
            # Update the flag in the update method
            self.player_is_moving = (
                pyxel.btn(pyxel.KEY_W)
                or pyxel.btn(pyxel.KEY_A)
                or pyxel.btn(pyxel.KEY_S)
                or pyxel.btn(pyxel.KEY_D)
            )

            self.aim.update(pyxel.mouse_x, pyxel.mouse_y)

            # set player with mouse cursor position
            if self.player.x < self.aim.x:
                self.player.direction = 1
            else:
                self.player.direction = -1

            self.player.update()

            for bullet in self.bullet_list:
                if (
                    bullet.x < 0
                    or bullet.x > pyxel.width
                    or bullet.y < 0
                    or bullet.y > pyxel.height
                ):
                    self.bullet_list.remove(bullet)
                else:
                    bullet.update()

            for enemy in self.enemy_list:
                enemy.update(self.player.x, self.player.y)

            # Collision judgement
            # Check for collisions between bullets and enemies
            for bullet in self.bullet_list:
                for enemy in self.enemy_list:
                    bullet_center_x = bullet.x + BULLET_SIZE / 2
                    bullet_center_y = bullet.y + BULLET_SIZE / 2
                    enemy_center_x = enemy.x + ENEMY_SIZE / 2
                    enemy_center_y = enemy.y + ENEMY_SIZE / 2

                    if (
                        (enemy_center_x - bullet_center_x) ** 2
                        + (enemy_center_y - bullet_center_y) ** 2
                    ) ** 0.5 < COLLISION_DISTANCE:
                        self.bullet_list.remove(bullet)
                        self.enemy_list.remove(enemy)
                        self.kill_count += 1
                        break

            # Check for collisions between player and enemies
            for enemy in self.enemy_list:
                if (
                    (self.player.x - enemy.x) ** 2 + (self.player.y - enemy.y) ** 2
                ) ** 0.5 < COLLISION_DISTANCE:
                    self.health -= 1

            if self.health <= 0:
                self.game_over = True

    def draw(self):
        if self.game_over == True:
            pyxel.text(
                WINDOW_WIDTH // 2 - 20,
                WINDOW_HEIGHT // 2,
                "GAME OVER",
                pyxel.frame_count % 16,
            )
            pyxel.text(
                WINDOW_WIDTH // 2 - 20,
                WINDOW_HEIGHT // 2 + 20,
                "Press Q to quit",
                pyxel.frame_count % 16,
            )
            pyxel.text(
                WINDOW_WIDTH // 2 - 20,
                WINDOW_HEIGHT // 2 + 40,
                "Press R to restart",
                pyxel.frame_count % 16,
            )

        if self.game_over == False:
            pyxel.cls(10)
            # Use the flag in the draw method to draw the player with an offset when moving
            self.player.draw()

            for bullet in self.bullet_list:
                bullet.draw()

            for enemy in self.enemy_list:
                enemy.draw()

            self.aim.draw()

            # show count of bullets
            pyxel.text(10, 10, f"Kills: {self.kill_count}", 7)


App()
