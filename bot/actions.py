import threading
import time

from javascript import require

pathfinder = require('mineflayer-pathfinder')

max_distance = 1


def walk_to(bot, x, y, z):
    movements = pathfinder.Movements(bot)
    bot.pathfinder.setMovements(movements)
    movements.allowParkour = True
    movements.allowSprinting = True
    movements.allowJump = True
    movements.allowClimb = True
    movements.allowSwim = True
    movements.allowFall = True
    movements.allowOpenDoors = True
    movements.allowBreakBlocks = True
    movements.allowPlaceBlocks = True
    movements.allowUseItems = True
    movements.canScaffold = True
    goal = pathfinder.goals.GoalNear(x, y, z, 1)
    bot.pathfinder.setGoal(goal)
    
def nearest_entity(bot, entity_type):
    closest = None
    closest_dist = max_distance
    for key in bot.entities:
        try:
            entity = bot.entities[key]
            if entity is None:
                continue
            #print(f"Entity: {entity.name}, Type: {entity.type}")
            if entity.type != 'mob':
                continue
            if entity.type != 'hostile':
                continue
            dist = bot.entity.position.distanceTo(entity.position)
            if dist < closest_dist:
                closest = entity
                closest_dist = dist
        except:
            continue
            
    return closest

def defend(bot):
    target = nearest_entity(bot, 'mob')
    if target:
        bot.attack(target)
    
def start_threat_monitoring(bot):
    def monitor():
        while True:
            defend(bot)     
            time.sleep(2)       
    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()