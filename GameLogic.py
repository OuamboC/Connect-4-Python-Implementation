from GameBoard import GameBoard
from Player import Player


class GameLogic:
    def __init__(self):
        # Initialize the game with players and a game board
        self.players = []
        self.board = GameBoard(5, 5)  # Create a 5x5 game board
        self.current_player_index = 0  # Start with the first player

    def switchPlayer(self):
        # Switch to the next player
        self.current_player_index = 1 - self.current_player_index

    def checkWinner(self, row, col):
        # Check if the current player has won
        token = self.players[self.current_player_index].token

        # Check for a win in horizontal and vertical lines
        if self.checkLine(row, 0, 0, 1, token) or self.checkLine(0, col, 1, 0, token):
            return True

        return False

    def checkLine(self, start_row, start_col, step_row, step_col, token):
        # Check if there are 4 consecutive tokens in a line
        count = 0
        for i in range(5):
            row = start_row + i * step_row
            col = start_col + i * step_col
            if (
                0 <= row < 5
                and 0 <= col < 5
                and self.board.getToken(row, col) == token
            ):
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    def playGame(self):
        # Main game loop
        print("Welcome to Connect 4 (5x5 grid)")
        print(
            "Instructions: The first player to align four of their tokens vertically or horizontally wins the game!"
        )

        #Ask for player names 
        player1_name = self.isValidPlayerName("Enter Player1's name: ")
        player2_name = self.isValidPlayerName("Enter Player2's name: ")

        #Initialise players with their names and tokens
        self.players.append(Player(player1_name, '0'))
        self.players.append(Player(player2_name, 'C'))


        while True:
            
            self.board.printGrid()  # Print the game board
            row, col = self.players[self.current_player_index].makeMove() # Get the player's move

            if self.board.isValidMove(row, col):
                self.board.placeToken(
                    row, col, self.players[self.current_player_index].token
                )  # Place the token

                if self.checkWinner(row, col):  # Check for a winner
                    self.board.printGrid()  # Print the final state of the board
                    print(
                        f"{self.players[self.current_player_index].name} wins!!!!!!"
                    )
                    break  # End the game loop

                self.switchPlayer()  # Switch to the next player
            else:
                print(
                    "Invalid move. Try again."
                )  # Inform the player of an invalid move
    
    def isValidPlayerName(self, player_label):
        while True:
            #Strip any leading/trailing whitespace
            name = input(f"{player_label}").strip() 
            #Check that the name is not empty and doesnot contain numbers /speccial characters
            if name and name.isalpha():
                return name
            else:
                print("Invalid name.Please enter a valid name with only letters (no numbers or special characters).")