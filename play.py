import tkinter as tk
from PIL import ImageTk
from bitarray import bitarray
from alberto_engine.alberto_engine import Alberto_Engine
from board_representation.board_printer import print_bits, print_board
from game_state.fen_to_state import fen_to_state
from game_state.game_state import GameState
from board_representation.initial_board import get_initial_board, get_board_1, get_board_2
from board_representation.chessboard import state_to_img
from move_solver.perform_move import move
from board_representation.board_cells import cells, get_diag
import time
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop

from move_solver.precalculated_moves.bishop_pre import get_bishop_precalculated 

alberto = Alberto_Engine()

root = tk.Tk()   
# Create a label


def move_alberto(state):
    print('Alberto is now thinking...')
    ini = time.time()
    origin, target, value  = alberto.select_move(state)
    n_state, captured = move(state=state,origin=origin, target=target)
    end = time.time()
    print('Alberto is done in', round(end-ini,3), 'seconds')
    print('Eval', value )
    print_board(n_state)
    
    state_to_img(state, root)
    
    
    root.update()  # Update the Tkinter window
    entry = tk.Entry(root)
    entry.pack()

    # Create a button
    button = tk.Button(root, text="Make Move",  command=lambda s=state: move_person(entry.get(), s))
    button.pack()


def move_person(com, state):
    print('It is your turn')
   
    person_move = com
    if person_move == 'q':
        quit()
    origin, target = get_bits(person_move)

    n_state, captured = move(state=state,origin=origin, target=target)
    print_board(n_state)
    
    state_to_img(state, root)
    root.update()
    
    move_alberto(n_state)

def get_bits(command:str):
    if len(command) == 4:
        origin = cells[command[:2].upper()]
        target = cells[command[2:4].upper()]
        return origin, target
    com = command.split(' ')
    origin = cells[com[0].upper()]
    target = cells[com[1].upper()]
    return origin, target
  
########### START ################


fen_position = input('Enter FEN or leave black for default: ')
state = get_initial_board() if len(fen_position) == 0 else fen_to_state(fen_position)

desired_color = input("Enter the desired color (black or white): ").lower()

if desired_color == 'black':
    print("You chose black.")
    alberto.color = True
    move_alberto(state)
    
elif desired_color == 'white' or desired_color == '':
    alberto.color = False
    print_board(state)
    
    print("You chose white. It is your turn")
    
    state_to_img(state, root)
    
    entry = tk.Entry(root)
    entry.pack()

    # Create a button
    button = tk.Button(root, text="Make Move",  command=lambda s=state: move_person(entry.get(), s))
    button.pack()
    root.update()  # Update the Tkinter window
    root.mainloop()

else:
    print("Invalid input. Please enter either 'black' or 'white'.")


