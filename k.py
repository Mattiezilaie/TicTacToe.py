








class TicTacToe:
    def __init__(self):
        self._board = [['','',''],['','',''],['','','']]
        self._current_state = "UNFINISHED"
        self._num = 0

    def horizontal_win(self, row, player):
        if row>2 or row<0:
            return False
        if self._board[row] != "":
            return False
        if self._current_state != "UNFINISHED":
            return False
        self._board[row] = player
        return True
        if self._board[row] == player:
            self._num = self._num + 1
            if self._board[row][0] == player and self._board[row][1] == player and self._board[row][2] == player:
                self._current_state = str(player) + "_Won"
                return True;

    def vertical_win(self, col, player):
        if row > 2 or row < 0 or col > 2 or col < 0:
            return False
        if self._board[row][col] != "":
            return False
        if self._current_state != "UNFINISHED":
            return False
        self._board[row][col] = player
        return True
        if self._board[row] == player:
            self._board[col] = player
            self._num = self._num + 1
            if self._board[0][col] == player and self._board[1][col] == player and self._board[2][col] == player:
                self._current_state = str(player) + "_Won"
                return True

    def diagonal_win(self, row, col, player):
        if row > 2 or row < 0 or col > 2 or col < 0:
            return False
        if self._board[row][col] != "":
            return False
        if self._current_state != "UNFINISHED":
            return False
        self._board[row][col] = player
        return True
        if self._board[row] == player:
            self._board[row][col] = player
            self._num = self._num + 1
            if self._board[0][0] == player and self._board[1][1] == player and self._board[2][2] == player:
                self._current_state = str(player) + "_Won"
            elif self._board[0][2] == player and self._board[1][1] == player and self._board[2][0] == player:
                self._current_state = str(player) + "_Won"
            return True


    def make_move(self, row, col, player):
                if row > 2 or row < 0 or col > 2 or col < 0:
                    return False
                if self._board[row][col] != "":
                    return False
                if self._current_state != "UNFINISHED":
                    return False
                self._board[row][col] = player
                return True
                count = 0
                while tic._current_state == "UNFINISHED":
                    if count % 2 == 0:
                        flag = tic.make_move(int(row), int(col), "X")
                    else:
                        flag = tic.make_move(int(row), int(col), "O")
                else:
                    count = count + 1
                if tic.get_current_state() == "DRAW":
                    print("Match is Draw")
                elif tic.get_current_state() == "X_WON":
                    print("Player X Won the Match")
                elif tic.get_current_state() == "O_WON":
                    print("Player O Won the Match")


    def get_current_state(self):
        return self._current_state


    def print_Table(self):
        print("\nPresent Status of TicTacToe board is : \n")
        l = "   0   1   2"
        count=0
        print(l)
        for i in self._board:
            print(str(count)+str(i))
            count=count+1
            print()
tic = TicTacToe()




tic.print_Table()
count = 0
while tic._current_state == "UNFINISHED":
    if count % 2 == 0:
        print("Player-x it's your turn")
        row = input("Enter Row In which You want to insert (0-2) : ")
        col = input("Enter Column In which You want to insert (0-2) : ")
        flag = tic.make_move(int(row), int(col), "X")
        if flag is False:
            tic.print_Table()
            while flag is False:
                print("Move is Not Successful")
                print("Player-x it's your turn")
                row = input("Enter Row In which You want to insert (0-2) : ")
                col = input("Enter Column In which You want to insert (0-2) : ")
                flag = tic.make_move(int(row), int(col), "X")
                tic.print_Table()
        else:
            print("Move is Successful")
            tic.print_Table()
    else:
        print("Player-O it's your turn")
        row = input("Enter Row In which You want to insert (0-2) : ")
        col = input("Enter Column In which You want to insert (0-2) : ")
        flag = tic.make_move(int(row), int(col), "O")
        if flag is False:
            tic.print_Table()
            while flag is False:
                print("Move is Not Successful")
                print("Player-O it's your turn")
                row = input("Enter Row In which You want to insert (0-2) : ")
                col = input("Enter Column In which You want to insert (0-2) : ")
                flag = tic.make_move(int(row), int(col), "X")
                tic.print_Table()

            else:
                print("Move is Successful")
        tic.print_Table()
    count = count + 1
if tic.get_current_state() == "DRAW":
    print("Match is Draw")
elif tic.get_current_state() == "X_Won":
    print("Player X Won the Match")
else:
    print("Player O Won the Match")