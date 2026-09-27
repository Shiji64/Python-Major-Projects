board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
positions = {1 : (0,0) , 2: (0,1) , 3: (0,2) , 4: (1,0) , 5: (1,1) , 6: (1,2) , 7: (2,0) , 8: (2,1) , 9: (2,2) }
player1 = "X"
player2 = "O"

#display the board
def display_board():
    print("┌───┬───┬───┐")
    print(f"│ {board[0][0]} │ {board[0][1]} │ {board[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[1][0]} │ {board[1][1]} │ {board[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[2][0]} │ {board[2][1]} │ {board[2][2]} │")
    print("└───┴───┴───┘")

#check a player winner or not
def check_winner(player):
    #check rows
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    
    #check columns
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
         return True
    #check diagonals
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False

#check whether the game is a draw
def check_draw():
    for i in board:
        for j in i:
            if j == " ":
                return False
    return True

#Ask whether player want another round
def play_again():
    while True:
        ch = input("Do you want to play again? (Y/N)").lower()
        if ch == "y":
           return True
        elif ch == "n":
            return False
        else:
            print("Invalid option! Pls enter Y or N")


#Reset board
def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "



#main function
def main():
    while True:
        reset_board()
        current_player = player1
        while True:
            display_board()
            if current_player == player1:
                player_name = "Player 1"
            else:
                player_name = "Player 2"
            
            player_pos = input(f"{player_name} ({current_player}) , Pls enter a position 1-9 on board: ")
            #validating non-numeric input
            try:
                player_pos = int(player_pos)
            except ValueError:
                print("Pls enter digits only!!")
                continue
            #validating out of range input    
            if(player_pos<1 or player_pos>9):
                print("Pls enter valid position from 1-9 only.")
                continue
            row,col = positions[player_pos]
            #If already that cell is occupied
            if(board[row][col] == "X" or board[row][col] == "O"):
                print("This position already occupied!!")
                continue
            board[row][col] = current_player   
            #check winner
            if(check_winner(current_player)):
                display_board()
                print(f"{player_name} ({current_player}) has won the game!")
                break
            elif check_draw():
                display_board()
                print("This game is a draw!!")
                break

            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
        #Play again
        if play_again():
            continue
        else:
            print("Thank u for playing! See you again!")
            break
            

main()
