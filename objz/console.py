# This file is placed in the Public Domain.


"console"


import _thread


from .client  import Client
from .command import command
from .event   import Event


class Console(Client):

    "Console"

    def loop(self):
        "proces events until interrupted."
        while True:
            try:
                evt = self.poll()
                command(evt)
                self.show(evt)
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def poll(self):
        "poll console and create event."
        evt      = Event()
        evt.txt  = input("> ")
        evt.type = "command"
        return evt


def __dir__():
    return (
        'Console',
    )
