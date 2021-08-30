from SQLdb import DB
import chess
current_games = DB("games")
current_games.create("games", "(id0 INT, id1 INT)")

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

def new_game(id0, id1):
	if current_games.get("games", "*", f"WHERE id0={id0} AND id1={id1}") == ():
		current_games.add("games", f"({id0}, {id1})")
		return True
	else:
		return False

def stop_game(id0, id1):
	if current_games.get("games", "*", f"WHERE id0={id0} AND id1={id1}") != ():
		current_games.cursor.execute(f"DELETE FROM games WHERE id1={id1} AND id0={id0}")
		return True
	else:
		return False
