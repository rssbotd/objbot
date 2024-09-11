# This file is placed in the Public Domain.
# pylint: disable=W0613,W0718


"client"


from .broker  import Broker
from .command import command
from .object  import Object
from .reactor import Reactor


class Client(Reactor):

    "Client"

    cache = Object()

    def __init__(self):
        Reactor.__init__(self)
        Broker.register(self)
        self.register("command", command)

    def display(self, evt):
        "display event results."
        for text in evt.result:
            self.say(evt.channel, text)

    def dosay(self, channel, txt):
        "make say."
        self.raw(txt)

    def say(self, channel, txt):
        "echo on verbose."
        self.raw(txt)

    def raw(self, txt):
        "print to screen."
        raise NotImplementedError


def __dir__():
    return (
       'Client',
    )
