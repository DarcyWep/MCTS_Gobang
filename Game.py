from Board import Board
from Players import Human, AI

from datetime import datetime


class Game:

    def __init__(self):
        self.board = Board()    # 初始棋盘(黑子先手)

    def graphic(self):
        """绘制棋盘"""
        width, height = self.board.size, self.board.size       # 棋盘大小

        print("   黑子(-1) 用 X 表示\t\t\t白子(1) 用 O 表示\n")

        for x in range(width):      # 打印行坐标
            print("{0:8}".format(x), end='')

        print('\r\n')
        for i in range(height):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                if self.board.board[i, j] == -1:
                    print('X'.center(8), end='')
                elif self.board.board[i, j] == 1:
                    print('O'.center(8), end='')
                else:
                    print('-'.center(8), end='')
            print('\r\n\r\n')

    def start_play(self):
        human, ai = Human(), AI()
        self.graphic()

        while True:

            self.board, move_pos = human.action(self.board)
            game_result = self.board.game_over(move_pos)

            self.graphic()
            if game_result == 'win' or game_result == 'tie':    # 游戏结束
                print('黑子落棋: {}, 黑子(-1)胜利！游戏结束！'.format(move_pos)) if game_result == 'win' \
                    else print('黑子落棋: {}, 平局！游戏结束！'.format(move_pos))
                break
            else:
                print('黑子落棋: {}, 未分胜负, 游戏继续！'.format(move_pos))

            # start_time = datetime.now()
            self.board, move_pos = ai.action(self.board, move_pos)
            # print(datetime.now() - start_time)
            game_result = self.board.game_over(move_pos)
            self.graphic()
            if game_result == 'win' or game_result == 'tie':    # 游戏结束
                print('白子落棋: {}, 白子(1)胜利！游戏结束！'.format(move_pos)) if game_result == 'win' \
                    else print('白子落棋: {}, 平局！游戏结束！'.format(move_pos))
                break
            else:
                print('白子落棋: {}, 未分胜负, 游戏继续！'.format(move_pos))


if __name__ == "__main__":
    game = Game()
    game.start_play()
