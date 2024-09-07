# This file is placed in the Public Domain.
# pylint: disable=W0718


"main"


from .client  import Client
from .command import command
from .event   import Event
from .log     import Logging
from .parse   import parse
from .utils   import spl


from objx.object import fmt


def cmnd(txt, outer):
    "do a command using the provided output function."
    clt = Client(outer)
    evt = Event()
    evt.txt = txt
    command(evt)
    clt.show(evt)
    return evt


def enable(outer):
    "enable printing."
    Client.out = Logging.out = outer


def init(modstr, *pkgs, disable=None):
    "scan modules for commands and classes"
    thrs = []
    for mod in spl(modstr):
        if disable and mod in spl(disable):
            continue
        for pkg in pkgs:
            modi = getattr(pkg, mod, None)
            if not modi:
                continue
            if "init" not in dir(modi):
                continue
            modi.init()
            break
    return thrs


def wrap(func):
    "catch exceptions"
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        pass


def __dir__():
    return (
        'boot',
        'cmnd',
        'enable',
        'init',
        'wrap'
    )
