from validators import Validator


class BodyValidator(Validator):

    def __init__(self, schema, data_loader=None):
        if data_loader is None:
            data_loader = json_loader
        self.schema = schema
        self.data_loader = data_loader

    async def validate(self, request):
        data = await self.data_loader(request)
        body = self.schema().load(data)
        request['body'] = body


async def json_loader(request):
    return await request.json()


async def form_data_loader(request):
    return await request.post()
