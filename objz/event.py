# This file is placed in the Public Domain.
# pylint: disable=R0902


"event"


import threading


from .default import Default


class Event(Default):

    "Event"

    def __init__(self):
        self.orig    = ""
        self.result  = []
        self.txt     = ""
        self.type    = "command"

    def reply(self, txt):
        "add text to the result"
        self.result.append(txt)


def __dir__():
    return (
        'Event',
    )
