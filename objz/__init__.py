# This file is placed in the Public Domain.
# pylint: disable=R0903,W0105,W0718,E1102


"shell"


import os
import pathlib
import pwd
import time
import _thread


from objr import Reactor
from objt import launch
from objw import Workdir
from objx import Default


rpr = object.__repr__


"broker"


class Broker:

    "Broker"

    objs = []

    @staticmethod
    def all():
        "return all objects."
        return Broker.objs

    @staticmethod
    def get(orig):
        "return object by matching repr."
        res = None
        for obj in Broker.objs:
            if rpr(obj) == orig:
                res = obj
                break
        return res

    @staticmethod
    def register(obj):
        "add bot."
        Broker.objs.append(obj)


"config"


class Config(Default):

    "Config"

    def __init__(self, name):
        self.name    = name
        self.wdr     = os.path.expanduser(f"~/.{name}")
        self.pidfile = os.path.join(self.wdr, f"{name}.pid")
        Workdir.wdr  = self.wdr

"event"


class Event:

    "Event"

    def __init__(self):
        self.orig    = ""
        self.result  = []
        self.txt     = ""

    def reply(self, txt):
        "add text to the result"
        self.result.append(txt)


"logging"

class Logging:

    "Logging"

    filter = []
    out = None


def debug(txt):
    "print to console."
    for skp in Logging.filter:
        if skp in txt:
            return
    if Logging.out:
        Logging.out(txt)


def enable(outer):
    "enable logging"
    Logging.out = outer


"commands"


class Commands:

    "Commands"

    cmds     = {}
    modnames = {}

    @staticmethod
    def add(func):
        "add command."
        Commands.cmds[func.__name__] = func
        if func.__module__ != "__main__":
            Commands.modnames[func.__name__] = func.__module__


def command(bot, evt):
    "check for and run a command."
    parse(evt)
    func = Commands.cmds.get(evt.cmd, None)
    if func:
        func(evt)
        bot.display(evt)


"utilities"


def forever():
    "it doesn't stop, until ctrl-c"
    while True:
        try:
            time.sleep(1.0)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def initer(modstr, *pkgs, disable=None):
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


def laps(seconds, short=True):
    "show elapsed time."
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    yea = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    yeas = int(nsec/yea)
    nsec -= yeas*yea
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if yeas:
        txt += f"{yeas}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def modnames(*args):
    "return module names."
    res = []
    for arg in args:
        res.extend([x for x in dir(arg) if not x.startswith("__")])
    return sorted(res)


def parse(obj, txt=None):
    "parse a string for a command."
    args = []
    obj.args    = obj.args or []
    obj.cmd     = obj.cmd or ""
    obj.gets    = obj.gets or Default()
    obj.hasmods = obj.hasmod or False
    obj.index   = None
    obj.mod     = obj.mod or ""
    obj.opts    = obj.opts or ""
    obj.result  = obj.reult or []
    obj.sets    = obj.sets or Default()
    obj.txt     = txt or obj.txt or ""
    obj.otxt    = obj.txt
    _nr = -1
    for spli in obj.otxt.split():
        if spli.startswith("-"):
            try:
                obj.index = int(spli[1:])
            except ValueError:
                obj.opts += spli[1:]
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            val = getattr(obj.gets, key, None)
            if val:
                value = val + "," + value
                setattr(obj.gets, key, value)
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                obj.hasmods = True
                if obj.mod:
                    obj.mod += f",{value}"
                else:
                    obj.mod = value
                continue
            setattr(obj.sets, key, value)
            continue
        _nr += 1
        if _nr == 0:
            obj.cmd = spli
            continue
        args.append(spli)
    if args:
        obj.args = args
        obj.txt  = obj.cmd or ""
        obj.rest = " ".join(obj.args)
        obj.txt  = obj.cmd + " " + obj.rest
    else:
        obj.txt = obj.cmd or ""


def pidfile(pid):
    "write the pid to a file."
    if os.path.exists(pid):
        os.unlink(pid)
    path = pathlib.Path(pid)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(pid, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


def privileges(username):
    "drop privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def spl(txt):
    "split comma separated string into a list."
    try:
        res = txt.split(',')
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def wrap(func):
    "catch exceptions"
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        pass


def __dir__():
    return (
        'Broker', 
        'Config',
        'Logging',
        'Event',
        'debug',
        'enable'
        'forever',
        'initer',
        'laps',
        'modnames',
        'parse',
        'pidfile',
        'privileges',
        'spl',
        'wrap'
    )
