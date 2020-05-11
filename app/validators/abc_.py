from abc import ABC, abstractmethod


class Validator(ABC):

    @abstractmethod
    async def validate(self, request):
        ...
