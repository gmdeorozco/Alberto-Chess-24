from PIL import Image, ImageDraw
from bitarray import bitarray
import tkinter as tk
from tkinter import PhotoImage
from game_state.game_state import GameState
from board_representation.board_cells import get_row, get_col
from board_representation.initial_board import get_initial_board
from PIL import ImageTk

def create_chessboard():
    # Create a blank image for the chessboard
    chessboard_size = 400  # Adjust the size as needed
    chessboard_image = Image.new("RGB", (chessboard_size, chessboard_size), color="white")
    draw = ImageDraw.Draw(chessboard_image)

    # Draw the chessboard squares
    square_size = chessboard_size // 8
    for i in range(8):
        for j in range(8):
            square_color = "lightgray" if (i + j) % 2 == 0 else "gray"
            draw.rectangle([j * square_size, i * square_size, (j + 1) * square_size, (i + 1) * square_size], fill=square_color)

    return chessboard_image

def load_image(path):
    # Replace this path with the actual path to your pawn image
    pawn_image = Image.open(path).convert("RGBA")
    # Resize the pawn image to half its original size
    pawn_size = (pawn_image.width // 2, pawn_image.height // 2)
    pawn_image = pawn_image.resize(pawn_size)
    return pawn_image


def place_on_chessboard(chessboard_image, pawn_image, row, col):
    # Place the resized pawn image on the chessboard at the specified row and column
    piece_size = chessboard_image.width // 8
    chessboard_image.paste(pawn_image, (col * piece_size, row * piece_size), pawn_image)

def place_group( piece_group,img,chessboard_image ):    
    for index, bit in enumerate(piece_group):
        if bit == True:
            the_bit = bitarray(64)
            the_bit[index] = True
            
            ind_row, r = get_row(the_bit)
            ind_row = 8 - ind_row
            ind_col, c = get_col(the_bit)
            ind_col = ord(ind_col)-65
            place_on_chessboard(chessboard_image, img,ind_row,ind_col)

'''def state_to_img(state:game_state):
    chessboard_image = create_chessboard()
    
    white_pawns = state.white_pieces[0].bits
    white_pawn_img = load_image("img/white_pawn.png")
    place_group(white_pawns, white_pawn_img,chessboard_image)
    
    white_knights = state.white_pieces[1].bits
    white_knight_img = load_image("img/white_knight.png")
    place_group(white_knights, white_knight_img,chessboard_image)
    
    white_bishops = state.white_pieces[2].bits
    white_bishop_img = load_image("img/white_bishop.png")
    place_group(white_bishops, white_bishop_img,chessboard_image)
    
    white_rooks = state.white_pieces[3].bits
    white_rook_img = load_image("img/white_rook.png")
    place_group(white_rooks, white_rook_img,chessboard_image)
    
    white_queens = state.white_pieces[4].bits
    white_queen_img = load_image("img/white_queen.png")
    place_group(white_queens, white_queen_img,chessboard_image)
    
    white_kings = state.white_pieces[5].bits
    white_king_img = load_image("img/white_king.png")
    place_group(white_kings, white_king_img,chessboard_image)
    
    # BLACK
        
    black_pawns = state.black_pieces[0].bits
    black_pawn_img = load_image("img/black_pawn.png")
    place_group(black_pawns, black_pawn_img,chessboard_image)
    
    black_knights = state.black_pieces[1].bits
    black_knight_img = load_image("img/black_knight.png")
    place_group(black_knights, black_knight_img,chessboard_image)
    
    black_bishops = state.black_pieces[2].bits
    black_bishop_img = load_image("img/black_bishop.png")
    place_group(black_bishops, black_bishop_img,chessboard_image)
    
    black_rooks = state.black_pieces[3].bits
    black_rook_img = load_image("img/black_rook.png")
    place_group(black_rooks, black_rook_img,chessboard_image)
    
    black_queens = state.black_pieces[4].bits
    black_queen_img = load_image("img/black_queen.png")
    place_group(black_queens, black_queen_img,chessboard_image)
    
    black_kings = state.black_pieces[5].bits
    black_king_img = load_image("img/black_king.png")
    place_group(black_kings, black_king_img,chessboard_image)
    
    # Display the resulting chessboard with the pawn
    chessboard_image.show()
'''

def state_to_img(state: GameState, window):
    # Clear the previous content of the window
    for widget in window.winfo_children():
        widget.destroy()

    chessboard_image = create_chessboard()
    
    white_pawns = state.white_pieces[0].bits
    white_pawn_img = load_image("img/white_pawn.png")
    place_group(white_pawns, white_pawn_img, chessboard_image)
    
    white_knights = state.white_pieces[1].bits
    white_knight_img = load_image("img/white_knight.png")
    place_group(white_knights, white_knight_img,chessboard_image)
    
    white_bishops = state.white_pieces[2].bits
    white_bishop_img = load_image("img/white_bishop.png")
    place_group(white_bishops, white_bishop_img,chessboard_image)
    
    white_rooks = state.white_pieces[3].bits
    white_rook_img = load_image("img/white_rook.png")
    place_group(white_rooks, white_rook_img,chessboard_image)
    
    white_queens = state.white_pieces[4].bits
    white_queen_img = load_image("img/white_queen.png")
    place_group(white_queens, white_queen_img,chessboard_image)
    
    white_kings = state.white_pieces[5].bits
    white_king_img = load_image("img/white_king.png")
    place_group(white_kings, white_king_img,chessboard_image)
    
    # BLACK
        
    black_pawns = state.black_pieces[0].bits
    black_pawn_img = load_image("img/black_pawn.png")
    place_group(black_pawns, black_pawn_img,chessboard_image)
    
    black_knights = state.black_pieces[1].bits
    black_knight_img = load_image("img/black_knight.png")
    place_group(black_knights, black_knight_img,chessboard_image)
    
    black_bishops = state.black_pieces[2].bits
    black_bishop_img = load_image("img/black_bishop.png")
    place_group(black_bishops, black_bishop_img,chessboard_image)
    
    black_rooks = state.black_pieces[3].bits
    black_rook_img = load_image("img/black_rook.png")
    place_group(black_rooks, black_rook_img,chessboard_image)
    
    black_queens = state.black_pieces[4].bits
    black_queen_img = load_image("img/black_queen.png")
    place_group(black_queens, black_queen_img,chessboard_image)
    
    black_kings = state.black_pieces[5].bits
    black_king_img = load_image("img/black_king.png")
    place_group(black_kings, black_king_img,chessboard_image)
    # ... (Repeat the same process for other pieces)

    # Convert the PIL Image to a Tkinter PhotoImage
    tk_image = PhotoImage(master=window, width=chessboard_image.width, height=chessboard_image.height)
    tk_image = ImageTk.PhotoImage(chessboard_image)
    
    # Display the image in a Tkinter Label
    label = tk.Label(window, image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection
    
    # Place the label in the window
    label.pack()

# Example usage:
'''root = tk.Tk()
state = get_initial_board()  # Assuming you have a game_state instance
state_to_img(state, root)
root.mainloop()'''