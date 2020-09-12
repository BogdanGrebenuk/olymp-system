import abc
from asyncio import gather
from datetime import datetime

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Transformer(abc.ABC):

    @abc.abstractmethod
    async def transform(self, entity):
        ...

    async def transform_many(self, entities):
        return await gather(*[
            self.transform(entity)
            for entity in entities
        ])


class DatetimeTransformer(Transformer):
    def transform(self, dt: datetime):
        return dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')


transformer_container = containers.DynamicContainer()
transformer_container.datetime_transformer = providers.Singleton(DatetimeTransformer)
