import pygwidgets

#This class is meant to create the right side buttones of the game not the 9*9 board buttons
class button:
  def __init__(self, window, topLeft, upImg, downImg, overImg, disImg):
    self.window = window
    self.topLeft = topLeft #touple (x,y) position on the UI
    self.upImg = upImg
    self.downImg = downImg
    self.overImg = overImg
    self.disImg = disImg

  def create_button(self):
    button = pygwidgets.CustomButton(self.window, self.topLeft,
                                      self.upImg,
                                      down = self.downImg,
                                      over = self.overImg,
                                      disabled = self.disImg)
    return button
    #can call .handleEvent() or .show() on the returned output

class matrix:
    def __init__(self, values):
        self.values = values #the entire matrix in the format [[0, 0, 0,...], [0, 0, 0, ...], ...]

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values

    def showValues(self): #print the entire matrix row by row
        for row in self.values:
            print(row)

    def setValue(self, value, coord): #row is the x-position, col is the y-position; (1,1) top left, (9,9) bottom right
        row = coord[0]
        col = coord[1]
        if (value > 9 or value < 0):
            raise ValueError("Value must be between 0 and 9.")
        elif (row > 9 or row < 1):
            raise ValueError("Row position must be between 1 and 9.")
        elif (col > 9 or col < 1):
            raise ValueError("Column position must be between 1 and 9.")
        else:
            self.values[row-1][col-1] = value
            
