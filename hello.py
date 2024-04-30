from flask import Flask,render_template,request,redirect,url_for,jsonify
from datetime import datetime
from googletrans import Translator,LANGUAGES
import os,csv
from sudoku import Sudoku
from PIL import Image,ImageFilter
from random import sample,randint,choice
tran=Translator()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")


board = [""] * 9
current_player = "X"
counter=2
result=''
def check_winner():
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != "":  # checking along column
            return True # true represents win case
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != "": # checking along row
            return True
    if board[0] == board[4] == board[8] != "": # checking along diagonal 1
        return True
    if board[2] == board[4] == board[6] != "": # checking along diagonal 2
        return True
    return False # false will let the code to keep running

def check_tie():
    return "" not in board # for tie case none of the cells are empty

@app.route('/play', methods=['GET', 'POST'])
def play_tic_tac_toe():
    global current_player,board,result

    if request.method == 'POST':
        cell_index = int(request.form['cell'])
        if board[cell_index] == "":
            board[cell_index] = current_player
            if check_winner():
                board = [""] * 9 # clears the board
                result = f"Player {current_player} wins!"
                return render_template('hello.html', result=result,current_player=current_player, board=board, counter=1)
            elif check_tie():
                board = [""] * 9 # clears the board
                result = "It's a tie!"
                return render_template('hello.html',current_player=current_player,result=result, board=board, counter=0)
            else:
                current_player = "O" if current_player == "X" else "X"

    return render_template('hello.html', board=board, current_player=current_player,result=result,counter=2)

tasks = []
completed=[]
datet=0

@app.route('/todo')
def todo():
    return render_template('todo.html', tasks=tasks,completed=completed)

@app.route('/todo/add_task', methods=['POST'])
def add_task():
    global datet
    content = request.form.get('content')
    heading = request.form.get('heading')
    if content!="":
        datet=datetime.now().strftime("%c")
        tasks.append([content,datet,heading])
    return redirect(url_for('todo'))

@app.route('/todo/complete_task/<int:task_id>')
def complete_task(task_id):
    global datet
    datet=datetime.now().strftime("%c")
    if task_id < len(tasks):
        tasks[task_id][1]=datet
        completed.append(tasks[task_id])
        del tasks[task_id]
    return redirect(url_for('todo'))

@app.route('/todo/update_task/<int:task_index>', methods=['GET', 'POST'])
def update_task(task_index):
    if request.method == 'GET':
        task = tasks[task_index]
        return render_template('todo.html', tasks=tasks, completed=completed, task_to_update=task)
    elif request.method == 'POST':
        updated_content = request.form.get('newcontent')
        updated_heading = request.form.get('newheading')
        if updated_content != "":  
            tasks[task_index][0] = updated_content
            dat=datetime.now().strftime("%c")
            tasks[task_index][1]=dat
        if updated_heading != "":  
            tasks[task_index][2] = updated_heading
            dat=datetime.now().strftime("%c")
            tasks[task_index][1]=dat
        return redirect(url_for('todo'))
translated=""

@app.route('/todo/delete_task/<int:task_index>', methods=['GET', 'POST'])
def delete_task(task_index):
        del tasks[task_index]
        return redirect(url_for('todo'))
        
def get_language_code(lang):
    for code, name in LANGUAGES.items():
        if name.lower() == lang.lower():
            return code
    return None

@app.route('/translate', methods=['GET', 'POST']) 
def translate():
    global translated
    if request.method=='POST':
        text=request.form['text']
        lang=request.form['lang']
        code = lang if lang in LANGUAGES else get_language_code(lang)
        txt = tran.translate(text, dest=code)
        t=txt.text

        detected = tran.detect(text).lang
        return render_template("translate.html", text=t,detected=detected)
    else:
        return render_template("translate.html", text="No text translated yet")

@app.route("/tools/image/post", methods=['POST',"GET"])
def image():
    img=request.files['image']
    op=request.form['op']
    if img:
        os.makedirs("static/tools/image", exist_ok=True) 
        img.save(os.path.join("static/tools/image", img.filename))
        if op=="greyscale":
            grayscale_img = Image.open(f"static/tools/image/{img.filename}").convert('L')
            grayscale_img.save(f"static/tools/image/grayscale_{img.filename}")
            return render_template("image.html" ,name=img.filename,out=f"grayscale_{img.filename}")

        elif op=="blur":
            blur_img = Image.open(f"static/tools/image/{img.filename}")
            blur_img = blur_img.filter(ImageFilter.GaussianBlur(15))  
            blur_img.save(f"static/tools/image/blur_{img.filename}")
            return render_template("image.html" ,name=img.filename,out=f"blur_{img.filename}")
        elif op=="rotate":
            rotated_img = Image.open(f"static/tools/image/{img.filename}")
            rotated_img = rotated_img.rotate(90)
            rotated_img.save(f"static/tools/image/rotated_{img.filename}") 
            return render_template("image.html", name=img.filename, out=f"rotated_{img.filename}")
