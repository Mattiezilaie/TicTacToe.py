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
                        elif tic.get_current_state() == "X_Won":
                            print("Player X Won the Match")
                        else:
                            tic.get_current_state() == "O_Won"
                            print("Player O Won the Match")
                    return True;

                    return False;

                return False;

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

