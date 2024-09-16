import functools
from typing import Optional
from mcdreforged.api.all import *

class Config(Serializable):
    locations_per_page: int = 10

    @classmethod
    @functools.lru_cache
    def __get_default(cls) -> 'Config':
        return Config.get_default()

    @classmethod
    def get(cls) -> 'Config':
        if _config is None:
            return cls.__get_default()
        return _config
    
def set_config_instance(cfg: Config):
    global _config
    _config = cfg


_config: Optional[Config] = None