class OlympException(Exception):
    """Base exception for olymp-system project"""

    HTTP_STATUS = 400

    def __init__(self, message='', payload=None):
        if payload is None:
            payload = {}
        super().__init__(message, payload)
        self.message = message
        self.payload = payload


if __name__ == '__main__':
    raise OlympException(payload={})
