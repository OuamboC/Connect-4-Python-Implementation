# Class to manage the game board
class GameBoard:
    def __init__(self, rows, cols):
        # Initialize the board with specified rows and columns
        self.rows = rows
        self.cols = cols
        # Create a grid filled with empty spaces
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    def printGrid(self):
        # Print the current state of the grid
        for row in self.grid:
            print(" | ".join(row))  # Join row elements with separator ' | '
            print("-" * (self.cols * 4 - 1))  # Print row separator
    
    def isValidMove(self, row, col):
        # Check if the move is within bounds and the cell is empty
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == ' '
    
    def placeToken(self, row, col, token):
        # Place the token on the grid if the move is valid
        if self.isValidMove(row, col):
            self.grid[row][col] = token
    
    def getToken(self, row, col):
        # Get the token at the specified position on the grid
        return self.grid[row][col]