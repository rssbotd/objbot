# This file is placed in the Public Domain.


"console"


import _thread


from .command import command
from .event   import Event


class Console:

    "Console"

    out = None

    def __init__(self, outer):
        self.out = outer

    def announce(self, txt):
        "echo text"

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

    def raw(self, txt):
        "echo text."
        if self.out:
            self.out(txt)

    def show(self, evt):
        "show results."
        for text in evt.result:
            self.raw(text)


def __dir__():
    return (
        'Console',
    )
