import discord
from discord.ext import commands

import main

client = commands.Bot(command_prefix = "." )

chess_figures = {"p":"♟", "P":"♙", "Q":"♕", "q":"♕", "N":"♘", "n":"♞", "R":"♖", "r":"♜", "B":"♗", "b":"♝", "K":"♔", "k":"♚", "/":"\n"}
for i in range(1, 9):
	chess_figures[f"{i}"] = "x"*i
chess_figures = str.maketrans(chess_figures)

@client.command()
async def start_game(ctx, mention : discord.Member):
	if main.new_game(ctx.author.id, mention.id):
		return await ctx.send("У вас уже есть активная игра")
	board = main.chess.Board()
	while not board.is_variant_end():
		board_info = board.board_fen()
		await ctx.send("```"+board_info.translate(chess_figures)+"```")
		while True:
			try:
				message = await client.wait_for("message", check = lambda msg: msg.author.id==ctx.author.id and board.turn or msg.author.id==mention.id and not board.turn)
				move = main.chess.Move.from_uci(message.content)
				if (board.is_legal(move)):
					board.push(move)
					break
				else:
					await ctx.send("Невозможный ход")
			except ValueError:
				pass
	main.stop_game(ctx.author.id, mention.id)
client.run(TOKEN)