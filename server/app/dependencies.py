from app.repositories.parameter_repository import ParameterRepository
from app.services.tts_service import TtsService

# repo jako singleton w pamięci
param_repo = ParameterRepository()


def get_parameter_repository():
    return param_repo


def get_tts_service(repo: ParameterRepository = Depends(get_parameter_repository)):
    return TtsService(repo)