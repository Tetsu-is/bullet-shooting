import pyxel

class App:
    def __init__(self):
        # ウィンドウのサイズとタイトルを設定
        pyxel.init(160, 120, title="Shooting Game!")
        # プレイヤーの初期座標を設定する
        self.player_x = 80
        self.player_y = 60
        # リソースファイルからプレイヤーの画像を読み込む
        pyxel.load("assets/my_resource.pyxres")
        # ゲームの更新と描画を開始
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(10)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        # プレイヤーを描画する
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16)


App()