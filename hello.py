from flask import Flask,render_template,request,jsonify,redirect,url_for
from datetime import datetime
from googletrans import Translator,LANGUAGES
import os
from PIL import Image,ImageFilter
tran=Translator()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("start.html")
# @app.route('/hello')
# def hello():
#     return render_template("hello.html")

board = [""] * 9
current_player = "X"

def check_winner():
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != "":
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != "":
            return True
    if board[0] == board[4] == board[8] != "":
        return True
    if board[2] == board[4] == board[6] != "":
        return True
    return False

def check_tie():
    return "" not in board
@app.route('/play', methods=['GET', 'POST'])
def play_tic_tac_toe():
    global current_player,board

    if request.method == 'POST':
        cell_index = int(request.form['cell'])
        if board[cell_index] == "":
            board[cell_index] = current_player
            if check_winner():
                board = [""] * 9
                current_player = "X"
                result = f"Player {current_player} wins!"
                return render_template('hellores.html', result=result, board=board)
            elif check_tie():
                result = "It's a tie!"
                return render_template('hellores.html', result=result, board=board)
            else:
                current_player = "O" if current_player == "X" else "X"

    return render_template('hello.html', board=board, current_player=current_player)


# Sample card data
cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']

# Global variables to keep track of the game state
flipped_cards = []
matched_pairs = 0
posttime=0
completedtime=0

@app.route('/card')
def card():
    return render_template('index2.html')

@app.route('/get_cards')
def get_cards():
    import random
    random.shuffle(cards)
    return jsonify(cards)

@app.route('/flip_card', methods=['POST'])
def flip_card():
    global flipped_cards

    # Get index of the flipped card from the request
    card_index = int(request.json['card_index'])

    # Ensure the card is not already flipped
    if card_index not in flipped_cards:
        flipped_cards.append(card_index)

    return jsonify(flipped_cards)

@app.route('/check_match', methods=['POST'])
def check_match():
    global flipped_cards, matched_pairs

    # Get the indices of the flipped cards from the request
    card_indices = request.json['card_indices']

    # Check if the two flipped cards match
    if len(card_indices) == 2:
        card1 = cards[card_indices[0]]
        card2 = cards[card_indices[1]]

        if card1 == card2:
            matched_pairs += 1
            if matched_pairs == len(cards) / 2:
                return jsonify({'status': 'win'})
            else:
                return jsonify({'status': 'match'})
        else:
            flipped_cards = []

    return jsonify({'status': 'no_match'})

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
updatedid=0
@app.route('/todo/update_task/<int:task_id>')
def update_task(task_id):
    global updateid
    updatedid=task_id
    return redirect(url_for('update'))

@app.route("/updatetodo",  methods=['GET', 'POST'])
def update():
    newhead=request.form.get('heading')
    # newhead=newhead.text
    ntext=request.form.get('note')
    if newhead!="":
        tasks[updatedid][2]=newhead
    elif ntext!="":
        tasks[updatedid][0]=ntext
    else:
        return redirect(url_for("/todo"))
    dat=datetime.now().strftime("%c")
    tasks[updatedid][1]=dat
    return redirect(url_for("todo"))


translated=""


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
# if __name__ == '__main__':
#     app.run(debug=False,host='0.0.0.0')
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
            blur_img = blur_img.filter(ImageFilter.BoxBlur(15))  
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