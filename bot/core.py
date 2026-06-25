from time import time
import sys
from javascript import require, On, Once
from actions import walk_to
from events import register_events


mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
process = require('process')

options = {
    'host': sys.argv[1],
    'port': sys.argv[2],
    'username': sys.argv[3],
    #'password': process.argv[4],
    #'version': '1.21.1'
}

bot = mineflayer.createBot(options)
bot.loadPlugin(pathfinder.pathfinder)

register_events(bot)