@app.route("/tools/image")
def img():
    name=""
    out=""
    return render_template("image.html",name=name,out=out)
useranime=[]  
search=""
imo=False
lst=""
userlist=["Romance"]
@app.route("/anime", methods=['GET','POST'])
def anime(): 
    global useranime,search,userlist,imo,lst
    if request.method=="POST":
        search=request.form["search"]
        lst=request.form["anime"]
    else:
        search=""
    if search=="imo":
        imo=True
    elif search=="imof":
        imo=False
    if lst!="":
       userlist.extend([i.rstrip(",") for i in lst.split()])
    with open(r"static\asset\anime.csv","r",encoding='utf-8') as fh:
        rd=csv.reader(fh)
        next(rd,None)
        ans=""
        useranime=list(rd)
        if search !="":
            for i in useranime:
                if i[1].lower()==search.lower():
                    ans=i
    if userlist!=[]:
        recomend=True
        recomlst=[]
        genre=max(userlist,key=lambda x: userlist.count(x))
        for i in useranime:
            if genre in i[2]:
                recomlst.append(i)
    print()
    if recomlst!=[]:
        recomlst=sample(recomlst,k=min(len(recomlst),5))
    else:
       recomlst=sample(useranime,k=5)
    useranime=sample(useranime,k=10)
    return render_template("anime.html",useranime=useranime,ans=ans,recomend=recomend,recomlst=recomlst,imo=imo)



ROWS = 8 # we set the numbers of rows and columns as 8*8 respectively for now. but can try to go for custom settings
COLS = 8
MINE_PROBABILITY = 0.1  # this here is the chace of a tile to be a mine 
board = [["" for _ in range(COLS)] for _ in range(ROWS)]  # this is the board that is containing the mines
display_board = [['' for _ in range(COLS)] for _ in range(ROWS)]  # this board is to be to displayed
num_mines = 0
def generate_board():
  global board,display_board,num_mines
  while num_mines < int(ROWS * COLS * MINE_PROBABILITY): # rows* cols * mine_probability is to get the total number of mines 
    row = randint(0, ROWS - 1)
    col = randint(0, COLS - 1)
    if board[row][col] != -1:  # to prevent placing of a mine on already existing mine
      board[row][col] = -1 # -1 is to denote a mine in the place
      # here we are alotting the tiles as mines
      num_mines += 1
  return board, display_board

def count_adjacent_mines(board, row, col): 
  count = 0
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if  board[i][j] == -1:
        count += 1
  return count

@app.route('/mine', methods=["GET", "POST"])
def mine():
  global board,display_board,num_mines
  if request.method == "GET":
    game_over = False  # Initialising the game 
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
  return redirect(url_for("mine")) 
@app.route('/rps')
def rps():
    return render_template('rpsindex.html')

@app.route('/rpsplay', methods=['POST'])
def rpsplay():
    choices = ['rock', 'paper', 'scissors']
    player_choice = request.json['choice']
    computer_choice = choice(choices)

    # Determine winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({'result': result,'delay': 3})

@app.route("/login")
def login():
    return redirect("http://10.128.5.173:8100/")

sudoku_game = Sudoku() #using Sudoku class defined in sudoku.py
sudoku_game.generate() # generating  a sudoku grid

@app.route('/sudoku')
def sudoku():
    return render_template('sudokuindex.html', grid=sudoku_game.get_grid())

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    grid = data['grid']
    sudoku_game.set_grid(grid) # return current state of sudoku grid
    sudoku_game.solve() # solves the grid
    return jsonify({'solution': sudoku_game.get_grid()}) # converts the above data into json type and return it

@app.route('/check_solution', methods=['POST'])
def check_solutionsudoku():
    data = request.json
    user_solution = data['grid']
    is_correct = sudoku_game.check_solution(user_solution)
    return jsonify({'is_correct': is_correct})
