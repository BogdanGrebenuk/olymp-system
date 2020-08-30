import time

import jwt
from dependency_injector import providers, containers

from app.containers.application import application_container
from app.exceptions import OlympException


class TokenException(OlympException):
    """Base exception for token-related exceptions"""


class TokenHeaderNotFound(TokenException):
    """Raised when authorization header isn't presented in request"""


class InvalidTokenHeaderFormat(TokenException):
    """Raised when token header has wrong format"""


class InvalidTokenContent(TokenException):
    """Raised when token contains invalid information

    For example, token contains id of non-existent user
    """


class TokenGenerator:

    def __init__(self, generator, config, executor):
        self.generator = generator
        self.config = config
        self.executor = executor

    async def generate(self, payload: dict) -> str:
        return await self.executor.run(
            self.generator,
            payload,
            self.config
        )


class TokenDecoder:

    def __init__(self, decoder, config, executor):
        self.decoder = decoder
        self.config = config
        self.executor = executor

    async def decode(self, token: str) -> dict:
        return await self.executor.run(
            self.decoder, token, self.config
        )


def extract_token(request) -> str:
    token_header = request.headers.get('Authorization')
    if token_header is None:
        raise TokenHeaderNotFound('Authorization header is not found!')
    try:
        _, token = token_header.split()
        return token
    except ValueError:
        raise InvalidTokenHeaderFormat(
            'token header must me in format "<scheme> <token>"'
        )


def generate_token(payload: dict, config: dict) -> str:
    token = jwt.encode(
        {
            **payload,
            'exp': int(time.time()) + int(config['expiration_time'])
        },
        config['secret'],
        algorithm=config['algorithm']
    )
    return token.decode(encoding='utf-8')


def decode_token(token: str, config: dict) -> dict:
    token = token.encode(encoding='utf-8')
    payload = jwt.decode(
        token,
        config['secret'],
        algorithm=config['algorithm']
    )
    return payload


token_services_container = containers.DynamicContainer()
token_services_container.token_generator = providers.Singleton(
    TokenGenerator,
    generator=generate_token,
    config=application_container.config.token,
    executor=application_container.process_executor
)
token_services_container.token_decoder = providers.Singleton(
    TokenDecoder,
    decoder=decode_token,
    config=application_container.config.token,
    executor=application_container.process_executor
)
token_services_container.token_extractor = providers.Object(
    extract_token
)
