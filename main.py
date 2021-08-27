import chess.svg

board = chess.Board()  # Создать доску
print(board.legal_moves)  # Показать возможнжные ходы

move = chess.Move.from_uci("g1f3")  # Сделать ход
board.push(move)  # Отправить ход на доску

img = chess.svg.board(board, lastmove=move, size=350)  # Создать SVG с последним ходом

# записть SVG в файл для просмотра
with open('board.svg', 'w') as f:
    f.write(img)
