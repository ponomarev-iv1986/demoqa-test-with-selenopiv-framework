import os
from typing import Literal

import pydantic_settings

BASE_DIR = os.path.dirname(__file__)

ContextType = Literal['local', 'remote']


class Settings(pydantic_settings.BaseSettings):
    context: ContextType = 'local'
    selenoid_login: str
    selenoid_password: str


settings = Settings(_env_file=os.path.join(BASE_DIR, '.env'))
