from bitarray import bitarray
from game_state import game_state
from piece import piece

def get_initial_board():

    white_pawns = bitarray(64)
    white_knights = bitarray(64)
    white_bishops = bitarray(64)
    white_rooks = bitarray(64)
    white_queens = bitarray(64)
    white_king = bitarray(64)
    black_pawns = bitarray(64)
    black_knights = bitarray(64)
    black_bishops = bitarray(64)
    black_rooks = bitarray(64)
    black_queens = bitarray(64)
    black_king = bitarray(64)
    
    white_pawns[8:16] = True
    white_knights[1] = True
    white_knights[6] = True
    white_bishops[2] = True
    white_bishops[5] = True
    white_rooks[0] = True
    white_rooks[7] = True
    white_queens[3] = True
    white_king[4] = True

    black_pawns[48:56] = True
    black_knights[57] = True
    black_knights[62] = True
    black_bishops[58] = True
    black_bishops[61] = True
    black_rooks[56] = True
    black_rooks[63] = True
    black_queens[59] = True
    black_king[60] = True

    white_pawn_pieces = piece(bits = white_pawns, type='pawn' )
    white_knights_pieces = piece(bits = white_knights, type='knight' )
    white_bishops_pieces = piece(bits = white_bishops, type='bishop' )
    white_rooks_pieces = piece(bits = white_rooks, type='rook' )
    white_queens_pieces = piece(bits = white_queens, type='queen' )
    white_king_pieces = piece(bits = white_king, type='king' )
    white_pieces = [
        white_pawn_pieces,
        white_knights_pieces,
        white_bishops_pieces,
        white_rooks_pieces,
        white_queens_pieces,
        white_king_pieces]
    
    black_pawn_pieces = piece(bits =  black_pawns, type='pawn',color=False )
    black_knights_pieces = piece(bits = black_knights, type='knight',color=False )
    black_bishops_pieces = piece(bits = black_bishops, type='bishop',color=False )
    black_rooks_pieces = piece(bits = black_rooks, type='rook',color=False )
    black_queens_pieces = piece(bits = black_queens, type='queen',color=False )
    black_king_pieces = piece(bits = black_king, type='king',color=False )
    black_pieces = [
        black_pawn_pieces,
        black_knights_pieces,
        black_bishops_pieces,
        black_rooks_pieces,
        black_queens_pieces,
        black_king_pieces]
    
    the_board = game_state(
        white_pieces=white_pieces, 
        black_pieces=black_pieces, 
        turn=True, 
        white_castling_kingside=True, 
        white_castling_queenside=True,
        black_castling_kingside = True,
        black_queenside_kingside = True,
        en_passant_target = bitarray(64),
        half_moves = 0,
        full_moves = 0,
        )

    return (the_board)

