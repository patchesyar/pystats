"""
pystats plugin for twitchy bot written by John "Tom 'Diamond' Dan" Lavoie
twitchy bot original code by Matthew McNamara <https://github.com/MattMcNam/twitchy>

pystats plugin is used to pull the most recent sizzling stats log file fromsizzlingstats.com. The triggering command
is !stats <str> with <str> being an optional parameter. This parameter is defaulted to the twitch channel username if
it is not stated in the chat command. The bot will find the most recent log for the steamID provided in the command and
post it as a message in chat.


to-do:
add an alt-case for players to redirect twitch usernames to steamurls. text document
add a confirmation notice if the lobby info is more than a day old
"""

from urllib.request import *
from plugins.BasePlugin import BasePlugin

class PystatsPlugin(BasePlugin):
    def __init__(self, twitchy):
        """
        initializes pystats plugin object with the commands
        """
        super(PystatsPlugin, self).__init__(twitchy)

        #self.registerCommand('stats', self.sizzlerHandler)
        self.registerCommand('stats', self.placeholder)

    def placeholder(self, nick, commandArg):
        """
        placeholder function: prints messages to console and chat to confirm
        the plugin is loaded and running
        """
        print("!stats attempted by "+nick)
        self.sendMessage("!stats is under construction, thanks for trying!")
    
    def sizzlerHandler(self, nick, commandArg):
        """
        Reply function to '!stats'. prints to console and calls sizzlerGet to
        post link to sizzlingstats.com
        """
        print("!stats called by "+nick+". I hope this works...")
        steamID= self.Twitch_Channel
        if len(commandArg)==2:
            steamID=commandArg[1]
        self.sendMessage(sizzlerGet(steamID))

    def sizzlerGet(steamID=self.Twitch_Channel):
        """
        given a steam ID in any format, retrieves the latest sizzling stats lobby
        link and returns it
        """
        Steam64=steamidCorrect(str(steamID))
        pagetitle=("http://www.sizzlingstats.com/player/"+Steam64)
        #pagetitle="http://www.fairportrobotics.org"
        print(pagetitle)
        with urlopen(pagetitle) as url:
            s=url.read
        print(s)

    def steamidCorrect(steamID):
        """
        pulls the steam64 id from steamidconverter.com/<steamID>
        can accept customURL, steam64, or steamID

        FORMAT EXAMPLES:
        steamID: STEAM_0:1:25030559
        steam64: 76561198010326847
        customURL: patchesyar
        """
        pagetitle="steamidconverter.com/"+steamID
        print(pagetitle)
        return str(steamID)
        with urlopen(pagetitle) as url:
            s=url.read
        print(s)
