import io
import pyttsx3
from fastapi import HTTPException
from app.repositories.parameter_repository import ParameterRepository
from app.config import settings

class TtsService:
    def __init__(self, repo: ParameterRepository):
        self.repo = repo

    def synthesize(self, text: str) -> bytes:
        engine = pyttsx3.init()
        rate = self.repo.get('rate') or settings.tts_rate
        volume = self.repo.get('volume') or settings.tts_volume
        voice = self.repo.get('voice') or settings.tts_voice

        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        if voice:
            engine.setProperty('voice', voice)

        buf = io.BytesIO()
        engine.save_to_file(text, 'output.wav')
        engine.runAndWait()

        with open('output.wav', 'rb') as f:
            data = f.read()
        return data