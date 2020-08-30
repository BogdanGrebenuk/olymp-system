from dataclasses import dataclass
from typing import Union, List, Callable, Awaitable

from aiohttp.web_request import BaseRequest

from utils.request import Validator


@dataclass
class Resource:
    method: str
    url: str
    allowed_roles: Union[List, None]  # if None, there is no restrictions
    validators: List[Validator]
    handler: Callable[[BaseRequest], Awaitable]


class SingleParamChooser:
    """Class that implement custom route resolving
    basing on presence of specified query parameter

    For example, there is one URI for accessing solutions for
    all contest (1) and solutions for team (2):
    (1) /api/contests/{contest_id}/solutions
    (2) /api/contests/{contest_id}/solutions?team_id={team_id}

    For keeping handler simple there will be two handlers,
    that object of this class will manipulate

    """
    def __init__(self, param_name, found_handler, missing_handler):
        self.param_name = param_name
        self.found_handler = found_handler
        self.missing_handler = missing_handler

    async def handle(self, request):
        if request['params'].get(self.param_name):
            return await self.found_handler(request)
        else:
            return await self.missing_handler(request)


def combine_resources(*resources):
    result = []
    for r in resources:
        result += r
    return result
