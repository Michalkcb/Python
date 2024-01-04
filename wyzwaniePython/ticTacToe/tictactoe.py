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
    print(payer + "twoja kolej")
    position = input("wybierz pozycję od 1 do 9: ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Błędna wartość. Wybierz pozycję w przedziale 1-9: ")

    position = int(position) - 1

    if board[position] != "_":
        print("To miejsce na planszy jest już zajęte")

    board[position] != player
    display_board()
