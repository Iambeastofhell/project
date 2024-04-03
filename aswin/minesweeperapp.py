from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('aswinindex.html')

@app.route('/generate_board', methods=['POST'])
def generate_board(): # requesting user to tell number of rows and columns for making grid
    rows = int(request.form.get(str('rows')))
    cols = int(request.form.get(str('cols')))
    if rows == None or cols == None:
        return render_template('aswinindex.html') 
    # the code below is to generate a minesweeper grid 
    mines=int(rows*cols*0.1235) #12.35% chance of a cell to be a mine
    board = [[0] * cols for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), mines)

    for mine_position in mine_positions: # alloting cells to be mines
        row = mine_position // cols
        col = mine_position % cols
        board[row][col] = -1  # -1 represents a mine

        # Update adjacent cells
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < rows and 0 <= col + j < cols and board[row + i][col + j] != -1:
                    board[row + i][col + j] += 1

    return jsonify(board)

if __name__ == '__main__':
    app.run(debug=True)
