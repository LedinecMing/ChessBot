import random

import chess.svg


def take_figures_uci(game_board):
    """
    Получение списка всех фигур которыми можно сделать ход
    :param game_board: Доска
    :return: Список фигур в формате uci
    """

    figures_for_take = []

    for i in game_board.legal_moves:
        if game_board.uci(i)[:2] not in figures_for_take:
            figures_for_take.append(game_board.uci(i)[:2])

    return figures_for_take


def take_figures_move(game_board, figure):
    """
    Получение всех возможных ходов для фигуры
    :param game_board: Доска
    :param figure: Выбранная фигура в формате uci
    :return: Список возможных ходов в формате uci
    """
    figure_move = []

    for i in game_board.legal_moves:
        if game_board.uci(i)[:2] == figure:
            figure_move.append(game_board.uci(i)[2:])

    return figure_move


board = chess.Board()  # Создать доску

# Генерация 10 случайных ходов из возможных
for i in range(10):
    figures = take_figures_uci(board)  # Получение всех возможных фигур для хода
    my_figure = random.choice(figures)  # Взять случайную фигуру для совершения хода
    figure_move = take_figures_move(board, my_figure)  # Получение всех возможных ходов для выбранной фигру
    my_move = random.choice(figure_move)  # Выбрать случайный ход

    board.push_san(f'{my_figure}{my_move}')  # Отправить ход на доску
    print(board, end='\n\n')  # Отрисовать доску в консоли
    move = chess.Move.from_uci(f'{my_figure}{my_move}')  # Сохранить ход

    img = chess.svg.board(board, lastmove=move, size=350)  # Создать SVG с последним ходом

    # записть SVG в файл для просмотра
    with open(f'game_svg/board {i}.svg', 'w') as f:
        f.write(img)
