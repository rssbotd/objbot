# This file is placed in the Public Domain.


"main"


from objt.thread import launch
from objz.utils  import spl


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
