from abc import ABC
from typing import Any, Union

from mcdreforged.api.all import *
from my_plugin import constants, mcdr_globals

def tr(key: str, *args, **kwargs) -> RTextBase:
    return ServerInterface.si().rtr(constants.PLUGIN_ID + '.' + key, *args, **kwargs)

def mk_cmd(s: str) -> str:
    cmd = constants.PREFIX
    if len(s) > 0:
        cmd += ' ' + s
    return cmd

def click_and_run(message: Any, text: Any, command: str) -> RTextBase:
    return RTextBase.from_any(message).h(text).c(RAction.run_command, command)

def __make_message_prefix() -> RTextBase:
    return RTextList(RText('[MY]', RColor.dark_aqua).h('My Plugin'), ' ')

def reply_message(source: CommandSource, msg: Union[str, RTextBase], *, with_prefix: bool = True):
    if with_prefix:
        msg = RTextList(__make_message_prefix(), msg)
    source.reply(msg)

def broadcast_message(msg: Union[str, RTextBase], *, with_prefix: bool = True):
    if with_prefix:
        msg = RTextList(__make_message_prefix(), msg)
    mcdr_globals.server.broadcast(msg)