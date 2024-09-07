# This file is placed in the Public Domain.


"list of commands"


from objx.object  import keys
from objz.client import Commands


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))


Commands.add(cmd)
