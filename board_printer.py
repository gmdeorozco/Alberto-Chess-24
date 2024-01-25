from game_state import GameState
from bitarray import bitarray
from piece import Piece

def print_board(board:GameState):
    board = str_board(board)

    print(board[56:64])
    print(board[48:56])
    print(board[40:48])
    print(board[32:40])
    print(board[24:32])
    print(board[16:24])
    print(board[8:16])
    print(board[0:8])

def str_board( board:GameState ):
    result_str = '................................................................'
    
    for piece in board.white_pieces:
        if piece is None: continue
        result_str = convert_str(piece, result_str=result_str)
    
    for piece in board.black_pieces:
        if piece is None: continue
        result_str = convert_str(piece, result_str=result_str)
    
    return result_str    


    return str_result

def convert_str(piece:Piece, result_str:str) -> str:
    
    for index, bit in enumerate(piece.bits):
        if bit==True:
            result_str = replace_char_at_position(result_str,index,get_char(piece))
    return result_str

def get_char( piece:Piece ) -> str:
    if piece.color:
        if piece.type == 'pawn':  return 'P'
        if piece.type == 'knight':  return 'N'
        if piece.type == 'bishop':  return 'B'
        if piece.type == 'rook' : return 'R'
        if piece.type == 'queen':  return 'Q'
        if piece.type == 'king':  return 'K'
    else:
        if piece.type == 'pawn' : return 'p'
        if piece.type == 'knight':  return 'n'
        if piece.type == 'bishop':  return 'b'
        if piece.type == 'rook' : return 'r'
        if piece.type == 'queen':  return 'q'
        if piece.type == 'king' : return 'k'
        
def replace_char_at_position(input_string, position, new_char):

    if 0 <= position < len(input_string):
        # Create a new string with the replaced character
        new_string = input_string[:position] + new_char + input_string[position + 1:]
        return new_string
    else:
        # If the position is out of bounds, return the original string
        return input_string


class ConsoleColors:
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    END = '\033[0m'

def print_alternating_colors(text,first,second):
    #text = text.replace('0','.')
    colored_text = ' '.join([f"{first}{c}" if i % 2 == 0 else f"{second}{c}" for i, c in enumerate(text)])
    print(f"{colored_text}{ConsoleColors.END}")

def print_bits(bits:bitarray,msg=''):
    print(msg)
    string = bits.to01()
    
    print_alternating_colors(string[56:64],ConsoleColors.WHITE,ConsoleColors.GRAY)
    print_alternating_colors(string[48:56],ConsoleColors.GRAY,ConsoleColors.WHITE)
    print_alternating_colors(string[40:48],ConsoleColors.WHITE,ConsoleColors.GRAY)
    print_alternating_colors(string[32:40],ConsoleColors.GRAY,ConsoleColors.WHITE)
    print_alternating_colors(string[24:32],ConsoleColors.WHITE,ConsoleColors.GRAY)
    print_alternating_colors(string[16:24],ConsoleColors.GRAY,ConsoleColors.WHITE)
    print_alternating_colors(string[8:16],ConsoleColors.WHITE,ConsoleColors.GRAY)
    print_alternating_colors(string[0:8],ConsoleColors.GRAY,ConsoleColors.WHITE)

