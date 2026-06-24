from concurrent.futures import process
from javascript import require, On, Once

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
process = require('process')

death_counter = 0
kill_counter = 0
block_mine_counter = 0
block_place_counter = 0

options = {
    'host': process.argv[2],
    'port': process.argv[3],
    'username': process.argv[4],
    'password': process.argv[5]
}

bot = mineflayer.createBot(options)

@Once(bot, 'spawn')
def on_spawn(this, *args):
    bot.chat("Hola brochachos")
    
@On(bot, 'chat')
def on_chat(this, username, message, *rest):
    if username == bot.username:
        return #ignore self
    print(f"{username}: {message}")
    
@On(bot, 'death')
def on_death(this, *args):
    global death_counter
    death_counter += 1
    bot.chat("darn it")
    print("Bot died")
    print(f"Death count: {death_counter}")
    
@On(bot, 'health')
def on_health(this, *args):
    print(f"Bot health: {bot.health}, Food: {bot.food}")
    
@On(bot, 'enityDead')
def on_kill(this, *args):
    global kill_counter
    kill_counter += 1
    print(f"Kill count: {kill_counter}")
    
@On(bot, 'diggingCompleted')
def on_block_mine(this, *args):
    global block_mine_counter
    block_mine_counter += 1
    print(f"Block mine count: {block_mine_counter}")
