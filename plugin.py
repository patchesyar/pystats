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

Note: Currently the prediction functions do not... function. This is meant to update current progress on the
program
"""

from urllib.request import *
from plugins.BasePlugin import BasePlugin

class PystatsPlugin(BasePlugin):
    predsOn= True
    predslist=[]
    def __init__(self, twitchy):
        """
        initializes pystats plugin object with the commands
        """
        super(PystatsPlugin, self).__init__(twitchy)

        #self.registerCommand('stats', self.sizzlerHandler)
        self.registerCommand('stats', self.placeholder)
        self.registerCommand('subtest', self.subtestHandler)
        """
        self.registerCommand('predstart', self.predStarter)
        self.registerCommand('predstop', self.predStopper)
        self.registerCommand('pred', self.predIntake)
        self.registerCommand('predcheck', self.predChecker)
        self.registerCommand('predlist', self.predLister)
        #remember to clear predslist in predcheck
"""
    def predStart(self, nick, commandArg):
        if nick== 'tomdiamond' or nick== 'raysfire' or nick== 'twilitlord':
            print("predictions are enabled")
            #global predsOn=True

    def predStop(self, nick, commandArg):
        if nick== 'tomdiamond' or nick== 'raysfire' or nick=='twilitlord;':
            print("predictions are disabled")
            #global predsOn=False

    def pred(self, nick, commandArg):
        if predsOn:
            print(nick+" has made a prediction")
            if len(commandArg)==2:
                count=0
                for element in predslist:
                    if element[0]== nick:
                        global predslist.remove(count)
                    count+=count
                global predslist.append((nick, commandArg[1]))
            else:
                self.sendMessage("Hey "+nick+", you can make a prediction with '!pred x:y'")
            
    def predChecker(self, nick, commandArg):
        if nick== 'tomdiamond' or nick== 'raysfire' or nick=='twilitlord;':
            print(nick+" is checking the preds"):
            if len(commandArg)!=2:
                self.sendMessage("Hey "+nick+", remember to add the correct kd too!")
            else:
                chickendinner=False
                for element in predslist:
                    if predslist[1]== commandArg[1]:
                        self.sendMessage(predslist[0]+" correctly guessed the kd and won the prediction contest!")
                        chickendinner=True
                if not chickendinner:
                    self.sendMessasge("Nobody won the prediction contest this time")
                global predslist=[]

    def predlist(self, nick, commandArg):
        if len(commandArg)==1:
            predmakers=""
            for element in global predslist:
                predmakers+=(element[0]+" ")
            self.sendMessage(predmakers) #returns the list of all the people that made predictions
        else:
            for element in global predslist:
                if element[0]==commandArg[1]:
                    self.sendMessage(element[1]) #returns the kd prediction for a certain player
                    

    def subtestHandler(self, nick, commandArg):
        self.sendMessage("I got "+ findSubstitutes())

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

    def sizzlerGet(steamID):
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

    def findSubstitutes():
        twitchname
        for line in open("substitutes.txt"):
            inline=line.split(" ")
            if twitchname!=inline[0]:
                break
            else:
                return inline[1]
        return twitchname
