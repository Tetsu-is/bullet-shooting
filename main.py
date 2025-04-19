import pyxel

class App:
    def __init__(self) -> None:
        pyxel.init(160, 120, title="Hello Pyxel")
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass

App()
