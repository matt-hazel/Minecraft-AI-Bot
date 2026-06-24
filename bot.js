const mineflayer = require('mineflayer')

const options = {
    host: process.argv[2],
    port: process.argv[3],
    username: process.argv[4],
    password: process.argv[5]
}

const bot = mineflayer.createBot(options)


// We start the program now by the following:
// node bot.js <host> <port> <username> <password>

const welcome = () => {
    bot.chat('Hola mi amigo(s)!')
}

bot.once('spawn', welcome)

