**NAME**

::

    OBJBOT - objects bot


**SYNOPSIS**

::

    objbot  <cmd> [key=val] [key==val]
    objbotc [-i] [-v]
    objbotd
    objbots


**DESCRIPTION**

OBJBOT is a oython3 bot, it can connect to IRC, fetch and display RSS
feeds, take todo notes, keep a shopping list and log text. You can
also copy/paste the service file and run it under systemd for 24/7
presence in a IRC channel.


**INSTALL**


installation is done with pipx

::

    $ pipx install objbot
    $ pipx ensurepath


**USAGE**


without any argument the bot does nothing

::

    $ objbot
    $

see list of commands

::

    $ objbot cmd
    cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,
    pwd,rem,req,res,rss,srv,syn,tdo,thr,upt


start a console

::

    $ objbotc
    >

use -i to init modules

::

    $ objbotc -i
    >

start daemon

::

    $ objbotd
    $

start service

::

    $ objbots
    <runs until ctrl-c>


**COMMANDS**


here is a list of available commands

::

    cfg - irc configuration
    cmd - commands
    dpl - sets display items
    err - show errors
    exp - export opml (stdout)
    imp - import opml
    log - log text
    mre - display cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    res - restore deleted feeds
    rss - add a feed
    syn - sync rss feeds
    tdo - add todo item
    thr - show running threads
    upt - show uptime


**CONFIGURATION**


*irc*

::

    $ objbot cfg server=<server>
    $ objbot cfg channel=<channel>
    $ objbot cfg nick=<nick>

*sasl*

::

    $ objbot pwd <nsvnick> <nspass>
    $ objbot cfg password=<frompwd>4

*rss*

::
 
    $ objbot rss <url>
    $ objbot dpl <url> <item1,item2>
    $ objbot rem <url>
    $ objbot nme <url> <name>

*opml*

::

    $ objbot exp
    $ objbot imp <filename>


**SYSTEMD**

::

    $ objbot srv > objbot.service
    $ sudo mv objbot.service /etc/systemd/system/
    $ sudo systemctl enable objbot --now


    joins #objbot on localhost


**SOURCE**


source is at ``https://github.com/rssbotd/objbot``


**FILES**

::

    ~/.objbot
    ~/.local/bin/objbot
    ~/.local/bin/objbotc
    ~/.local/bin/objbotd
    ~/.local/bin/objbots
    ~/.local/pipx/venvs/objbot/*


**AUTHOR**

Bart Thate ``<rssbotd@gmail.com>``


**COPYRIGHT**


``OBJBOT`` is Public Domain.
