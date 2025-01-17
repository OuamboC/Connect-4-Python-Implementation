#Main class
from GameLogic import GameLogic
class Connect4PythonImplementation:
    def __init__(self):
        #self.player1 = Player("Player 1", 'O')
       # self.player2 = Player("Player 2", 'C')
       # self.game = GameLogic([self.player1, self.player2])
         self.game = GameLogic()  #Initialise the game without passing players initially 

    def run(self):
        self.game.playGame()

if __name__ == "__main__":
    app = Connect4PythonImplementation()
    app.run()