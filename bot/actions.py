from javascript import require

pathfinder = require('mineflayer-pathfinder')


def walk_to(bot, x, y, z):
    movements = pathfinder.Movements(bot)
    bot.pathfinder.setMovements(movements)
    goal = pathfinder.goals.GoalNear(x, y, z, 1)
    bot.pathfinder.setGoal(goal)