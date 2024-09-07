# This file is placed in the Public Domain.


"client"


class Client:

    "Client"

    out = None

    def __init__(self, outer=None):
        self.out = outer

    def say(self, _channel, txt):
        "echo on verbose."
        self.raw(txt)

    def raw(self, txt):
        "print to screen."
        if self.out:
            txt = txt.encode('utf-8', 'replace').decode()
            self.out(txt)

    def show(self, evt):
        "show results into a channel."
        for txt in evt.result:
            self.say(evt.channel, txt)


def __dir__():
    return (
       'Client',
    )
