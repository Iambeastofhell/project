from flask import Flask, render_template, request, jsonify
from sudoku import Sudoku

app = Flask(__name__)

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


