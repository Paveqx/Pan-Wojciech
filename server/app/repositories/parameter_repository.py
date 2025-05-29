from typing import Any, Dict

class ParameterRepository:
    def __init__(self):
        self._params: Dict[str, Any] = {}

    def get(self, name: str) -> Any:
        return self._params.get(name)

    def set(self, name: str, value: Any) -> None:
        self._params[name] = value

    def all(self) -> Dict[str, Any]:
        return dict(self._params)