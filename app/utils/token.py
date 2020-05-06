import time

import jwt


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

