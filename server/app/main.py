from fastapi import FastAPI
from app.controllers.speech_controller import router as speech_router

app = FastAPI()
app.include_router(speech_router, prefix="/api")