from bitarray import bitarray
from game_state.game_state import GameState
from board_representation.piece import Piece

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

    white_pawn_pieces = Piece(bits = white_pawns, type='pawn' )
    white_knights_pieces = Piece(bits = white_knights, type='knight' )
    white_bishops_pieces = Piece(bits = white_bishops, type='bishop' )
    white_rooks_pieces = Piece(bits = white_rooks, type='rook' )
    white_queens_pieces = Piece(bits = white_queens, type='queen' )
    white_king_pieces = Piece(bits = white_king, type='king' )
    white_pieces = [
        white_pawn_pieces,
        white_knights_pieces,
        white_bishops_pieces,
        white_rooks_pieces,
        white_queens_pieces,
        white_king_pieces]
    
    black_pawn_pieces = Piece(bits =  black_pawns, type='pawn',color=False )
    black_knights_pieces = Piece(bits = black_knights, type='knight',color=False )
    black_bishops_pieces = Piece(bits = black_bishops, type='bishop',color=False )
    black_rooks_pieces = Piece(bits = black_rooks, type='rook',color=False )
    black_queens_pieces = Piece(bits = black_queens, type='queen',color=False )
    black_king_pieces = Piece(bits = black_king, type='king',color=False )
    black_pieces = [
        black_pawn_pieces,
        black_knights_pieces,
        black_bishops_pieces,
        black_rooks_pieces,
        black_queens_pieces,
        black_king_pieces]
    
    the_board = GameState(
        white_pieces=white_pieces, 
        black_pieces=black_pieces, 
        turn=True, 
        white_castling_kingside=True, 
        white_castling_queenside=True,
        black_castling_kingside = True,
        black_castling_queenside = True,
        en_passant_target = bitarray(64),
        half_moves = 0,
        full_moves = 0,
        )

    return (the_board)


def get_board_1():

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
    
    white_pawns[12] = True
    white_pawns[15] = True
    white_pawns[27] = True
    white_pawns[48] = True
    
    black_pawns[36] = True
    black_pawns[45] = True
    black_pawns[8] = True
    

    white_pawn_pieces = Piece(bits = white_pawns, type='pawn' )
    white_knights_pieces = Piece(bits = white_knights, type='knight' )
    white_bishops_pieces = Piece(bits = white_bishops, type='bishop' )
    white_rooks_pieces = Piece(bits = white_rooks, type='rook' )
    white_queens_pieces = Piece(bits = white_queens, type='queen' )
    white_king_pieces = Piece(bits = white_king, type='king' )
    white_pieces = [
        white_pawn_pieces,
        white_knights_pieces,
        white_bishops_pieces,
        white_rooks_pieces,
        white_queens_pieces,
        white_king_pieces]
    
    black_pawn_pieces = Piece(bits =  black_pawns, type='pawn',color=False )
    black_knights_pieces = Piece(bits = black_knights, type='knight',color=False )
    black_bishops_pieces = Piece(bits = black_bishops, type='bishop',color=False )
    black_rooks_pieces = Piece(bits = black_rooks, type='rook',color=False )
    black_queens_pieces = Piece(bits = black_queens, type='queen',color=False )
    black_king_pieces = Piece(bits = black_king, type='king',color=False )
    black_pieces = [
        black_pawn_pieces,
        black_knights_pieces,
        black_bishops_pieces,
        black_rooks_pieces,
        black_queens_pieces,
        black_king_pieces]
    
    the_board = GameState(
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

def get_board_2():
    the_board = get_board_1()
    the_board.white_pieces[3].bits[5]=True
    the_board.black_pieces[3].bits[60]=True
    return the_board
