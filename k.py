# Author:
# Date:
# Description:

class TicTacToe:
    def __init__(self):
        self._board

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