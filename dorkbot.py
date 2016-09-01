from irc import *
import os
import random

channel = "#2dorks"
server = "irc.freenode.net"
nickname = "dorkbot"

irc = IRC()
irc.connect(server, channel, nickname)

while 1:
    text = irc.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!" + '\r\n')

    if "PRIVMSG" in text and channel in text and "!potato" in text:
        irc.send(channel, "Po-tate-ohs!" + '\r\n')
