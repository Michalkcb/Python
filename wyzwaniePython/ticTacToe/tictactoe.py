board = ["_","_","_",
         "_","_","_",
         "_","_","_",]

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | "+ board[2] + " | " + " 1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | "+ board[5] + " | " + " 3 | 4 | 5")
    print(board[6] + " | " + board[7] + " | "+ board[8] + " | " + " 6 | 7 | 8")
    print("\n")

display_board()

def handle_turn(player):
    print(player + "twoja kolej")
    position = input("wybierz pozycję od 1 do 9: ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Błędna wartość. Wybierz pozycję w przedziale 1-9: ")

    position = int(position) - 1

    if board[position] != "_":
        print("To miejsce na planszy jest już zajęte")

    board[position] != player
    display_board()

def check_rows():
        row_1 = board[0] == board[1] == board[2] != "_"
        row_2 = board[3] == board[4] == board[5] != "_"
        row_3 = board[6] == board[7] == board[8] != "_"

        if row_1 or row_2 or row_3:
            return True
        else:
            return False
        
def check_cols():
        col_1 = board[0] == board[3] == board[6] != "_"
        col_2 = board[1] == board[4] == board[7] != "_"
        col_3 = board[2] == board[5] == board[8] != "_"

        if col_1 or col_2 or col_3:
            return True
        else:
            return False
        
def check_diag():
        diag_1 = board[0] == board[4] == board[8] != "_"
        diag_2 = board[6] == board[4] == board[2] != "_"

        if diag_1 or diag_2:
            return True
        else:
            return False
        
def flip_player(current_player):
    if current_player == "X":
          current_player = "O"
    else:
        current_player = "X"

    return current_player