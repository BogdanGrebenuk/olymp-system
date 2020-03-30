from services.codesaver.savers import save_python


def get_saver(language):
    if language == 'python':
        return save_python
    ...  # TODO: other languages savers
    raise ValueError(f'there is no code saver for language {language}')
