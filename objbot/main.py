# This file is placed in the Public Domain.
# pylint: disable=W0718


"main"


from objt.thread import launch


from .client  import Client, command
from .console import Console
from .event   import Event
from .log     import Logging
from .utils   import spl


rpr = object.__repr__


def enable(outer):
    "enable printing."
    Logging.out = outer


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
            launch(modi.init)
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
