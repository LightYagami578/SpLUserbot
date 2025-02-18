from Spoiled.Database.sudo import add_sudo, del_sudo, is_sudo, get_sudos
from pyrogram import Client, filters
from pyrogram.types import Message
from Spoiled.Utils import get_id, eor
from config import STUFF
from . import add_command

hl = STUFF.COMMAND_HANDLER

@Client.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.me)
async def add_or_del_sudo(_, m):
    try:
        id = await get_id(_, m)
    except:
        return await eor(m, f"<i>{hl}addsudo or {hl}rmsudo [Reply | Username | Id]</id>")
    sudo = await is_sudo(id)
    if m.text.split()[0][1].lower() == "r":
        if not sudo:
            return await eor(m, f"<i>This user isn't sudo..!</i>")
        await del_sudo(id)
        return await eor(m, f"<i>Sudo removed for the user {id} .</i>")
    if sudo:
        return await eor(m, f"<i>{id} is already a sudo user..!</i>")
    await add_sudo(id)
    return await eor(m, f"<i>{id} is added to sudo...!</i>")

@Client.on_message(filters.command("sudos", hl))
async def sudo_users(_, m):
    me = await _.get_me()
    sudo = await is_sudo(m.from_user.id)
    if m.from_user.id != me.id and not sudo:
        return
    SUDOS = await get_sudos()
    if not SUDOS:
        return await eor(m, f"<i>No sudo users..!</i>")
    msg = ""
    for SUDO in SUDOS:
        SUDO = int(SUDO)
        msg += f"\n<code>{SUDO}</code>"
    return await eor(m, f"<i>Sudo :-</i>\n{msg}\n\n<i>Count :- {len(SUDOS)}</i>")

command = "Sudo"
help = f"`» {hl}addsudo - add user as sudo.\n\n» {hl}rmsudo - remove user as sudo.\n\n» {hl}sudos - get sudo users.`"

add_command(command, help)
