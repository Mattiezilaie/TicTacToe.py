# Author: Mahtab Zilaie
# Date: November 23 2019
# Description:class named TicTacToe that has two private data members:
# the board and current state.nit method that initializes the board to a list of three
# lists that each contain three empty strings and initializes the current_state to "UNFINISHED".
# make_move that takes three parameters, a row and a column and player.
#values of current_state are: "X_WON", "O_WON", "DRAW", or "UNFINISHED".
# A game is drawn when all of the squares are filled, but neither player has won.
# and a method that prints out the board.
class TicTacToe:
    def __init__(self):
        self._board = [['','',''],['','',''],['','','']]
        self._current_state = "UNFINISHED"
        self._num = 0
    def make_move(self, row, col, player):
        if row >= 0 and row <= 2 and col >= 0 and col <= 2:
            if self._current_state == "UNFINISHED":
                if not self._board[row][col]:
                    self._board[row][col]= player
                    self._num = self._num + 1
                    if self._board[row][0]==player and self._board[row][1]==player and self._board[row][2]==player:
                        self._current_state = str(player) + "_Won"
                    elif self._board[0][col] == player and self._board[1][col] == player and self._board[2][col] == player:
                        self._current_state = str(player) + "_Won"
                    elif self._board[0][0] == player and self._board[1][1] == player and self._board[2][2] == player:
                        self._current_state = str(player) + "_Won"
                    elif self._board[0][2] == player and self._board[1][1] == player and self._board[2][0] == player:
                        self._current_state = str(player) + "_Won"
                    else:
                        if self._num == 9 and self._current_state == "UNFINISHED":
                            self._current_state = "DRAW"
                    return True;
                else:
                    return False;
            else:
                return False;
        else:
            return False;


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