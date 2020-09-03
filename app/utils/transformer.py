import abc
from asyncio import gather


class Transformer(abc.ABC):

    @abc.abstractmethod
    async def transform(self, entity):
        ...

    async def transform_many(self, entities):
        return await gather(*[
            self.transform(entity)
            for entity in entities
        ])
