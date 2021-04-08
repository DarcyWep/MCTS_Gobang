import numpy as np

num_in_a_row_will_win = 4     # 几子棋


class Board:
    """棋盘类"""

    def __init__(self, board=None, size=6, next_player=-1):
        self.size = size    # 棋盘大小 size * size
        self.board = np.zeros((self.size, self.size), int) if board is None else board     # 棋盘初始状态

        self.next_player = next_player   # 当前下棋玩家（-1：黑子，1：白子）

    def get_legal_pos(self):
        """获取当前棋盘可落子处"""
        indices = np.where(self.board == 0)  # 返回棋盘中未落子处的下标（一个二维数组，第一个对应行坐标，第二个对应列坐标）
        # zip：将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
        return list(zip(indices[0], indices[1]))

    def is_move_legal(self, move_pos):

        x, y = move_pos[0], move_pos[1]
        if x < 0 or x > self.size or y < 0 or y > self.size:    # 检查落子坐标
            return False
        if self.board[x, y] != 0:   # 该位置是否还能落子
            return False

        return True

    def move(self, move_pos):
        if not self.is_move_legal(move_pos):    # 落子位置不合理
            raise ValueError("move {0} on board {1} is not legal". format(move_pos, self.board))
        # 新棋盘，准备赋予新结点使用(-self.next_player: 更新下棋选手)
        new_board = Board(board=np.copy(self.board), next_player=-self.next_player)
        new_board.board[move_pos[0], move_pos[1]] = self.next_player     # 落子

        return new_board      # 返回新棋盘

    def game_over(self, move_pos):
        """
        判断游戏是否结束
        :param move_pos: 落子下标
        :param player: 落子方
        :return:
        """
        if self.board_result(move_pos):     # player玩家胜利，游戏结束
            return 'win'
        elif len(self.get_legal_pos()) == 0:        # 未分胜利且无可落子点位，返回平局
            return 'tie'
        else:       # 游戏未结束
            return None

    def board_result(self, move_pos):
        """
        每次落子都需要判断棋盘状态，确定棋局是继续还是结束
        :param move_pos: 落子下标
        :return:
        """
        x, y = move_pos[0], move_pos[1]
        player = self.board[x, y]   # 落子方
        direction = list([[self.board[i][y] for i in range(self.size)]])  # 纵向是否有五颗连子
        direction.append([self.board[x][j] for j in range(self.size)])  # 横向是否有五颗连子
        direction.append(self.board.diagonal(y - x))  # 该点正对角是否有五颗连子
        direction.append(np.fliplr(self.board).diagonal(self.size - 1 - y - x))  # 该点反对角是否有五颗连子
        for v_list in direction:
            count = 0
            for v in v_list:
                if v == player:
                    count += 1
                    if count == num_in_a_row_will_win:
                        return True     # 该玩家赢下游戏
                else:
                    count = 0
        return False

    def __str__(self):
        return "next_player: {}\nboard:\n{}\n".format(self.next_player, self.board)


if __name__ == '__main__':
    import random
    print(random.randint(0, 0))
    pass

