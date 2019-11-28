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
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_state = 'UNFINISHED'
    def get_current_state(self):
        return self.current_state
    def make_move(self, row, column, player):
        if(row<0 or row>2 or column<0 or column>2):
            return False
            if(self.board[row][column]!=''):
                return False
            if(self.current_state == 'X_WON' or self.current_state == 'O_WON' or self.current_state == 'DRAW'):
                return False
                self.board[row][column] = player
                self.update_current_state()
                return True
    def update_current_state(self):
        if(self.board[0][0]==self.board[0][1] and self.board[0][1]==self.board[0][2] and self.board[0][2]!=''):
            if(self.board[0][0]=='x'):
                self.current_state = 'X_WON'
            else:
                self.current_state = 'O_WON'
        elif(self.board[1][0]==self.board[1][1] and self.board[1][1]==self.board[1][2] and self.board[1][2]!=''):
            if(self.board[1][0]=='x'):
                self.current_state = 'X_WON'
            else:
                self.current_state = 'O_WON'
        elif(self.board[2][0]==self.board[2][1] and self.board[2][1]==self.board[2][2] and self.board[2][2]!=''):
            if(self.board[2][0]=='x'):
                self.current_state = 'X_WON'
            else:
                self.current_state = 'O_WON'
        elif(self.board[0][0]==self.board[1][0] and self.board[1][0]==self.board[2][0] and self.board[2][0]!=''):
            if(self.board[0][0]=='x'):
                self.current_state = 'X_WON'
            else:
                self.current_state = 'O_WON'

        elif(self.board[0][1]==self.board[1][1] and self.board[1][1]==self.board[2][1] and self.board[2][1]!=''):
             if(self.board[0][1]=='x'):
                 self.current_state = 'X_WON'
             else:
                 self.current_state = 'O_WON'
        elif(self.board[0][2]==self.board[1][2] and self.board[1][2]==self.board[2][2] and self.board[2][2]!=''):
             if(self.board[0][2]=='x'):
                 self.current_state = 'X_WON'
             else:
                 self.current_state = 'O_WON'
        elif(self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2] and self.board[2][2]!=''):
             if(self.board[0][0]=='x'):
                 self.current_state = 'X_WON'
             else:
                 self.current_state = 'O_WON'
        elif(self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0] and self.board[2][0]!=''):
             if(self.board[0][2]=='x'):
                 self.current_state = 'X_WON'
             else:
                 self.current_state = 'O_WON'
        else:
                flag = 0
                for i in range(3):
                 for j in range(3):
                     if(self.board[i][j]==''):
                         flag = 1
                         break
                 if(flag==0):
                     self.current_state = 'DRAW'
                 else:
                     self.current_state = 'UNFINISHED'
    def print_board(self):
         for i in range(3):
             for j in range(3):
                 if(self.board[i][j]==''):
                     print(' ', end = ' ')
                 else:
                     print(self.board[i][j], end = ' ')
             print("\n")
