import discord
from discord.ext import commands
# Define the board as a 3x3 array.
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
# Define the players as 'X' and 'O'.
players = ['X', 'O']
# Choose the first player randomly.
current_player = random.choice(players)
# Create the Discord bot.
bot = commands.Bot(command_prefix='!')
# Define the `tictactoe` command.
@bot.command()
async def tictactoe(ctx):
    # Check if the user is in a voice channel.
    if not ctx.author.voice:
        await ctx.send('You must be in a voice channel to play Tic Tac Toe.')
        return
    # Get the user's voice channel.
    voice_channel = ctx.author.voice.channel
    # Get the user's name.
    user_name = ctx.author.name
    # Send a message to the user's voice channel.
    await voice_channel.send(f'Welcome to Tic Tac Toe, {user_name}!')
    # Start the game loop.
    while True:
        # Display the board to the user.
        await voice_channel.send(embed=board_embed)
        # Get the user's move.
        move = await get_user_move(ctx)
        # Update the board with the user's move.
        board[move[0]][move[1]] = current_player
        # Check if the game is over.
        if check_winner(board):
            await voice_channel.send(embed=winner_embed)
            break
        # Switch players.
        current_player = players[players.index(current_player) ^ 1]
# Define the function to get the user's move.
async def get_user_move(
