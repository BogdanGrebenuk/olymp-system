from validators import Validator


class RequestValidator(Validator):

    def __init__(self, schema, data_manager=None):
        if data_manager is None:
            data_manager = JSONBodyManager
        self.schema = schema
        self.data_manager = data_manager

    async def validate(self, request):
        raw_data = await self.data_manager.load(request)
        data = self.schema().load(raw_data)
        self.data_manager.set(request, data)


class DataManager:

    def __init__(self, loader, request_attr):
        self.loader = loader
        self.request_attr = request_attr

    async def load(self, request):
        return await self.loader(request)

    def set(self, request, data):
        request[self.request_attr] = data


async def load_json(request):
    return await request.json()


async def load_form_data(request):
    return await request.post()


async def load_params(request):
    return request.rel_url.query


JSONBodyManager = DataManager(load_json, 'body')
DataFormManager = DataManager(load_form_data, 'body')
ParamsManager = DataManager(load_params, 'params')
