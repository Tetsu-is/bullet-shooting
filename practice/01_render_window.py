import pyxel

class App:
    def __init__(self):
        # ウィンドウのサイズとタイトルを設定
        pyxel.init(160, 120, title="Shooting Game!")
        # ゲームの更新と描画を開始
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(2)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)

App()