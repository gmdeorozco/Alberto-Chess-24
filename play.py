from alberto_engine import Alberto_Engine
from board_printer import print_bits, print_board
from game_state import game_state
from initial_board import get_initial_board, get_board_1, get_board_2

from chess_game import move
from board_cells import cells
import time 

alberto = Alberto_Engine()

def move_alberto(state):
    print('Alberto is now thinking...')
    ini = time.time()
    origin, target, value  = alberto.select_move(state)
    n_state, captured = move(state=state,origin=origin, target=target)
    end = time.time()
    print('Alberto is done in', end-ini, 'seconds')
    print('Eval', value )
    print_board(n_state)
    move_person(n_state)

def move_person(state):
    print('It is your turn')
    try:
        person_move = input("Enter your move: ")
        if person_move == 'q':
            quit()
        origin, target = get_bits(person_move)
    except:
        print('Enter a correct move')
        move_person(state)
    n_state, captured = move(state=state,origin=origin, target=target)
    print_board(n_state)
    move_alberto(n_state)

def get_bits(command:str):
    com = command.split(' ')
    origin = cells[com[0].upper()]
    target = cells[com[1].upper()]
    return origin, target
  

    
desired_color = input("Enter the desired color (black or white): ").lower()
if desired_color == 'black':
    print("You chose black.")
elif desired_color == 'white' or desired_color == '':
    state = get_initial_board()
    print_board(state)
    
    print("You chose white. It is your turn")
    move_person(state)
else:
    print("Invalid input. Please enter either 'black' or 'white'.")
    