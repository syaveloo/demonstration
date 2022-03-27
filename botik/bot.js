// take discord.js classes
const { Client, Intents } = require("discord.js");
const { token } = require('./cfg.json')

// create client instance
const client = new Client({
  intents:['GUILDS',
          'DIRECT_MESSAGES',
          'GUILD_MESSAGES'],
  partials:['MESSAGE', 'CHANNEL'] });

// when ready tell me
client.once("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
})

client.on("messageCreate", msg => {
  console.log(`new message ${msg}`);
  if (msg.content === "ping") {
    msg.reply("pong");
  }
})

// login bot
client.login(token);
