import argparse


class Board(object):
    def __init__(self, rows):
        self.rows = rows
        self.numbers = self.parse_rows(self.rows)
        self.selected = []

        self.bingo = len(self.rows)

        self.row = [0] * self.bingo
        self.col = [0] * self.bingo

    @staticmethod
    def parse_rows(rows):
        numbers = {}
        for row in range(len(rows)):
            for col in range(len(rows[0])):
                numbers[rows[row][col]] = {
                    "row": row,
                    "col": col
                }
        return numbers
    
    def add_number(self, number):
        """
        This is going to be the situation where
        a number is called
        """
        if number in self.numbers.keys():
            # r_num = self.numbers[number]['row']
            # c_num = self.numbers[number]['col']

            # self.row[r_num] += 1
            # self.col[c_num] += 1

            self.selected.append(number)

    def is_winner(self):
        """
        Call to see if the board state has won
        """
        if len(self.selected) < 5:            
            return False
        
        # since we do not worry about diagonals 
        # we just have to worry when one of the 
        # dimensions is filled
        bingo = len(self.rows)
        
        row = [0] * bingo
        col = [0] * bingo
        for num in self.selected:
            r_num = self.numbers[num]['row']
            c_num = self.numbers[num]['col']

            row[r_num] += 1
            col[c_num] += 1

            if row[r_num] == bingo or col[c_num] == bingo:
                return True
        
        return False

    def get_unselected(self):
        unselected = set(self.selected).symmetric_difference(list(self.numbers.keys()))

        return unselected

def parse_data(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # parse random numbers
    rand_nums = [int(x) for x in lines[0].split(',')]

    # parse board
    boards = []
    board = []
    for line in lines[1:]:
        if line == "\n":
            if board:
                boards.append(Board(board))
            board = []
        else:
            row = []
            for col in line.split(' '):
                if col:
                    row.append(int(col))
            board.append(row)
    boards.append(Board(board))

    return rand_nums, boards


def find_winner(nums, boards):
    for num in nums:
        for board in boards:
            board.add_number(num)
            if board.is_winner():
                print(num * sum(board.get_unselected()))
                return board


if __name__ == "__main__":
    ap = argparse.ArgumentParser('day 04')
    ap.add_argument('input_file', help='file path to input')

    args = ap.parse_args()

    nums, boards = parse_data(args.input_file)

    board = find_winner(nums, boards)
