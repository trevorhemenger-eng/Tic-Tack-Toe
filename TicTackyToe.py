rows = 3
colums = 3
board = []
O_input = ()
X_input = ()

def initialize_board():
    """This inisilisez print_board to br used"""
    return[1,2,3,4,5,6,7,8,9]

def print_board():
    print(f"""{board[0]}|{board[1]}|{board[2]}
-----
{board[3]}|{board[4]}|{board[5]}
-----
{board[6]}|{board[7]}|{board[8]}
""")

def Check_win_condision():
    """This checks if the board has gotten a win yet"""
    for i in range(0,rows * colums,3):
        if board[i] == board[i + 1] == board[i + 2]:
            #top row all matches
            winner = board[i]
            return winner #returns x or o if win is detected      
    for i in range(colums):
        if board[i] == board[i + 3] == board[i + 6]:
            #top row all matches
            winner = board[i]
            return winner #returns x or o if win is detected 
    if board[1] == board[5] == board[9]:
        winner = board[1]
        return winner
    if board[0] == board[4] == board[8]:
        print("tba")
    print("no win detected")
    return None    

def Correct_input(turn):
    """Checks if the input put in by the user is correct."""
    while True:
        userinput = input(f"{turn}'s turn. please input 1 - 9 on the board: ")
        if not userinput.isnumeric() or not 1 <= int(userinput) <= 9 :
            print()
            print("Invalid, please put a number on the board.")
            print()
        elif board[int(userinput)-1] in ["X", "O"] :
            print()
            print("space already taken")
            print()
        else:
            board[int(userinput)-1] = turn
            #userinput is 1 higher than the index in the list
            return int(userinput)
 
board = initialize_board()
while True:
    print_board()
    choice = Correct_input("X")
    if Check_win_condision() != None:
        print()
        print("X won")
        print()
        print_board()
        break
    print_board()
    choice1 = Correct_input("O")
    if Check_win_condision() != None:
            print()
            print("O won")
            print()
            print_board()
            break