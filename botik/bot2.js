const Discord = require("discord.js");
const { token } = require('./cfg.json');
const client = new Discord.Client({
    intents: [
        /*
            Intents 'GUILDS' is required
            if you wish to receive (message) events
            from guilds as well.

            If you don't want that, do not add it.
            Your bot will only receive events
            from Direct Messages only.
        */
        'GUILDS',
        'DIRECT_MESSAGES',
        'GUILD_MESSAGES'
    ],
    partials: ['MESSAGE', 'CHANNEL'] // Needed to get messages from DM's as well
});
const PREFIX = '!';

client.on('ready', () =>{
    console.log('Bot Online! Woohoo!');
});


client.on('messageCreate', message =>{
    console.log('Message registered!');
});

client.login(token);
