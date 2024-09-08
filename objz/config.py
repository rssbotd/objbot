# This file is placed in the Public Domain.
# pylint: disable=R0902,R0903


"configuration"


import os


from objw.workdir import Workdir
from objx.default import Default


class Config(Default):

    "Config"

    def __init__(self, name):
        Default.__init__(self)
        self.name    = name
        self.wdr     = os.path.expanduser(f"~/.{name}")
        self.pidfile = os.path.join(self.wdr, f"{name}.pid")
        Workdir.wdr  = self.wdr


def __dir__():
    return (
        "Config",
    )
