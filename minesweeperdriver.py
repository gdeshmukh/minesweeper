from minesweeper import Minesweeper


class MinesweeperDriver:

    def __init__(self):
        self._turns = 0
        self._playNextGame = False
        self._wins = 0
        self._losses = 0
        self._userHeight = int(input("Enter a height: "))
        self._userLength = int(input("Enter a length: "))
        self._userBombs = int(input("Enter number of bombs: "))
        self._userX = 0
        self._userY = 0

    def play(self):
        game = Minesweeper(self._userHeight, self._userLength, self._userBombs)
        game.print()
        self._userX = int(input("Select an x coordinate: "))
        self._userY = int(input("Select a y coordinate: "))
        game.selectFirst(self._userX - 1, self._userY - 1)
        game.print()
        while game.checkStatus() == "In progress":
            validInput = False
            while not validInput:
                action = input("select or flag or unflag: ").lower()
                if action == "select" or action == "flag" or action == "unflag":
                    validInput = True
                else:
                    print("Invalid choice, try again.")
            validInput = False
            while not validInput:
                self._userX = int(input("Select an x coordinate: "))
                self._userY = int(input("Select a y coordinate: "))
                if type(self._userX) == int and type(self._userY) == int:
                    if not game.checkValid(self._userX - 1, self._userY - 1):
                        validInput = True
                else:
                    print("Coordinate has already been selected")
            if action == "select":
                game.select(self._userX - 1, self._userY - 1)
            if action == "flag":
                game.flag(self._userX - 1, self._userY - 1)
            if action == "unflag":
                game.unflag(self._userX - 1, self._userY - 1)
            game.print()
        if game.checkStatus() == "Won":
            self._wins += 1
            print("You won!")
        if game.checkStatus() == "Lost":
            self._losses += 1
            print("You lost!")
        playAgain = input("Would you like to play again(Y or N)? ")
        if playAgain == "Y":
            self._playNextGame = True
            self.scoreCount()
            self._userHeight = int(input("Enter a height: "))
            self._userLength = int(input("Enter a length: "))
            self._userBombs = int(input("Enter number of bombs: "))
        if playAgain == "N":
            self._playNextGame = False
            print("Thank you for playing!")

    def scoreCount(self):
        print("Wins: " + str(self._wins) + " Losses: " + str(self._losses))

    def getPlayAgain(self):
        return self._playNextGame


def main():
    game = MinesweeperDriver()
    game.play()
    game.scoreCount()
    while game.getPlayAgain():
        game.play()

main()
