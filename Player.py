class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def makeMove(self):
        move = input(f"{self.name}, enter your move as two numbers separated by a space (row col): ")
        row, col = move.split()  # Split the input string into two parts
        row = int(row)  # Convert the first part to an integer
        col = int(col)  # Convert the second part to an integer
        return row, col