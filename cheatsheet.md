# Mineflayer Python Cheat Sheet

## Imports

```python
from javascript import require, On, Once
```

## Requiring npm packages

```python
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
```

## Creating the bot

```python
bot = mineflayer.createBot({
    'host': 'localhost',
    'port': 25565,
    'username': 'MyBot'
})
```

## Events

Use `@On` for events that fire repeatedly, `@Once` for events that fire one time.
The first argument is always `this` — you must include it but can ignore it.

```python
@Once(bot, 'spawn')
def on_spawn(this, *args):
    print('Bot spawned!')

@On(bot, 'chat')
def on_chat(this, username, message, *rest):
    if username == bot.username:
        return  # ignore the bot's own messages
    print(f'{username}: {message}')

@On(bot, 'death')
def on_death(this, *args):
    print('Bot died!')

@On(bot, 'health')
def on_health(this, *args):
    print(f'Health: {bot.health}, Food: {bot.food}')
```

### Common events
| Event | When it fires |
|---|---|
| `spawn` | Bot enters the world |
| `login` | Bot connects to the server |
| `chat` | A player sends a chat message |
| `death` | Bot dies |
| `health` | Health or food changes |
| `kicked` | Bot is kicked from server |
| `end` | Connection ends |

## Chatting

```python
bot.chat('Hello world!')
```

Max 256 characters. Add a delay between messages to avoid being kicked.

## Movement (requires mineflayer-pathfinder)

```python
pathfinder_pkg = require('mineflayer-pathfinder')
bot.loadPlugin(pathfinder_pkg.pathfinder)

from javascript import require
movements = pathfinder_pkg.Movements(bot)
bot.pathfinder.setMovements(movements)

GoalBlock = pathfinder_pkg.goals.GoalBlock
GoalNear = pathfinder_pkg.goals.GoalNear

# Walk to a specific block
bot.pathfinder.setGoal(GoalBlock(x, y, z))

# Walk near a position (within 2 blocks)
bot.pathfinder.setGoal(GoalNear(x, y, z, 2))
```

## Game state

```python
bot.health          # 0-20
bot.food            # 0-20
bot.entity.position # {x, y, z}
bot.username        # bot's name
bot.players         # dict of online players
bot.inventory       # inventory object
```

## Players

```python
# Get a player's position
player = bot.players['PlayerName']
pos = player.entity.position

# Walk to a player
bot.pathfinder.setGoal(GoalNear(pos.x, pos.y, pos.z, 2))
```

## Blocks

```python
# Get block at position
block = bot.blockAt(bot.entity.position)

# Dig a block
import asyncio
bot.dig(block)

# Place a block (must be holding it)
bot.placeBlock(reference_block, face_vector)
```

## Inventory

```python
# Find an item by name
item = bot.inventory.findInventoryItem('oak_log', None, False)

# Equip an item
bot.equip(item, 'hand')
```

## Entities

```python
# Get all nearby entities
entities = bot.entities

# Find nearest entity by type
def nearest_entity(type_name):
    closest = None
    closest_dist = float('inf')
    for entity in bot.entities.values():
        if entity.type == type_name:
            dist = bot.entity.position.distanceTo(entity.position)
            if dist < closest_dist:
                closest = entity
                closest_dist = dist
    return closest

# Attack an entity
bot.attack(entity)
```

## JS vs Python syntax differences

| JS | Python |
|---|---|
| `bot.on('event', () => {})` | `@On(bot, 'event')` decorator |
| `bot.once('event', () => {})` | `@Once(bot, 'event')` decorator |
| `console.log()` | `print()` |
| `const x = require('pkg')` | `x = require('pkg')` |
| Arrow functions `() =>` | Not used — use decorators |
| `bot.entity.position.x` | `bot.entity.position.x` (same) |

## Tips

- Always include `*args` or `*rest` in event callbacks to catch extra arguments
- `@On` callbacks run in a separate thread — be careful with shared state
- Pylance may show import warnings for `javascript` — these are harmless
- Use `offline-mode=true` in `server.properties` for local testing without auth
