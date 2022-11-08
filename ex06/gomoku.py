import tkinter
import tkinter.messagebox

# キャンパスの縦横サイズ(px)
CANVAS_SIZE = 400


# 線の数
LINE_NUM = 10


#色の設定
BOARD_COLOR = "brown"
PLAYER1_COLOR = "black"
PLAYER2_COLOR = "white"

#プレーヤーの値
PLAYER1 = 1
PLAYER2 = 2

class Board():
    def __init__(self, master):
        self.master = master # 親ウィンジェット
        self.player = PLAYER1 
        self.board = None # 盤面上の管理する二次元リスト
        self.color = {
            PLAYER1 : PLAYER1_COLOR, PLAYER2 : PLAYER2_COLOR
        }
        self.nextDisk = None


        # ウィンジェットの作成
        self.createWidgets()


        # イベントの設定
        self.setEvents()


        # ゲームの初期化
        self.initBoard()



    def createWidgets(self): # ウィンジェットの作成
        self.canvas = tkinter.Canvas( # キャンパスの作成
            self.master, bg = BOARD_COLOR,
            width = CANVAS_SIZE, height = CANVAS_SIZE,
            highlightthickness = 0
        )
        self.canvas.pack(padx = 10, pady = 10)


    def setEvents(self): # イベントを設定する
        self.canvas.bind("<ButtonPress>", self.click)


    def initBoard(self): #ゲームの初期化を行う
        # 盤面上の管理する二次元リストを作成(初期値全てNone)
        self.board = [[None] * (LINE_NUM) for i in range(LINE_NUM)]
        # 線と線の間隔を計算(px)
        self.interval = CANVAS_SIZE // (LINE_NUM + 1)

        # 交点描画位置の左上オフセット
        self.offset_x = self.interval
        self.offset_y = self.interval

        # 縦線を描く
        for x in range(LINE_NUM):
            # 開始、終了の座標の計算
            xs = x * self.interval + self.offset_x
            ys = self.offset_y
            xe = xs
            ye = (LINE_NUM - 1) * self.interval + self.offset_y

            #線を描く
            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )

        # 横線を描く
        for y in range(LINE_NUM):
            # 開始、終了の座標の計算
            ys = y * self.interval + self.offset_y
            xs = self.offset_x
            ye = ys
            xe = (LINE_NUM - 1) * self.interval + self.offset_y

            #線を描く
            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )
    
    
    def drawDisk(self, x, y, color): # (x, y)に白か黒の円を描く
        # (x, y)の交点の中心座標を計算する
        center_x = x * self.interval + self.offset_x
        center_y = y * self.interval + self.offset_y

        # 中心座標から円の開始、終了座標を計算する
        xs = center_x - (self.interval * 0.8) // 2
        ys = center_y - (self.interval * 0.8) // 2
        xe = center_x + (self.interval * 0.8) // 2
        ye = center_y + (self.interval * 0.8) // 2

        # 円を描く
        tag_name = "disk_" + str(x) + "_" + str(y)
        self.canvas.create_oval(
            xs, ys,
            xe, ye,
            fill = color,
        )

        return tag_name

    
    def getIntersection(self, x ,y): # クリックした場所に駒が縦線と横線の交差点に置く
        ix = (x - self.offset_x + self.interval // 2) // self.interval
        iy = (y - self.offset_y + self.interval // 2) // self.interval

        return ix, iy

    
    def click(self, event): # クリックした時の処理
        # クリックした位置がどの交点であるかを計算
        x, y = self.getIntersection(event.x, event.y)

        if x < 0 or x >= LINE_NUM or y < 0 or y >= LINE_NUM:
            return

        if not self.board[y][x]: # 駒が置かれてない場合は駒を置く
            self.place(x, y, self.color[self.player])

    
    def place(self, x, y, color): # (x, y)の交点にcolorの駒を置く
        self.drawDisk(x, y, color)
        # 描いた円の色をリストに記憶させる
        self.board[y][x] = color

        # 5つ並んだかどうかをチェック
        if self.count(x, y, color) >= 5:
            self.showResult()
            return
        
        # プレイヤー交代
        if self.player == PLAYER1:
            self.player = PLAYER2
        else:
            self.player = PLAYER1

    
    def count(self, x, y, color): # (x, y)にcolorの駒を置いた時の駒の並び数をチェック
        # チェックする方向をリストに格納
        count_dir = [
            (1, 0), # 右
            (1, 1), # 右下
            (0, 1), # 上
            (-1, 1), # 左下
        ]

        max = 0 # 駒の並び数の最大値

        # count_dirの方向に対して駒の並び数をチェック
        for i, j in count_dir:
            # 石の並び数を1に初期化
            count_num = 1

            # (x, y)から現在の方向に対して1交点ずつ遠ざけながら石が連続しているかをチェック
            for s in range(1, LINE_NUM):
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= LINE_NUM or yj < 0 or yj < 0 or yj >= LINE_NUM:
                    # 盤面外の交点の場合は駒は連続していない
                    break

                if self.board[yj][xi] != color:
                    # 異なる色の駒が置かれていれば駒は連続していない
                    break

                # 上記以外の場合
                count_num += 1

            # 逆方向をチェック
            for s in range(-1, -(LINE_NUM), -1):
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= LINE_NUM or yj < 0 or yj < 0 or yj >= LINE_NUM:
                    # 盤面外の交点の場合は駒は連続していない
                    break

                if self.board[yj][xi] != color:
                    # 異なる色の駒が置かれていれば駒は連続していない
                    break

                # 上記以外の場合
                count_num += 1

            # 最大値を置き換え
            if max < count_num:
                max = count_num

        # 駒が連続している数の最大値を返却
        return max

    

    def showResult(self): # ゲーム終了時の結果を表示する
        #勝利者は先ほど駒を置いたプレイヤー
        winner = self.player

        # 結果をメッセージボックスで表示
        if winner == PLAYER1:
            tkinter.messagebox.showinfo("結果", "プレイヤー１の勝利した")
        else:
            tkinter.messagebox.showinfo("結果", "プレイヤー2 の勝利した")

app = tkinter.Tk()
app.title("五目並べ")
board = Board(app)
app.mainloop()






