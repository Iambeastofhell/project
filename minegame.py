from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

ROWS = 8 # we set the numbers of rows and columns as 8*8 respectively for now. but can try to go for custom settings
COLS = 8
MINE_PROBABILITY = 0.1  # this here is the chace of a tile to be a mine 
board = [["" for _ in range(COLS)] for _ in range(ROWS)]  # this is the board that is containing the mines
display_board = [['' for _ in range(COLS)] for _ in range(ROWS)]  # this board is to be to displayed
num_mines = 0
def generate_board():
  global board,display_board,num_mines
  while num_mines < ROWS * COLS * MINE_PROBABILITY: # rows* cols * mine_probability is to get the total number of mines 
    row = random.randint(0, ROWS - 1)
    col = random.randint(0, COLS - 1)
    if board[row][col] != -1:  # to prevent placing of a mine on already existing mine
      board[row][col] = -1 # -1 is to denote a mine in the place
      # here we are alotting the tiles as mines
      num_mines += 1
  return board, display_board

def count_adjacent_mines(board, row, col): 
  count = 0
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if 0 <= i < ROWS and 0 <= j < COLS and board[i][j] == -1:
        count += 1
  return count

@app.route("/", methods=["GET", "POST"])
def index():
  global board,display_board,num_mines
  if request.method == "GET":
    game_over = False  # Initialising the  game state
    win = False
    return render_template("minesweeper.html", board=display_board, game_over=game_over, win=win)
  else:
    row = int(request.form["row"])
    col = int(request.form["col"])
    board, display_board = generate_board()
    if board[row][col] == -1:
      # When game finishes all mines are revealed
      for i in range(ROWS):
        for j in range(COLS):
          if board[i][j] == -1:
            display_board[i][j] = "*"
      return render_template("minesweeper.html", board=display_board, game_over=True)
    else:
      num_mines = count_adjacent_mines(board, row, col)
      display_board[row][col] = str(num_mines) if num_mines else ""
      # Check for win condition if all non-mine cells revealed
      win = True
      for i in range(ROWS):
        for j in range(COLS):
          if board[i][j] != -1 and display_board[i][j] == "":
            win = False
            break
      if win:
        return render_template("minesweeper.html", board=display_board, game_over=True, win=True)
      return render_template("minesweeper.html", board=display_board, game_over=False)  # Game continues

@app.route("/play_again")
def play_again():
  global board,display_board,num_mines
  board = [["" for _ in range(COLS)] for _ in range(ROWS)]  # Hidden board with mines
  display_board = [['' for _ in range(COLS)] for _ in range(ROWS)]  # Board to display
  num_mines = 0 # Reset game state and redirect to main page
  return redirect(url_for("index")) 