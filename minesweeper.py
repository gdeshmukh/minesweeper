import random


class Minesweeper:
    def __init__(self, x, y, bombs):
        self._x = x
        self._y = y
        self._bombs = bombs
        self._status = "In progress"
        self._board = [[0] * self._y for a in range(self._x)]
        self._selected = [[False] * self._y for a in range(self._x)]
        self._flagged = [[False] * self._y for a in range(self._x)]
        for x in range(self._bombs):
            bombX = random.randint(0, (self._x - 1))
            bombY = random.randint(0, (self._y - 1))
            if self._board[bombX][bombY] != 'B':
                self._board[bombX][bombY] = 'B'
            else:
                x = x - 1
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if(self._board[i][j] == 'B'):
                    pass
                else:
                    bombCounter = 0
                    if(i == 0 and j == 0):
                        if self._board[i + 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j + 1] == 'B':
                            bombCounter += 1
                    elif(i == 0 and (j != 0 and j != len(self._board[i]) - 1)):
                        if self._board[i + 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j + 1] == 'B':
                            bombCounter += 1
                    elif(i == 0 and j == len(self._board[i]) - 1):
                        if self._board[i + 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j - 1] == 'B':
                            bombCounter += 1
                    elif(j == 0 and (i != 0 and i != len(self._board) - 1)):
                        if self._board[i - 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j + 1] == 'B':
                            bombCounter += 1
                    elif(j == 0 and i == len(self._board) - 1):
                        if self._board[i - 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j + 1] == 'B':
                            bombCounter += 1
                    elif(i == len(self._board) - 1 and j == len(self._board[i]) - 1):
                        if self._board[i - 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j - 1] == 'B':
                            bombCounter += 1
                    elif(i == len(self._board) - 1 and (j != 0 and j != len(self._board[i]) - 1)):
                        if self._board[i - 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j + 1] == 'B':
                            bombCounter += 1
                    elif(j == len(self._board[i]) - 1 and (i != 0 and i != len(self._board) - 1)):
                        if self._board[i - 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j - 1] == 'B':
                            bombCounter += 1
                    else:
                        if self._board[i - 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i - 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i + 1][j + 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j - 1] == 'B':
                            bombCounter += 1
                        if self._board[i][j + 1] == 'B':
                            bombCounter += 1
                    self._board[i][j] = bombCounter        
                
    def print(self):
        print(end='   ')
        for a in range(len(self._board)):
            print(a + 1, end=' ')
        print()
        for i in range(len(self._board)):
            if(i < 9):
                print(i + 1, end='  ')
            else:
                print(i + 1, end=' ')
            for j in range(len(self._board[i])):
                if self._selected[i][j]:
                    print(self._board[i][j], end=' ')
                elif self._flagged[i][j]:
                    print("F", end=' ')
                elif not self._selected[i][j]:
                    print("-", end=' ')
            print()

    def checkValid(self, x, y):
        try:
            return self._selected[x][y]
        except Exception as exceptObj:
            print("Coordinate doesn't exist")

    def select(self, i, j):
        try:
            if self.checkValid(i,j) == None:
                raise Exception
            if self._board[i][j] == 'B':
                self._status = "Lost"
                self._selected[i][j] = True
            if self._board[i][j] != 0 and self._board[i][j] != 'B':
                self._selected[i][j] = True
            if self._board[i][j] == 0 and not self._selected[i][j]:
                self._selected[i][j] = True
                if -1 < i < len(self._board) and -1 < j < len(self._board[i]):
                    try:
                        if i > 0:
                            if self._board[i - 1][j] == 0 and not self._selected[i-1][j]:
                                self.select(i-1,j)
                            if self._board[i - 1][j] != 0 and self._board[i - 1][j] != 'B' and not self._selected[i-1][j]:
                                self._selected[i-1][j] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if i > 0 and j > 0:
                            if self._board[i - 1][j - 1] == 0 and not self._selected[i-1][j - 1]:
                                self.select(i-1,j-1)
                            if self._board[i - 1][j - 1] != 0 and self._board[i - 1][j - 1] != 'B' and not self._selected[i-1][j - 1]:
                                self._selected[i-1][j - 1] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if i > 0 and j < len(self._board[i]) - 1:
                            if self._board[i - 1][j + 1] == 0 and not self._selected[i-1][j + 1]:
                                self.select(i-1,j+1)
                            if self._board[i - 1][j + 1] != 0 and self._board[i - 1][j + 1] != 'B' and not self._selected[i-1][j + 1]:
                                self._selected[i-1][j + 1] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if i < len(self._board) - 1:
                            if self._board[i + 1][j] == 0 and not self._selected[i+1][j]:
                                self.select(i+1,j)
                            if self._board[i + 1][j] != 0 and self._board[i + 1][j] != 'B' and not self._selected[i+1][j]:
                                self._selected[i+1][j] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if i < len(self._board) - 1 and j > 0:
                            if self._board[i + 1][j - 1] == 0 and not self._selected[i+1][j - 1]:
                                self.select(i+1,j-1)
                            if self._board[i + 1][j - 1] != 0 and self._board[i + 1][j - 1] != 'B' and not self._selected[i+1][j - 1]:
                                self._selected[i+1][j - 1] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if i < len(self._board) - 1 and j < len(self._board[i]):
                            if self._board[i + 1][j + 1] == 0 and not self._selected[i+1][j+1]:
                                self.select(i+1,j+1)
                            if self._board[i + 1][j + 1] != 0 and self._board[i + 1][j + 1] != 'B' and not self._selected[i+1][j+1]:
                                self._selected[i+1][j + 1] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if j > 0:
                            if self._board[i][j - 1] == 0 and not self._selected[i][j - 1]:
                                self.select(i,j-1)
                            if self._board[i][j - 1] != 0 and self._board[i][j - 1] != 'B' and not self._selected[i][j - 1]:
                                self._selected[i][j - 1] = True
                    except Exception as exceptObj:
                        pass
                    try:
                        if j < len(self._board[i]):
                            if self._board[i][j + 1] == 0 and not self._selected[i][j + 1]:
                                self.select(i,j+1)
                            if self._board[i][j + 1] != 0 and self._board[i][j + 1] != 'B' and not self._selected[i][j + 1]:
                                self._selected[i][j + 1] = True
                    except Exception as exceptObj:
                        pass
        except Exception as exceptObj:
            print()
        
    def selectFirst(self, i, j):
        try:
            if self.checkValid(i,j) == None:
                raise Exception
            bombCheck = False
            while not bombCheck:
                if self._board[i][j] != 0:
                    self.__init__(self._x, self._y, self._bombs)
                else:
                    bombCheck = True
                    self.select(i,j)
        except Exception as exceptObj:
            pass

    def flag(self, x, y):
        try:
            if self.checkValid(x,y) == None:
                raise Exception
            if self._flagged[x][y] == True:
                print("This coordinate has been already flagged")
            else:
                self._flagged[x][y] = True
        except Exception as exceptObj:
            pass
    
    def unflag(self, x, y):
        try:
            if self.checkValid(x,y) == None:
                raise Exception
            if self._flagged[x][y] == False:
                print("This coordinate has been already un-flagged")
            else:
                self._flagged[x][y] = False
        except Exception as exceptObj:
            pass

    def checkStatus(self):
        bombCheck = 0
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == 'B' and self._flagged[i][j] == True:
                    bombCheck += 1
        if bombCheck == self._bombs:
            self._status = "Won"
            return self._status
        else:
            return self._status

    def getSolution(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                    self.select(i,j)
        self.print()
