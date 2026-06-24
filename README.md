Minecraft AI Bot
A Python-based Minecraft bot built on mineflayer that plays the game autonomously — surviving, building, and learning over time. Powered by Claude (Anthropic) for in-game reasoning and chat, with a reinforcement learning layer to improve the bot's decision-making.

Goals
Autonomous survival and progression through Minecraft
Schematic-based building
Claude integration for in-game chat and high-level decision making (ReAct loop)
Reinforcement learning to improve bot behavior over time
Action logging and documentation of the bot's decisions

Tech Stack
Python — core bot logic and AI integration
mineflayer (Node.js) — Minecraft bot framework
mineflayer-pathfinder — movement and navigation
mineflayer-schem — schematic building
JSPyBridge (javascript pip package) — Python to Node.js bridge
Claude API (Anthropic) — agent reasoning and chat


Project Structure

Minecraft Bot/
├── main.py                 # Entry point
├── bot/
│   ├── core.py             # Bot creation and plugin loading
│   ├── events.py           # Event listeners
│   ├── actions.py          # Movement, digging, building, combat
│   └── state.py            # Game state reader
├── ai/
│   ├── claude.py           # Claude API integration
│   └── react_loop.py       # Observe → Think → Act cycle
├── rl/
│   ├── env.py              # Gym environment wrapper
│   └── rewards.py          # Reward functions
└── schematics/             # .schem files for building

Setup:
  Prerequisites
    Python 3.14+
    Node.js 21+
    Minecraft Java Edition
    Anthropic API key
    
Install

# Install Node.js dependencies
npm install mineflayer mineflayer-pathfinder mineflayer-schem prismarine-viewer

# Install Python dependencies
pip install javascript anthropic
Configuration
Create a .env file in the project root:


ANTHROPIC_API_KEY=your_key_here


Running

python main.py
Note: Your Minecraft server must be running in offline mode (online-mode=false in server.properties) for the bot to connect without Mojang authentication.

Roadmap
 Bot connection and basic events
 Movement and pathfinding
 Survival state machine (gather, craft, shelter)
 Claude ReAct loop integration
 Schematic building
 Reinforcement learning environment