class board(matrix):
    def __init__(self, values):
        super().__init__(values)

    def check(self, answersBoard): #check values of current board against the answers board
        if isinstance(answersBoard, board):
            incorrect = []
            for xpos in range(9):
                for ypos in range(9):
                    if self.values[xpos][ypos] != answersBoard.values[xpos][ypos]:
                        incorrect.append((xpos+1, ypos+1))
        else:
            raise TypeError("Answers board must be a board.")
        if len(incorrect) == 0:
            print("All positions are correct.")
            return
        else:
            print("There are incorrect positions.")
            return incorrect #returns coordinates of incorrect values

    def draw(self): #draw out each number of the board within the program (permanent, not changeable by user)
        for row in range(9):
            for column in range(9):
                if self.values[row][column] == 1:
                    window.blit(n1, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 2:
                    window.blit(n2, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 3:
                    window.blit(n3, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 4:
                    window.blit(n4, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 5:
                    window.blit(n5, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 6:
                    window.blit(n6, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 7:
                    window.blit(n7, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 8:
                    window.blit(n8, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))
                elif self.values[row][column] == 9:
                    window.blit(n9, (loc_BoardCell[row][column][0],loc_BoardCell[row][column][1]))

class possi:
    def __init__(self):
        self.cand = [0, 0, 0, 0, 0, 0, 0, 0, 0] #candidates are formatted as  where 0 = not a possibility

    def addCandidate(self, value):
        if (value > 9 or value < 1):
            raise ValueError("Candidate value must be between 1 and 9.")
        else:
            self.cand[value-1] = value

    def removeCandidate(self, value):
        if (value > 9 or value < 1):
            raise ValueError("Candidate value must be between 1 and 9.")
        else:
            self.cand[value-1] = 0
            
# Each number (0 to 9) should be created as the object of this class in the beginning of the code --> one = Number(1,..)
# 0 is the case when the cell must be empty and yet to be solved by the player (an empty squre button)


class number:
  def __init__(self, value, upImg = "numbers/n0.png", downImg = "numbers/n0g.png", overImg = "numbers/n0.png"):
    self.value = value  #int
    self.upImg = upImg
    self.downImg = downImg
    self.overImg = overImg

    @property
    def value(self):
      return self._value

    @value.setter
    def value(self, value):
      if value > 9 or value < 0:
        raise ValueError("Value must be between 0 and 9.")
      else:
        self._value = value
        
import pygwidgets


class cell:
  def __init__(self, window, value, topLeft):  #"value" (given as int) is the number should be on the cell(button) based on the unsolved matrix and if value=0 means this is a cell that player needs to solve and so it's empty
    self.window = window                                                     #"int_Num" is the dict in the format 0:Number(0,...), 1:Number(1,...) or 1:obj from NUmber class #see the note at the end
    self.value = value #obj from Number class
    self.topLeft = topLeft #touple (x,y) position on the UI
    self.num = int_num[value]
    #self.possi = possi  #obj from possi class
    #self.sound = sound
    #possi_list = [] #list of possi buttons

  @property
  def topLeft(self):
    return self._topLeft

  @topLeft.setter
  def topLeft(self, topLeft):
    self._topLeft = topLeft

  #This can also be part of the initializer but the it would be hard to do the handle event and there is no obj to call obj.handleEvent() on
  def create_cell(self):
    cell_button = pygwidgets.CustomButton(self.window, self.topLeft,
                                            up = self.num.upImg,
                                            down = self.num.downImg,
                                            over = self.num.overImg
                                         )
    #But in the function we return an obj from pygwidgets.CustomButton so handleEvent() can be called  #NOTE: we call .draw() as a built in function in pygwidgets in main
    return cell_button
  
class cellBoard(cell):
    def __init__(self, window, value, topLeft):
      super().__init__(window, value, topLeft)
      self.num = int_num[value]
    
    def create_cell(self):
      cell_button = pygwidgets.CustomRadioButton(self.window, self.topLeft, "Board",
                                                 on = self.num.downImg,
                                                 off = self.num.upImg,
                                                 value = False,
                                                 onDown = self.num.downImg,
                                                 offDown = self.num.upImg)
      return cell_button

loc_BoardCell = [
    [(125,41), (200,41), (275,41), (350,41), (425,41), (500,41), (575,41), (650,41), (725,41)],
    [(125,116), (200,116), (275,116), (350,116), (425,116), (500,116), (575,116), (650,116), (725,116)],
    [(125,191), (200,191), (275,191), (350,191), (425,191), (500,191), (575,191), (650,191), (725,191)],
    [(125,266), (200,266), (275,266), (350,266), (425,266), (500,266), (575,266), (650,266), (725,266)],
    [(125,341), (200,341), (275,341), (350,341), (425,341), (500,341), (575,341), (650,341), (725,341)],
    [(125,416), (200,416), (275,416), (350,416), (425,416), (500,416), (575,416), (650,416), (725,416)],
    [(125,491), (200,491), (275,491), (350,491), (425,491), (500,491), (575,491), (650,491), (725,491)],
    [(125,566), (200,566), (275,566), (350,566), (425,566), (500,566), (575,566), (650,566), (725,566)],
    [(125,641), (200,641), (275,641), (350,641), (425,641), (500,641), (575,641), (650,641), (725,641)],
]

loc_Possi = [(303,735),(378, 735),(453,735),(528,746),(603,735),(678,735),(753,735),(828,735),(903, 735)]
loc_Input = [(30,41),(30,116),(30,191),(30,266),(30,341),(30,416),(30,491),(30,566),(30,641)]

boardA = board([
 [0, 6, 2, 5, 0, 0, 3, 8, 7],
 [1, 3, 0, 6, 8, 0, 0, 0, 0],
 [7, 0, 0, 0, 0, 2, 0, 0, 6],
 [0, 0, 0, 7, 3, 8, 2, 5, 4],
 [5, 2, 0, 0, 0, 0, 0, 1, 8],
 [8, 7, 4, 2, 1, 5, 0, 0, 0],
 [9, 0, 0, 4, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 7, 9, 0, 4, 2],
 [2, 4, 6, 0, 0, 3, 8, 7, 0]
])

answersA = board([
 [4, 6, 2, 5, 9, 1, 3, 8, 7],
 [1, 3, 9, 6, 8, 7, 4, 2, 5],
 [7, 5, 8, 3, 4, 2, 1, 9, 6],
 [6, 9, 1, 7, 3, 8, 2, 5, 4],
 [5, 2, 3, 9, 6, 4, 7, 1, 8],
 [8, 7, 4, 2, 1, 5, 9, 6, 3],
 [9, 8, 7, 4, 2, 6, 5, 3, 1],
 [3, 1, 5, 8, 7, 9, 6, 4, 2],
 [2, 4, 6, 1, 5, 3, 8, 7, 9]
])

boardB = board([
 [8, 3, 5, 0, 2, 1, 4, 0, 0],
 [1, 0, 7, 4, 6, 5, 0, 3, 0],
 [0, 0, 2, 3, 0, 0, 1, 5, 9],
 [0, 0, 8, 5, 0, 0, 6, 0, 1],
 [0, 5, 4, 0, 1, 0, 9, 8, 0],
 [9, 0, 6, 0, 0, 2, 5, 0, 0],
 [2, 4, 9, 0, 0, 7, 3, 0, 0],
 [0, 8, 0, 2, 3, 6, 7, 0, 4],
 [0, 0, 3, 1, 4, 0, 8, 2, 5]
])

answersB = board([
 [8, 3, 5, 9, 2, 1, 4, 6, 7],
 [1, 9, 7, 4, 6, 5, 2, 3, 8],
 [4, 6, 2, 3, 7, 8, 1, 5, 9],
 [3, 2, 8, 5, 9, 4, 6, 7, 1],
 [7, 5, 4, 6, 1, 3, 9, 8, 2],
 [9, 1, 6, 7, 8, 2, 5, 4, 3],
 [2, 4, 9, 8, 5, 7, 3, 1, 6],
 [5, 8, 1, 2, 3, 6, 7, 9, 4],
 [6, 7, 3, 1, 4, 9, 8, 2, 5]
])

boardC = board([
 [0, 7, 0, 5, 0, 0, 2, 4, 0],
 [1, 0, 0, 6, 4, 2, 7, 0, 3],
 [2, 0, 4, 7, 9, 8, 5, 0, 6],
 [7, 0, 1, 0, 3, 5, 0, 0, 4],
 [8, 2, 0, 0, 7, 0, 0, 6, 5],
 [5, 0, 0, 1, 2, 0, 8, 0, 7],
 [6, 0, 7, 3, 5, 1, 4, 0, 2],
 [3, 0, 5, 2, 8, 4, 0, 0, 9],
 [0, 8, 2, 0, 0, 7, 0, 5, 0]
])

answersC = board([
 [9, 7, 6, 5, 1, 3, 2, 4, 8],
 [1, 5, 8, 6, 4, 2, 7, 9, 3],
 [2, 3, 4, 7, 9, 8, 5, 1, 6],
 [7, 6, 1, 8, 3, 5, 9, 2, 4],
 [8, 2, 3, 4, 7, 9, 1, 6, 5],
 [5, 4, 9, 1, 2, 6, 8, 3, 7],
 [6, 9, 7, 3, 5, 1, 4, 8, 2],
 [3, 1, 5, 2, 8, 4, 6, 7, 9],
 [4, 8, 2, 9, 6, 7, 3, 5, 1]
])

########ACTUAL GAME #######

import pygame
from pygame.locals import *
import sys

WD_WIDTH = 1280 # change later
WD_HEIGHT = 840 # change later
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set up background and layouts
pygame.init()
window = pygame.display.set_mode((WD_WIDTH, WD_HEIGHT))

background_surface = pygame.Surface(window.get_size())
background_surface.fill((0, 220, 0)) # not presenting
font_title = pygame.font.Font(None, 128)
text_surface = font_title.render("Sudoku", True, WHITE)
font_sub = pygame.font.Font(None, 32)
input_text = font_sub.render("Inputs:", True, WHITE)
pos_text = font_sub.render("Possibilities:", True, WHITE)
##########
int_num = {
    0:number(0), #obj from Number class
    1:number(1,"numbers/n1b.png","numbers/n1g.png","numbers/n1g.png"),
    2:number(2,"numbers/n2b.png","numbers/n2g.png","numbers/n2g.png"),
    3:number(3,"numbers/n3b.png","numbers/n3g.png","numbers/n3g.png"),
    4:number(4,"numbers/n4b.png","numbers/n4g.png","numbers/n4g.png"),
    5:number(5,"numbers/n5b.png","numbers/n5g.png","numbers/n5g.png"),
    6:number(6,"numbers/n6b.png","numbers/n6g.png","numbers/n6g.png"),
    7:number(7,"numbers/n7b.png","numbers/n7g.png","numbers/n7g.png"),
    8:number(8,"numbers/n8b.png","numbers/n8g.png","numbers/n8g.png"),
    9:number(9,"numbers/n9b.png","numbers/n9g.png","numbers/n9g.png")
}
###########

n0 = pygame.image.load('numbers/n0.png')
n1 = pygame.image.load('numbers/n1.png')
n2 = pygame.image.load('numbers/n2.png')
n3 = pygame.image.load('numbers/n3.png')
n4 = pygame.image.load('numbers/n4.png')
n5 = pygame.image.load('numbers/n5.png')
n6 = pygame.image.load('numbers/n6.png')
n7 = pygame.image.load('numbers/n7.png')
n8 = pygame.image.load('numbers/n8.png')
n9 = pygame.image.load('numbers/n9.png')

stare = button(window, (850, 450), upImg = "buttons/stare_up.png", downImg = "buttons/stare_up.png", overImg = "buttons/stare_over.png", disImg = "buttons/stare_up.png")
new = button(window, (850, 525), upImg = "buttons/new_up.png", downImg = "buttons/new_up.png", overImg = "buttons/new_over.png", disImg = "buttons/new_up.png")
end = button(window, (850, 600), upImg = "buttons/end_up.png", downImg = "buttons/end_up.png", overImg = "buttons/end_over.png", disImg = "buttons/end_up.png")


def background():
    # grid
    pygame.draw.rect(window, WHITE, (125, 41, 675, 675))
    pygame.draw.line(window, BLACK, (350, 41), (350, 716), 5) # vertical line
    pygame.draw.line(window, BLACK, (575, 41), (575, 716), 5)
    pygame.draw.line(window, BLACK, (425, 41), (425, 716), 1)
    pygame.draw.line(window, BLACK, (500, 41), (500, 716), 1)
    pygame.draw.line(window, BLACK, (650, 41), (650, 716), 1)
    pygame.draw.line(window, BLACK, (725, 41), (725, 716), 1)
    pygame.draw.line(window, BLACK, (200, 41), (200, 716), 1)
    pygame.draw.line(window, BLACK, (275, 41), (275, 716), 1)
    pygame.draw.line(window, BLACK, (125, 266), (800, 266), 5) # horizontal line
    pygame.draw.line(window, BLACK, (125, 491), (800, 491), 5)
    pygame.draw.line(window, BLACK, (125, 116), (800, 116), 1)
    pygame.draw.line(window, BLACK, (125, 191), (800, 191), 1)
    pygame.draw.line(window, BLACK, (125, 341), (800, 341), 1)
    pygame.draw.line(window, BLACK, (125, 416), (800, 416), 1)
    pygame.draw.line(window, BLACK, (125, 566), (800, 566), 1)
    pygame.draw.line(window, BLACK, (125, 641), (800, 641), 1)

    # right side buttons
    pygame.draw.rect(window, (255, 255, 255), (850, 225, 350, 100)) # time display
    pygame.draw.rect(window, (255, 255, 255), (850, 375, 300, 50))

    # possibilities
    pygame.draw.rect(window, WHITE, (30, 41, 75, 675))
    pygame.draw.line(window, BLACK, (30, 116), (105, 116), 3)
    pygame.draw.line(window, BLACK, (30, 191), (105, 191), 3)
    pygame.draw.line(window, BLACK, (30, 266), (105, 266), 3)
    pygame.draw.line(window, BLACK, (30, 341), (105, 341), 3)
    pygame.draw.line(window, BLACK, (30, 416), (105, 416), 3)
    pygame.draw.line(window, BLACK, (30, 491), (105, 491), 3)
    pygame.draw.line(window, BLACK, (30, 566), (105, 566), 3)
    pygame.draw.line(window, BLACK, (30, 641), (105, 641), 3)

    pygame.draw.rect(window, WHITE, (303, 735, 675, 75))
    pygame.draw.line(window, BLACK, (378, 735), (378, 810), 3)
    pygame.draw.line(window, BLACK, (453, 735), (453, 810), 3)
    pygame.draw.line(window, BLACK, (528, 735), (528, 810), 3)
    pygame.draw.line(window, BLACK, (603, 735), (603, 810), 3)
    pygame.draw.line(window, BLACK, (678, 735), (678, 810), 3)
    pygame.draw.line(window, BLACK, (753, 735), (753, 810), 3)
    pygame.draw.line(window, BLACK, (828, 735), (828, 810), 3)
    pygame.draw.line(window, BLACK, (903, 735), (903, 810), 3)

currentBoard = board(boardA.values)
##########
input_button_list= []
for i in range(1,10):
  c = cell(window, i, loc_Input[i-1])
  b = c.create_cell()
  input_button_list.append((b,c))

##########
board_button_list= []
for row in range(9):
  for col in range(9):
    if currentBoard.values[row][col] == 0:
      c = cellBoard(window, 0, loc_BoardCell[row][col])
      b = c.create_cell()
      board_button_list.append((b,c))
##########

stareButton = stare.create_button()
newButton = new.create_button()
endButton = end.create_button()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        for b,c in board_button_list: #board selection
           if b.handleEvent(event):
              print(c.topLeft)

        for b,c in input_button_list: #input selection
           if b.handleEvent(event):
              for bu,ce in board_button_list:
                 if bu.getValue() == True:
                    print(ce.value)
                    print(c.value)
                    ce.value = c.value
                    bu = ce.create_cell()
        
        if newButton.handleEvent(event):
          if currentBoard.values == boardA.values:
            currentBoard.values = boardB.values
          elif currentBoard.values == boardB.values:
            currentBoard.values = boardC.values
          elif currentBoard.values == boardC.values:
            currentBoard.values = boardA.values

    window.blit(text_surface, (850, 70))
    window.blit(input_text, (30, 12))
    window.blit(pos_text, (135, 760))

    background()
    for b,c in input_button_list:
      b.draw()
    for b,c in board_button_list:
      b.draw()
    stareButton.draw()
    newButton.draw()
    endButton.draw()
    currentBoard.draw()
    pygame.display.update()

    #pygame.display.flip()