import os

import pydantic_settings

BASE_DIR = os.path.dirname(__file__)


class Settings(pydantic_settings.BaseSettings):
    pass
