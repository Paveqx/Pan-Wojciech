from fastapi import APIRouter, Depends, HTTPException, Response
from app.models.parameter import Parameter
from app.services.tts_service import TtsService
from app.dependencies import get_tts_service, get_parameter_repository

router = APIRouter()

@router.post("/to_speech")
async def to_speech(payload: dict, tts: TtsService = Depends(get_tts_service)):
    text = payload.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Brak tekstu do syntezy")
    audio = tts.synthesize(text)
    return Response(content=audio, media_type="audio/wav")

@router.patch("/set_parameter")
async def set_parameter(param: Parameter, repo=Depends(get_parameter_repository)):
    repo.set(param.name, param.value)
    return repo.all()