pystats
=======

pystats plugin for twitchy bot by Matt McNamara https://github.com/MattMcNam/twitchy
Sizzling stats by SizzlingCalamari and dy/dx

pystats plugin is used to pull the most recent sizzling stats log file fromsizzlingstats.com. The triggering command
is !stats <str> with <str> being an optional parameter. This parameter is defaulted to the twitch channel username if
it is not stated in the chat command. The bot will find the most recent log for the steamID provided in the command and
post it as a message in chat.

Installation:
to install pystats onto your twitchy bot, copy the pystats folder into the plugins folder. More information
on the architecture of twitchy bot and plugins can be found on the github.

to-do:
add an alt-case for players to redirect twitch usernames to steamurls. text document
add a confirmation notice if the lobby info is more than a day old
