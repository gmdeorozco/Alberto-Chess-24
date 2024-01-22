import numpy as np
import matplotlib.pyplot as plt

def create_chessboard():
    # Create an 8x8 chessboard using NumPy
    chessboard = np.zeros((8, 8), dtype=int)

    # Fill the chessboard with alternating light and dark colors
    chessboard[1::2, ::2] = 1  # Light squares
    chessboard[::2, 1::2] = 1  # Light squares

    return chessboard

def display_chessboard(chessboard):
    # Define colors for light and dark squares
    light_color = 'lightgray'
    dark_color = 'gray'

    # Create a custom colormap using ListedColormap
    colors = [dark_color, light_color]
    cmap = plt.cm.colors.ListedColormap(colors)

    # Display the chessboard using matplotlib
    plt.imshow(chessboard, cmap=cmap, origin='upper')
    plt.show()

# Create and display the chessboard
chessboard = create_chessboard()
display_chessboard(chessboard)

