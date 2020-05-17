import time

import jwt

from exceptions.token import (
    TokenHeaderNotFound,
    InvalidTokenHeaderFormat
)


def get_token(request):
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


def create_token(payload, token_config):
    token = jwt.encode(
        {
            **payload,
            'exp': int(time.time()) + int(token_config['expiration_time'])
        },
        token_config['secret'],
        algorithm=token_config['algorithm']
    )
    return token.decode(encoding='utf-8')


def decode_token(token: str, token_config):
    token = token.encode(encoding='utf-8')
    payload = jwt.decode(
        token, token_config['secret'], algorithm=token_config['algorithm']
    )
    return payload

