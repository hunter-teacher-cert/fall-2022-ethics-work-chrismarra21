#https://py3.codeskulptor.org/#user307_VR9Kig4dOZ_3.py
#Christine Marra
#CSCI 77800 Fall 2022
#Collaborators: Maxwell Yearwood
#Consulted



# PYTHON CODE
from array import*


"""The Rules of Life:
   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.
      ** two conditions
   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.
      ** two conditions
   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.
      ** one condition
   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation."""




  #create, initialize, and return  empty board (all cells dead) represented by 0's
def createNewBoard(numRows, numCols ):
    board = []
    

    for r in range(numRows):
        columnElements = []
        for c in range(numCols):
            columnElements.append(0)
        board.append(columnElements)
                
    return board;
    
 
# print the board to the terminal (screen)
def printBoard(board ):
  
      for row in board:         
          for col in row:
              print(col, end = " ") #inserts a space after each entry
            
          print()
        
  
  


  #set cell (r,c) to val
  #used in Main to default dead cells
def setCell(board, r, c, val ):
    board[r][c] = val
  

#//return number of living neigbours of board[r][c]
def countNeighbours(board, r, c):
    count = 0
  
    for i in range(len(board)): #loops through each row one element before,element location and one element after.
        for j in range(len(board[0])):   #loops through each column
             if (r-1 <= i and i <= r +1) and (c-1 <= j and j <= c+1) and (not(i == r and j ==c)) and board[i][j] == 'X':
                count += 1
    return count


#precond: given a board and a cell
#postcond: return next generation cell state based on CGOL rules
#(alive 'X', dead '0')
def getNextGenCell(board, r , c, count):

    count = countNeighbours(board,r,c)
    if board[r][c]== 'X':
        if count < 2 or count > 3:
           nextGen = '0'
    elif board[r][c]== '0':
        if count == 3:
         nextGen = 'X'
    return nextGen
    



# generate and return a new board representing next generation
# newBoard is being filled with neighbour counts

def generateNextBoard(board):
    newBoard = []
    for r in range(len(board)):
        columnElements = []
        for c in range(len(board[0])):
            columnElements.append(countNeighbours(board, r, c))
        newBoard.append(columnElements)

    for r in range(len(board)):
        columnElements = []
        for c in range(len(board[0])):
            board.append(getNextGenCell(board,r,c, newBoard[r][c]))
    return board
  

  


# Test #1 
board = []
    
board = createNewBoard(5,5);
printBoard( board );


#breathe life into some cells:
setCell(board, 0, 0, 'X')
setCell(board, 0, 1, 'X')
setCell(board, 1, 0, 'X')
print()
printBoard( board )

      


#TASK:
# Once your initial version is running,
#try out different starting configurations of living cells...
#(Feel free to comment out the above three lines.)*/
    
print("Gen X:")
 
printBoard(board)
print("--------------------------\n\n")
board = generateNextBoard(board)
println("Gen X+1:")
printBoard(board)
print("--------------------------\n\n")
