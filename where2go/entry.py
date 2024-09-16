from typing import Optional
from mcdreforged.api.all import *

from where2go import mcdr_globals
from where2go.command import CommandManager
from where2go.config import Config, set_config_instance
from where2go.loacations import LocationStorage

command_manager: Optional[CommandManager] = None
config: Optional[Config] = None
loacation_storage: Optional[LocationStorage] = None

mcdr_globals.load()

def on_load(server: PluginServerInterface, old):
    global command_manager, config, loacation_storage
    try:
        config = server.load_config_simple(target_class=Config, failure_policy='raise')
        set_config_instance(config)
    except Exception as e:
        server.logger.error('Failed to load config: {}'.format(e))
    try:
        command_manager = CommandManager(server)
    except Exception as e:
        server.logger.error('failed to load command: {}'.format(e))



