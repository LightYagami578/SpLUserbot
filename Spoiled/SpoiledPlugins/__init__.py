import time
from config import STUFF
from Spoiled.Utils import *
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

hl = STUFF.COMMAND_HANDLER

startTime = time.time()

COMMANDS_HELP = {}

def add_command(command, help):
    global COMMANDS_HELP
    COMMANDS_HELP[command] = help

def build_help_markup(set):
    le = len(set)
    rows = le // 3
    rows += 1
    rem = le % 3
    buttons = []
    y = []
    a = 0
    filled = 0
    for each in set:
        x = IKB(each, callback_data=set[each].lower())
        y.append(x)
        a += 1
        if a == 3:
            buttons.append(y)
            filled += 1
            a = 0
            y = []
        if filled == (rows - 1):
            if set.index(each) == (le - 1):
                buttons.append(y)
                y = []
    final = IKM(buttons)
    return final
                
    
