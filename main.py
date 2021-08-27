import chess
import chess.svg

board = chess.Board()

img = chess.svg.board(board, size=350)

print(img)