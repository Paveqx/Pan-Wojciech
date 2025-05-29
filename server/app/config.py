import os
from pydantic_settings import BaseSettings


def _get_env(var: str, default):
    return os.getenv(var, default)

class Settings(BaseSettings):
    tts_rate: int = int(_get_env("TTS_RATE", 150))
    tts_volume: float = float(_get_env("TTS_VOLUME", 1.0))
    tts_voice: str = _get_env("TTS_VOICE", "")

settings = Settings()

import os
from pydantic import BaseSettings


def _get_env(var: str, default):
    return os.getenv(var, default)

class Settings(BaseSettings):
    tts_rate: int = int(_get_env("TTS_RATE", 150))
    tts_volume: float = float(_get_env("TTS_VOLUME", 1.0))
    tts_voice: str = _get_env("TTS_VOICE", "")

settings = Settings()