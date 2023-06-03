'''
    my implementation of a text-based
    version of the classic game of tic-tac-toe
    or knaughts and crosses
'''

from sys import exit

def main():
    player = "X"
    turn = 1
    state = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    # Game Loop
    while True:
        # Check for winner
        draw_board(state)
        if turn >= 6:
            if winner_x(state):
                exit(f"winner: X")
            if winner_o(state):
                exit(f"winner: O")
            if turn == 10:
                exit(f"It's a tie")
        
        
        # get player choice
        try:
            choice = int(input("choose a square(1-9) "))
            if choice > 9 or choice < 1: raise ValueError
            if state[choice] == "X" or state[choice] == "O": raise ValueError
        except (TypeError, ValueError):
            print("Invalid choice please try again (1-9) ")
            continue
        else:
            # Update game state
            state[choice] = player
            if player == "X":
                player = "0"
            else: player = "X"
            turn += 1


def draw_board(state):
    print(f"\n{state[1]} | {state[2]} | {state[3]}\n\
---------\n\
{state[4]} | {state[5]} | {state[6]}\n\
---------\n\
{state[7]} | {state[8]} | {state[9]}\n")
    

def winner_x(state):
    wins = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 5, 9],[3, 5, 7]]
    # for each possible win combination
    for win in wins:
        if state[win[0]] == "X" and state[win[1]] == "X" and state[win[2]] == "X":
            return "X"
        else: continue

def winner_o(state):
    wins = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 5, 9],[3, 5, 7]]
    for win in wins:
        if state[win[0]] == "O" and state[win[1]] == "O" and state[win[2]] == "O":
            return "O"
        else: continue

if __name__ == "__main__":
    main()