from flask import Flask, render_template, request, jsonify
from sudoku import Sudoku

app = Flask(__name__)

sudoku_game = Sudoku()
sudoku_game.generate()

@app.route('/')
def index():
    return render_template('sudokuindex.html', grid=sudoku_game.get_grid())

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    grid = data['grid']
    sudoku_game.set_grid(grid)
    sudoku_game.solve()
    return jsonify({'solution': sudoku_game.get_grid()})

@app.route('/check_solution', methods=['POST'])
def check_solution():
    data = request.json
    user_solution = data['grid']
    is_correct = sudoku_game.check_solution(user_solution)
    return jsonify({'is_correct': is_correct})

if __name__ == '__main__':
    app.run(debug=True)
